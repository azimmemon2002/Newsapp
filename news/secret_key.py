# importing the function from utils
from django.core.management.utils import get_random_secret_key

# generating and printing the SECRET_KEY
print("Below is your secret key add into seeting.py\n\n")
print(get_random_secret_key())