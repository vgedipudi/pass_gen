# pass_gen
password generator
Project Overview: Password Generation and Security Check

# Introduction #
The project comprises two primary Python scripts: pass_gen.py and check_password_pwned.py. 
It demonstrates a range of programming concepts and techniques, from generating random passwords 
and handling data with Pandas to web scraping and interacting with an API for security checks. 
The project provides a practical application of Python in the realm of data manipulation and cyber security, 
showcasing how scripts can be integrated to form a comprehensive workflow.

# Objectives #

    * Password Generation *: Create a set of random passwords with specified criteria for length 
    and character composition.

    * Data Manipulation *: Employ Pandas for reading, filtering, and writing data.

    * Security Verification *: Check the generated passwords against the "Have I Been Pwned" API to 
    determine if they have been compromised in known data breaches.

    * Web Scraping *: Extract data from a simple webpage to demonstrate scraping techniques.

    * File Operations *: Read from and write to files for data persistence and result presentation.

# Tools and Libraries Used #

    * Python *: The primary programming language used for the project.
    
    * Pandas *: A powerful Python library for data manipulation and analysis, particularly for working 
    with structured data like CSV files.
    
    * Requests *: A Python HTTP library used to make requests to external URLs, crucial for both the web 
    scraping and API interaction aspects of the project.
    
    * BeautifulSoup *: A library for parsing HTML and XML documents, used here for web scraping.
    
    * hashlib *: A Python module providing a secure way to hash passwords.
    
    * Standard Python Libraries *: Such as random for generating random elements and string for accessing standard string character sets.

# Project Execution #

* pass_gen.py *:

Generates a set of random passwords based on predefined criteria (length, number of uppercase letters, symbols, and digits).
Saves these passwords into passwords.csv.
Reads and filters this CSV file to get a subset of passwords.
Performs various list, dictionary, and tuple operations to demonstrate Python's data structure manipulation capabilities.

* check_password_pwned.py *:

Reads the generated passwords from passwords.csv.
Checks each password against the "Have I Been Pwned" API to determine if it has been exposed in a data breach.
Saves the results of this check to pwned_results.txt.
Demonstrates basic web scraping by extracting content from a simple webpage (example.com) and saving it to scraped_content.txt.
This project serves as an educational tool for understanding various Python functionalities and their practical applications, especially in the areas of cybersecurity and data handling.
