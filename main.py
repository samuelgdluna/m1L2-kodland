import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

user = int(input("Quantos caracters deseja que a senha tenha?"))

password = ""

for i in range(user):
    password += random.choice(elements)

print("Sua senha é: " + password)