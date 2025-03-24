import random
passlen = int(input("Enter the length of password: "))
s = "abchjfeioeklkahuffjdcvuj1w283749836281828@#^$*^%$&*AEHRFJDIEODENGVYIGHRBFYIFJMSJ"
p = "".join(random.sample(s, passlen))
print(p)
