#Disclaimer
-Please take saftey measures before testing out these programs. It could be potentially exposing your computer to dangers while performing such test. 
-Please use Virtual machines such as VMware or VirtualBox. Both are free and safe to use.

# SSH-BruteForce
This is a Brute Force attack on computers using a Wordlist. This Program prompts for the IP address of targeted machine, the user's name and the wordlist selecting.

#More About Project:
  -Host Computer (Your PC): Not Used
  -Guest Computer (Virtual Machine): Kali Linux
  -Target Computer (Virtual Machine): MetaSploitable
      -The Metasploit Project is a computer security project that provides information about security vulnerabilities and aids in penetration testing and IDS signature development.
  -Language: Python
      - Files imported include :
          -paramiko (Gets SSH client necessary to identify machine IP and user)
          -sys
          -os
          -socket
          -threading(made to speed up the password cracking process)
          -time
          -termcolor (for aesthical purposes, to differentiate between valid and invalid entries)
