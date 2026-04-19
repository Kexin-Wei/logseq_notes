"""
Add papers from Surgical AI Literature Review to Zotero collections.

S1 (Foundations) & S2 (World Models) → AI & Robotics
S3–S8 (Surgical topics)              → Medical Robot
"""

import os
import re
import time
import sys
from pathlib import Path
from dotenv import load_dotenv
from pyzotero import zotero

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

API_KEY = os.getenv("ZOTERO_API_KEY")
USER_ID = os.getenv("ZOTERO_USER_ID")

COLLECTION_AI_ROBOTICS = "2V3H5UWT"
COLLECTION_MEDICAL_ROBOT = "6N24ISGM"

# Sections mapping to collections
AI_ROBOTICS_SECTIONS = {"S1", "S2"}
MEDICAL_ROBOT_SECTIONS = {"S3", "S4", "S5", "S6", "S7", "S8"}

MD_PATH = Path(__file__).resolve().parent / "Surgical AI Literature Review.md"


def parse_papers(md_text: str) -> list[dict]:
    """Parse the markdown and extract papers with their section and identifiers."""
    papers = []
    current_section = None

    section_pattern = re.compile(r"^## (S\d+):")
    row_pattern = re.compile(
        r"^\|\s*(\d+)\s*\|"           # paper number
        r"\s*\[([^\]]+)\]\(([^)]*)\)"  # [title](url)
        r"\s*\|\s*(\d{4})\s*\|"       # year
        r".*?\|\s*(\[[^\]]*\])"        # source tags like [Z][N] or [NEW]
    )

    for line in md_text.splitlines():
        sm = section_pattern.match(line)
        if sm:
            current_section = sm.group(1)
            continue

        if current_section is None:
            continue

        rm = row_pattern.match(line)
        if rm:
            num, title, url, year, source = rm.groups()
            paper = {
                "num": int(num),
                "title": title.strip(),
                "url": url.strip(),
                "year": int(year),
                "source": source.strip(),
                "section": current_section,
            }

            arxiv_match = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", url)
            if arxiv_match:
                paper["arxiv_id"] = arxiv_match.group(1)

            doi_match = re.search(r"doi\.org/(10\..+)", url)
            if doi_match:
                paper["doi"] = doi_match.group(1)

            papers.append(paper)

    return papers


def get_collection(section: str) -> str:
    if section in AI_ROBOTICS_SECTIONS:
        return COLLECTION_AI_ROBOTICS
    return COLLECTION_MEDICAL_ROBOT


def add_paper_by_arxiv(zot: zotero.Zotero, arxiv_id: str, collection_key: str) -> bool:
    template = zot.item_template("preprint")
    template["creators"] = []
    template["title"] = f"arXiv:{arxiv_id}"
    template["url"] = f"https://arxiv.org/abs/{arxiv_id}"
    template["archive"] = "arXiv"
    template["archiveID"] = f"arXiv:{arxiv_id}"
    template["collections"] = [collection_key]
    try:
        resp = zot.create_items([template])
        return bool(resp.get("successful") or resp.get("success"))
    except Exception as e:
        print(f"  Error: {e}")
        return False


def add_paper_by_doi(zot: zotero.Zotero, doi: str, collection_key: str) -> bool:
    template = zot.item_template("journalArticle")
    template["DOI"] = doi
    template["url"] = f"https://doi.org/{doi}"
    template["collections"] = [collection_key]
    try:
        resp = zot.create_items([template])
        return bool(resp.get("successful") or resp.get("success"))
    except Exception as e:
        print(f"  Error: {e}")
        return False


def check_existing(zot: zotero.Zotero) -> set[str]:
    existing = set()
    items = zot.everything(zot.items(itemType="-attachment"))
    for item in items:
        data = item["data"]
        archive_id = data.get("archiveID", "")
        if "arXiv:" in archive_id:
            existing.add(archive_id.replace("arXiv:", ""))
        url = data.get("url", "")
        m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", url)
        if m:
            existing.add(m.group(1))
        doi = data.get("DOI", "")
        if doi:
            existing.add(doi.lower())
    return existing


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN (no changes will be made) ===\n")

    zot = zotero.Zotero(USER_ID, "user", API_KEY)

    try:
        zot.key_info()
        print("Connected to Zotero API.")
    except Exception as e:
        print(f"Failed to connect: {e}")
        sys.exit(1)

    md_text = MD_PATH.read_text()
    papers = parse_papers(md_text)
    print(f"Found {len(papers)} papers in the literature review.\n")

    print("Checking existing library items...")
    existing = check_existing(zot)
    print(f"Found {len(existing)} existing identifiers.\n")

    added = 0
    skipped = 0
    failed = 0

    for p in papers:
        collection = get_collection(p["section"])
        coll_name = "AI & Robotics" if collection == COLLECTION_AI_ROBOTICS else "Medical Robot"
        identifier = p.get("arxiv_id") or p.get("doi")

        if not identifier:
            print(f"  [{p['num']:2d}] SKIP (no arXiv/DOI): {p['title'][:60]}")
            skipped += 1
            continue

        check_val = identifier if "arxiv_id" in p else identifier.lower()
        if check_val in existing:
            print(f"  [{p['num']:2d}] EXISTS: {p['title'][:60]}")
            skipped += 1
            continue

        if dry_run:
            print(f"  [{p['num']:2d}] WOULD ADD to [{coll_name}]: {p['title'][:60]}")
            added += 1
            continue

        print(f"  [{p['num']:2d}] Adding to [{coll_name}]: {p['title'][:60]}...", end=" ")

        if "arxiv_id" in p:
            ok = add_paper_by_arxiv(zot, p["arxiv_id"], collection)
        else:
            ok = add_paper_by_doi(zot, p["doi"], collection)

        if ok:
            print("OK")
            added += 1
        else:
            print("FAILED")
            failed += 1

        time.sleep(0.5)

    action = "to add" if dry_run else "added"
    print(f"\nDone: {added} {action}, {skipped} skipped, {failed} failed.")


if __name__ == "__main__":
    main()
