import  base64
import os
import sys
 
program = input('enter file  to  encrypt>')

rec =int(input(""" 

Tips:

 encrytion 1 \t = good
 encrytion  2 \t = best
 encrytion 3  \t = badest

"""))
with open (program, "r") as f:
    file3 = f.read()
    file3 = file3 + '#'*1000
 
def b64(file):
    encodedBytes = base64.b64encode(file.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    return encodedStr

def b32(file):
    encodedBytes = base64.b32encode(file.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    return encodedStr

def b16(file):
    encodedBytes = base64.b16encode(file.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    return encodedStr

encodedStr=file3
for r in range(rec):
    encodedStr=b64(encodedStr)
    encodedStr=b32(encodedStr)
    encodedStr=b16(encodedStr)
    encodedStr="import base64;exec(base64.b64decode((base64.b32decode((base64.b16decode('"+encodedStr+"'))))))"
    print(f"{(r+1)/rec*100:.3f} %", end="\r")

p=program.find('.py')
program=program[:p]+'_encrypted.py'
with open(program, 'w') as f:
    f.write(encodedStr)


    print("do  you want  to  return dashboard?(yes/no)")

choice=input()

if 'yes' in  choice:
    os.system('python dashboard.py')

elif 'no' in  choice :
    sys.exit(0)