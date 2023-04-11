tags:: [[unread]]
title:: @A Neural Probabilistic Language Model
item-type:: [[journalArticle]]
original-title:: A Neural Probabilistic Language Model
language:: en
authors:: [[Yoshua Bengio]], [[Réjean Ducharme]], [[Pascal Vincent]], [[Christian Jauvin]]
library-catalog:: Zotero
links:: [Local library](zotero://select/library/items/LFVFLJ6J), [Web library](https://www.zotero.org/users/6786528/items/LFVFLJ6J)

- [[Abstract]]
	- A goal of statistical language modeling is to learn the joint probability function of sequences of words in a language. This is intrinsically difﬁcult because of the curse of dimensionality: a word sequence on which the model will be tested is likely to be different from all the word sequences seen during training. Traditional but very successful approaches based on n-grams obtain generalization by concatenating very short overlapping sequences seen in the training set. We propose to ﬁght the curse of dimensionality by learning a distributed representation for words which allows each training sentence to inform the model about an exponential number of semantically neighboring sentences. The model learns simultaneously (1) a distributed representation for each word along with (2) the probability function for word sequences, expressed in terms of these representations. Generalization is obtained because a sequence of words that has never been seen before gets high probability if it is made of words that are similar (in the sense of having a nearby representation) to words forming an already seen sentence. Training such large models (with millions of parameters) within a reasonable time is itself a signiﬁcant challenge. We report on experiments using neural networks for the probability function, showing on two text corpora that the proposed approach signiﬁcantly improves on state-of-the-art n-gram models, and that the proposed approach allows to take advantage of longer contexts.
- [[Attachments]]
	- [Bengio et al_A Neural Probabilistic Language Model.pdf](zotero://select/library/items/3NWR9ZPD) {{zotero-linked-file "/Users/kexinwei/GoogleDrive/ZoteroFiles/Bengio et al_A Neural Probabilistic Language Model.pdf"}}