# Random Password Generator and Login System

## Overview

This project is a basic implementation of a user authentication system. It prompts the user to enter a username, generates a random password upon request, and then allows the user to log in with the provided credentials. The password is a randomly selected combination of alphabets (both lowercase and uppercase) and numbers.

## Why it's Useful

This project is a helpful starting point for beginners who want to understand basic user authentication mechanisms and random password generation in Python. It can be used as a simple template for creating more complex authentication systems or integrated into larger projects requiring user identification.

## Getting Started

### Prerequisites

- Python installed on your machine.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/BrandonBlkk/User-Login.git
    ```

2. Navigate to the project directory:

    ```bash
    cd User-Login
    ```

### Usage

1. Run the script:

    ```bash
    python UserLogin.py
    ```

2. Enter your username when prompted. Ensure it includes alphabets; otherwise, you will be prompted to enter it again.

3. Decide whether you want to generate a password by typing "yes" or "no" when prompted.

4. If you chose to generate a password, the system will display your generated username and password.

5. You will have three attempts to log in. Enter your username and the generated password when prompted.

6. If the login is successful, you'll see a "Successfully Login!" message; otherwise, you'll receive an "Invalid Login!" message.

### Example

```bash
Enter your username: user123
Do you want to generate a password? yes
Username: user123 : Password: 5ArMv
Enter your username to login: user123
Enter your password to login: 5ArMv
Successfully Login!
```

Feel free to modify and expand upon this code according to your project requirements.
