import hashlib

a=input("ENTER YOUR STRING :")
result = hashlib.md5(a.encode())

print("THE HEXADECIMAL EQUIVALENT OF HASH IS :",end = " ")
print(result.hexdigest())

print("THE BYTE EQUIVALENT OF HASH IS :",end = " ")
print(result.digest())
