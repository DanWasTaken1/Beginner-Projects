import string
import random
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
def rdm():
  length = random.randint(8, 24)
  temp = random.sample(all,length)
  password = "".join(temp)
  return password
while True:
  print(f"Got Password : {rdm()}")