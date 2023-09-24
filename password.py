import random
import os

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "&#/\^@*?!"

use_for = lower_case + upper_case + number + symbols
length_for_pass = 12

password = "".join(random.sample(use_for, length_for_pass))

print("Le mot de passe généré pour vous est : ",password)