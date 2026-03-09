- Linux user and group management quick reference.
- All read commands work without sudo — only modifications require admin.
- ## About Yourself
  
  ```bash
  whoami                 # your username
  id                     # your uid, gid, and all groups
  groups                 # your groups (short version)
  sudo -l                # what sudo privileges you have
  passwd                 # change your own password
  ```
- ## Users on the System
  
  ```bash
  cat /etc/passwd        # all users
  getent passwd          # all users (includes network/LDAP users)
  awk -F: '$3 >= 1000 {print $1}' /etc/passwd   # only human users
  ```
- ## Groups on the System
  
  ```bash
  cat /etc/group         # all groups
  getent group           # all groups (includes network/LDAP)
  getent group sudo      # members of a specific group
  getent group docker    # members of a specific group
  awk -F: '$4 == 1007 {print $1}' /etc/passwd   # users with specific primary GID
  ```
- ## Who's Online
  
  ```bash
  who                    # currently logged-in users
  w                      # logged-in users + activity
  last                   # recent login history
  ```
- ## Find What a Group Owns
  
  ```bash
  find / -group docker 2>/dev/null    # files owned by a group
  ```
- ## Admin Only (needs sudo)
  
  ```shell
  sudo groupadd research              # create group
  sudo groupdel research              # delete group
  sudo usermod -aG docker kexin       # add user to group
  sudo gpasswd -d kexin docker        # remove user from group
  ```