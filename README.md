# Secure Password Generator

This is a Python script I wrote to generate cryptographically strong, random passwords that meet a given set of constraints. It uses Python's `secrets` module to ensure the generated passwords are suitable for security-sensitive applications.



## Skills Demonstrated

This project was a practical exercise in using Python's standard library and regular expressions to build a useful program. My learning focused on:

- **Importing Modules:** Gaining experience with importing and using powerful modules from Python's standard library, including `secrets` for cryptographic security, `string` for common character sets, and `re` for pattern matching.

- **Regular Expressions (Regex):** Learning to define and use regex patterns to solve a practical problem. This included building dynamic patterns and using `re.findall()` to validate that the generated password met a series of character-type constraints.

## Features

- Generates cryptographically strong random passwords using the `secrets` module.
- Allows customization of password length.
- Enforces constraints for the minimum number of digits, special characters, uppercase, and lowercase letters.
- Includes a guard clause to raise a `ValueError` for impossible constraints.

## Requirements

This script uses only Python's standard library, so no external packages are needed. All you need is **Python 3.x** installed.

## Usage

To run the script with the built-in example, save the code as `password_generator.py` and execute it from your terminal:

```sh
python password_generator.py
```

This will run the `main()` function and produce a new, random 16-character password that meets the default constraints.

**Example Output:**
```
Generated password: n@8KjP!w_s3G*z7L
```

## Code Overview

- **`generate_password`**: The core function that contains all the logic for validation, generation, and constraint checking.
- **`main`**: A simple execution block that calls the function with default parameters and prints a new password.

## Technologies Used

- **Language:** Python 3
- **Modules:** `secrets`, `re`, `string`
- **Key Concepts:** Cryptographic Randomness, Regular Expressions, Generator Expressions, Guard Clauses
