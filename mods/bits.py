# import getpasscd
import sys
import os
import getpass
from colorama import Fore, Back, Style

# Variables
username = getpass.getuser() # Get username
header = Fore.RED + f'{username}' + Fore.WHITE + '@' + Fore.RED + 'SkeletonKey $ ' + Fore.RESET # header for user input
remote_path = 'raw.githubusercontent.com/AlexKollar/Cryptex/master' # remote url path
local_path = f'/home/{username}/.SkeletonKey' if username != 'root' else '/root/.SkeletonKey' # local path to skelkey
cipher = f'{local_path}/ciphers/' # local path to ciphers

# Colors
SUCCESS = '\033[92m'
FAIL = '\033[91m'
END = '\033[0m'

version = open(f'{local_path}/version.txt').read().strip()
banner = Fore.RED + f'''
            SkeletonKey Version : 0.{version}\n
''' + Fore.RESET

help_menu = Fore.CYAN + """
+-------------------------------------------------------------+
| [+] EXAMPLE: key cc -d -t 'This is a string to encrypt'  |
| [+] ARG 1. Cipher                                           |
|       [cc] --------- Caesar Cipher                          |
|       [vc] --------- Vingenere Cipher                       |
|       [rc] --------- Reverse Cipher                         |
|       [mc] --------- Multiplicative Cipher                  |
|       [xor] -------- XOR Cipher                             |
|       [r13] -------- ROT 13                                 |
|       [r47] -------- ROT 47                                 |
|       [b64] -------- Base64                                 |
|       [bin] -------- Binary                                 |
|       [pix] -------- Image Pixel                            |
|       [hex] -------- Hex                                    |
|       [oct] -------- Octal                                  |
|       [mor] -------- Morse Code                             |
|       [pho] -------- Phonetic Alphabet                      |
|       [1337] ------- L33T 5P34K                             |
|       [menc] ------- MENC                                   |
|       [translate] -- Google Translate API                   |
|       [md5] -------- MD5                                    |
|       [se] --------- Static Encryption                      |
|       [cleartext] -- Just Cleartext                         |
+-------------------------------------------------------------+
| [+] ARG 2. Cipher Method                                    |
|       [-e] ---------- Encrypt                               |
|       [-d] ---------- Decrypt                               |
|       [-b] ---------- Break                                 |
| [+] Google Translate API                                    |
|       [-tr] --------- Translate                             |
|       [-lang] ------- List Languages                        |
+-------------------------------------------------------------+
| [+] Additional Arguments                                    |
|       [-t] ---------- Input Text                            |
|       [-i] ---------- Input File                            |
|       [-o] ---------- Output File                           |
|       [-k] ---------- Encryption Key                        |
|       [-r] ---------- Range                                 |
|       [-w] ---------- Wordlist                              |
|       [-src] -------- Source Language                       |
|       [-dest] ------- Destination Language                  |
+-------------------------------------------------------------+
| [+] SkeletonKey Arguments                                       |
|       [--help] ------ help                                  |
|       [--version] --- version                               |
|       [--update] ---- update                                |
+-------------------------------------------------------------+
""" + Fore.RESET
