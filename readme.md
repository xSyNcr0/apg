# APG v1.0 - Advanced Password Generator

## Overview

APG (Advanced Password Generator) is a robust and flexible password generation tool designed to create strong, customizable passwords based on user input. It offers various levels of obfuscation and customization to ensure generated passwords meet specific security requirements.

## Features

- Generates passwords with customizable length and character composition
- Supports inclusion of words, numbers, dates, and special characters
- Multiple levels of password strength and obfuscation
- Handles special cases such as padded numbers and "plus one" sequences
- Outputs generated passwords to a file

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/APG.git
    cd APG
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main script to start the password generator:

```sh
python main.py
```

You will be prompted to input various parameters such as words, numbers, dates, special characters, and password configuration options.
Example Inputs

    Words: word1, word2, word3
    Numbers: 123, 456, 789
    Dates: 2023-01-01, 2024-12-31
    Special Characters: @, &, !
    Password Length: 8, 14
    Number of Digits: 1, 2
    Number of Special Characters: 0, 2
    Number of Uppercase Letters: 0, 2
    Password Strength Level: 1 to 5
    Plus One: 0 (no effect) or 1 (enable)
    Padded Numbers: 2
    Obfuscation Level: 0 (no effect) to 3
    Obfuscation Iterations: 1 to 99
    Year Range: 2016, 2021

Example Output

Generated passwords will be saved in wordlist.txt file in the current directory.
Disclaimer

The developer assumes no liability and is not responsible for any issues or damages caused by using APG. Use at your own risk.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Author

Created by xSyNcr0


Feel free to adjust the content and formatting to better match your preferences or project specifics.
