from cryptography.fernet import Fernet
import os 
import sys

  

#verify_file(file)
 
 
program = input('file  to  encrypt>')

key = Fernet.generate_key()

with  open('special_key.key' , 'wb') as thekey:
    thekey.write(key)
    thekey.close()


with  open(program ,'r')as filetoencryt:
    file_dta = filetoencryt.read()
    file_enc = Fernet(key).encrypt(file_dta)
    filetoencryt.close()
 


    fzi= program.replace(".py" , "_evilfil.py")
    with open (fzi,"wb")as encryptedfile:
        encryptedfile.write(file_enc)
        encryptedfile.close()
        print('file  key  as  been  save to specialkey  in dir  / including  evilfil.py')
   

with open (program,'r') as key_file:
    key = key_file.read()
    key_file.close()

print("do  you want  to  return dashboard?(yes/no)")

choice=input()

if 'yes' in  choice:
    os.system('python dashboard.py')

elif 'no' in  choice :
    sys.exit(0)