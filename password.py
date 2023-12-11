import secrets
import random
import string
digit=string.digits
splchar=string.punctuation
letter=string.ascii_letters
len=int(input("enter the length of password:"))
password=""
sel=digit+splchar+letter
for i in range (len):
    password+=''.join(secrets.choice(sel))

print(password)