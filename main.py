import tkinter as tk
import string

# Create the main application window.
window = tk.Tk()
window.title('Password Strength Checker')
window.geometry('400x300')

# Check the strength of the entered password.
def check_password():
    password = password_entry.get()

    length_ok = len(password) >= 12
    uppercase_ok = any(character.isupper() for character in password)
    lowercase_ok = any(character.islower() for character in password)
    number_ok = any(character.isdigit() for character in password)
    special_ok = any(character in string.punctuation for character in password)

    # Calculate the password strength score.
    score = sum([
        length_ok,
        uppercase_ok,
        lowercase_ok,
        number_ok,
        special_ok
    ])

    # Determine the password strength.
    if score <= 1:
        strength = 'Weak'
    elif score <= 3:
        strength = 'Moderate'
    else:
        strength = 'Strong'

    # Display the password strength.
    result_label.config(text=f'Your password strength is {strength}')


# Create a label for the password field.
password_label = tk.Label(window, text='Enter a password: ')
password_label.pack(pady=5)

# Create the password input field.
password_entry = tk.Entry(window, show='*')
password_entry.pack(pady=5)

# Create a label to display the password strength.
result_label = tk.Label(window, text='Password strength will appear here')
result_label.pack(pady=5)

# Create a button to check the password.
check_button = tk.Button(window, text='Check Password', command=check_password)
check_button.pack(pady=5)

# Start the application.
window.mainloop()