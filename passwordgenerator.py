import random
import string

def get_length():
  while True:
    try:
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length >= 8:
        return length
      else:
        print("Password must be at least 8 characters long.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols):
  characters = []
  if include_uppercase:
    characters.extend(string.ascii_uppercase)
  if include_lowercase:
    characters.extend(string.ascii_lowercase)
  if include_digits:
    characters.extend(string.digits)
  if include_symbols:
    characters.extend(string.punctuation)

  if not characters:
    characters.extend(random.sample(string.ascii_uppercase, 1))
    characters.extend(random.sample(string.ascii_lowercase, 1))
    characters.extend(random.sample(string.digits, 1))
    characters.extend(random.sample(string.punctuation, 1))

  # Shuffle characters and select desired length
  random.shuffle(characters)
  password = ''.join(random.sample(characters, length))
  return password

def get_complexity():
  include_uppercase = input("Include uppercase letters (y/n)? ").lower() == "y"
  include_lowercase = input("Include lowercase letters (y/n)? ").lower() == "y"
  include_digits = input("Include digits (y/n)? ").lower() == "y"
  include_symbols = input("Include symbols (y/n)? ").lower() == "y"
  return include_uppercase, include_lowercase, include_digits, include_symbols

def main():
  length = get_length()

  include_uppercase, include_lowercase, include_digits, include_symbols = get_complexity()

  password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)

  print(f"Your generated password is: {password}")

if __name__ == "__main__":
  main()
