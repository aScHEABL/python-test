# import random
# import string

# letters = string.ascii_letters
# digits = string.digits
# special_chars = string.punctuation
# combination = letters + digits + special_chars
# pwd_length = 12

# password = "".join(random.sample(combination, pwd_length))

# print('你的新密碼是: ' + password)

import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

combination = letters + digits + special_chars

pwd_length = 12
password = ''

for i in range(pwd_length):
  password += ''.join(secrets.choice(combination))

print('你的新密碼是: ' + password)