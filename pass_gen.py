# pass_gen.py
# This script generates passwords and performs various operations using Pandas, lists, tuples, and dictionaries.

import string
import random
import pandas as pd


class PasswordGenerator:
    def __init__(self, length, uppercase_num, symbols_num, numbers_num):
        self.length = length
        self.uppercase_num = uppercase_num
        self.symbols_num = symbols_num
        self.numbers_num = numbers_num

    def generate_password(self):
        # 4.3, 4.4, 4.9
        if self.length < self.uppercase_num + self.symbols_num + self.numbers_num:
            raise ValueError("Total number of uppercase, symbols, and numbers should not exceed password length")

        password_characters = random.sample(string.ascii_uppercase, self.uppercase_num) + \
                              random.sample(string.punctuation, self.symbols_num) + \
                              random.sample(string.digits, self.numbers_num)

        remaining_chars = self.length - len(password_characters)
        password_characters += random.sample(string.ascii_lowercase, remaining_chars)

        random.shuffle(password_characters)
        return ''.join(password_characters)


def save_passwords_to_csv(passwords, filename):
    df = pd.DataFrame(passwords, columns=['Password'])
    df.to_csv(filename, index=False)


def read_and_filter_passwords(filename):
    # 8_2 Read CSV
    df = pd.read_csv(filename)

    # 8_3 Subset DataFrame using a boolean
    filtered_df = df[df['Password'].apply(len) > 12]  # Example: Filter passwords longer than 12 characters

    # 8_4 Write filtered data to CSV
    filtered_df.to_csv('filtered_passwords.csv', index=False)


# Example of list and dictionary manipulation
def list_and_dict_operations():
    # 5.9, 5.10, 5.11: List operations
    my_list = []
    for i in range(5):
        my_list.append(i)  # Append item to list
    my_list.remove(3)  # Remove an item

    # 5.15, 5.17, 5.18, 5.19: Dictionary operations
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    for key, value in my_dict.items():
        my_dict[key] = 'new_' + value  # Update values programmatically


# 5.12, 5.13, 5.14: Tuple operations
def tuple_operations():
    my_tuple = (1, 2, 3)
    a, b, c = my_tuple  # Assign tuple members to variables
    return a, b, c


# 2.2 Script Description
# The main function demonstrating the usage of various features.
def main():
    # Generate and save passwords
    passwords = [PasswordGenerator(12, 2, 2, 2).generate_password() for _ in range(20)]
    save_passwords_to_csv(passwords, 'passwords.csv')

    # Read and filter passwords
    read_and_filter_passwords('passwords.csv')

    # List and dictionary operations
    list_and_dict_operations()

    # Tuple operations
    a, b, c = tuple_operations()
    print(f"Tuple values: {a}, {b}, {c}")


if __name__ == "__main__":
    main()


