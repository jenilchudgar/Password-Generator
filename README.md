# Password Generator

This is a password generator application built using Tkinter and Python. It generates strong and secure passwords based on user-selected options such as password length and difficulty level.

## Features

- Allows the user to select the length of the password.
- Provides options to choose the difficulty level: easy, medium, or hard.
- Supports customization by allowing the user to select different character types for the password generation, including lowercase letters, uppercase letters, numbers, and special characters.
- Generates unique and random passwords every time.
- Copies the generated password to the clipboard for easy use.

## Prerequisites

- Python (version 3.6 or above) must be installed on your system.
- The following Python libraries need to be installed:
  - Tkinter
  - Pillow
  - Pyperclip
  - Random

## Installation

1. Clone the repository:

```
git clone https://github.com/Jenil-Chudgar/password-generator.git
```

2. Change into the project directory:

```
cd password-generator
```

3. Install the required libraries:

```
pip install -r requirements.txt
```

## Usage

1. Run the `main.py` file:

```
python main.py
```

2. The application window will appear, showing options for password length, difficulty level, and character types.

3. Select the desired options and click on the "Generate Password" button.

4. If you want to copy the generated password, click on the "Copy" button.

5. You can generate multiple passwords by changing the options and clicking the "Generate Password" button again.

## Screenshots

![Password Generator](screenshot.png)

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
