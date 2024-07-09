# Password Generator Project
import random
import secrets
import string
from typing import List

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def get_user_input(prompt: str) -> int:
    return int(input(prompt))


def append_characters_to_password(character_count: int, characters: List, password: List) -> List:
    for _ in range(character_count):
        random_character = secrets.choice(characters)
        password.append(random_character)
    return password


def shuffle_characters(password: List) -> List:
    return random.sample(password, len(password))


def join_characters(password: List) -> str:
    return "".join(password)


def generate_secure_password(
    letters_count: int, symbols_count: int, numbers_count: int, letters: List, symbols: List, numbers: List
) -> str:
    password_characters = []

    password_characters = append_characters_to_password(letters_count, letters, password_characters)
    password_characters = append_characters_to_password(symbols_count, symbols, password_characters)
    password_characters = append_characters_to_password(numbers_count, numbers, password_characters)

    shuffled_password_characters = shuffle_characters(password_characters)
    generated_password = join_characters(shuffled_password_characters)

    return generated_password


def main():
    print("Welcome to the Password Generator!")
    letters_count = get_user_input("How many letters would you like in your password?\n")
    symbols_count = get_user_input(f"How many symbols would you like?\n")
    numbers_count = get_user_input(f"How many numbers would you like?\n")

    secure_password = generate_secure_password(letters_count, symbols_count, numbers_count, letters, symbols, numbers)

    print(f"Your password is: {secure_password}")


if __name__ == "__main__":
    main()
