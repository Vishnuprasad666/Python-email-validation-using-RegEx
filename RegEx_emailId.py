import re

email=input("Enter your Email ID: ")
pattern=r"^[a-z0-9\_\.\-]+@[a-z0-9]+\.[a-z]{2,}"

res=re.search(pattern,email)
if res:
    print("Your Email ID is Valid")
else:
    print("Your Email ID is Invalid")