import sys

def encrypt(message,mode):
	ret=''; i=0;
	N=ord('Z')+1-ord('A')
	for m in message:
		if m.isalpha():
			m=m.upper()
			M=ord(m)-ord('A')
			K=ord(key[i])-ord('A')
			E=(M+mode*K)%26
			E+=ord('A')
			ret+=chr(E)			
			i=(i+1)%len(key);
		#else: ret+=m
	if mode==-1: ret=ret.lower()
	return ret

if len(sys.argv)!=4:
	print('vigenere.py file key mode'); sys.exit()
file=sys.argv[1]; key=sys.argv[2];
if not(key.isalpha()):
	print('key must contain letters only.'); sys.exit()
key=key.upper()
if sys.argv[3]=='decrypt':
	mode=-1; FILE='decrypted-'+file
else:
	mode=1; FILE='encrypted-'+file

message=''
with open(file) as f:
	message=f.read()

MESSAGE=encrypt(message,mode)

print(message,'\n'); print(MESSAGE)
with open(FILE,'w') as f:
	f.write(MESSAGE)
