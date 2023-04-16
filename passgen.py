from cryptography.fernet import Fernet
key = Fernet.generate_key()
key_utf8 = key.decode('utf-8')
print("THIS PASSWORD IS VERY IMPORTANT, LOOSING IT WILL CAUSE COMPLETE INABILITY TO ACCESS 
PREVIOUSLY SAVED HOSTS AND PASSWORDS, KEEP THIS SAFE", key_utf8)
