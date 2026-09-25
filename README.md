# Password Strength Checker

A small Python application that checks the strength of a password based on common password requirements.

## Features

- Checks password length
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for numbers
- Checks for special characters
- Calculates a password strength score
- Displays a Weak, Moderate, or Strong result
- Uses a simple Tkinter graphical interface
- Hides the password while it is being entered

## How It Works

The application checks five password requirements:

1. At least 12 characters
2. Contains an uppercase letter
3. Contains a lowercase letter
4. Contains a number
5. Contains a special character

Each requirement that is met adds one point to the password's strength score.

- 0-1 points: Weak
- 2-3 points: Moderate
- 4-5 points: Strong

## Technologies

- Python
- Tkinter

## How to Run

Run `main.py` with Python:

```bash
python main.py