# random password generation
import string
import random

upper = string.ascii_uppercase

lower = string.ascii_lowercase

digits = string.digits

special_chars = "!@#$%^&*()_-+=[]\\';.,/<>?:{}"

password1 = ""

# 4 letter password
for lst in [upper, lower, digits, special_chars]:
    password1 += random.choice(lst)
print(password1)

# n letter password. Sample function returns a list of randon unique elements from the passed iterable sequence that is
# of certain length. Here length is n
n = 10
chars = upper + lower + digits + special_chars
password2 = "".join(random.sample(chars, n))
print(password2)
