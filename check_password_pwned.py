# check_password_pwned.py
# This script checks if passwords have been exposed in data breaches using the "Have I Been Pwned" API.
# It also demonstrates web scraping and file operations.
# 8.1, 8.2, 8.3, 8.4
import requests
import hashlib
import pandas as pd
from bs4 import BeautifulSoup
from pass_gen import PasswordGenerator  # 3.17: Importing module from pass_gen.py


# Function to check if a password has been pwned
# utilizes 7.1 - 7.5
def check_password_pwned(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars, tail = sha1password[:5], sha1password[5:]
    response = requests.get('https://api.pwnedpasswords.com/range/' + first5_chars)
    # 7.1 - check_password_pwned fxn splits response from API into individual
    # lines using the .splitlines() method on the response text.
    hashes = (line.split(':') for line in response.text.splitlines())
    return any(tail in line for line in hashes)


# 10.1, 10.2, 10.3: Web scraping example
def scrape_example_website():
    url = "http://example.com"  # Placeholder for a non-sensitive, simple webpage
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}  # 10.3: Polite web scraping
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        # Example: Scrape the main heading
        main_heading = soup.find('h1').get_text()
        return main_heading
    except requests.RequestException as e:
        print(f"Error scraping website: {e}")
        return None


# 3.20, 3.21: Write and append results to a file
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content + '\n')


def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\n')


# Main function to demonstrate the usage of the script
def main():
    # Read passwords from CSV
    df = pd.read_csv('passwords.csv')

    # Check each password using the API
    for password in df['Password']:
        is_pwned = check_password_pwned(password)
        result = f"Password '{password}' has been pwned: {is_pwned}"
        append_to_file('pwned_results.txt', result)

    # Web scraping example
    main_heading = scrape_example_website()
    if main_heading:
        write_to_file('scraped_content.txt', main_heading)

# Ensures script only runs main function when directly executed (e.g., python check_password_pwned.py), 
# not when imported as a module.
if __name__ == "__main__":
    main()
