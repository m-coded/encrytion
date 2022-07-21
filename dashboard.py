 
import subprocess as sp
import os
import pyfiglet
from colorama import Fore, Back, Style

ascii_banner = pyfiglet.figlet_format("!CRYPTER!")
print(Fore.GREEN,ascii_banner)


tile='''
  [+]#######################################################################[+]                                                                                                                                                 
  [+]   Tool created by suject0
                              (crypter fud!! )                              [+]
  [+]                                                                       [+]
  [+]   dicord/subject101                                                   [+]
  [+]#######################################################################[+]
'''

print(Fore.YELLOW, tile)


details = """""

section:

[:] ASE file encrytion \t = 1
[:] base encryption \t = 2

Note:
 section  one  is base  ASE encryt  with  key  rate  256 bit impossible  to  decrypt
 section two  baseencode max simple  encrytion 
"""
print(details)

choice = int(input('>>'))

if choice  == 1:

  os.system('python encrypt.py' )



elif choice  == 2:
  os.system('python crypter.py')