# Password Cracker and Estimator

This Python script is a simple brute-force password cracker that:
1. Estimates the time it will take to crack a given password based on the complexity of the password and the allowed character set.
2. Brute-forces the password, measuring the actual time taken to crack it.
3. Reports detailed statistics, including:
   - Total combinations to test.
   - Number of combinations tested.
   - Time taken to crack the password.
   - Average operations (attempts) per second.

## Features

- **Estimation**: Calculates the number of combinations to test and an estimated cracking time assuming 1,000,000 attempts per second.
- **Brute-force Cracking**: Iterates through all possible combinations of characters to find the password.
- **Detailed Statistics**:
  - Total combinations tested.
  - Time taken for the cracking process.
  - Average attempts per second during the cracking process.

## Requirements

- Python 3.7 or later.

No additional libraries are required as the script uses only standard Python modules.

## Usage

1. Clone this repository or download the script file.
2. Run the script with Python:
   ```bash
   python password_cracker.py
   ```
3. Enter the password you want to test when prompted.

### Example Run

```plaintext
Enter the password to test: abc

Estimating cracking time...
Total combinations to test: 238328
Estimated time to crack (assuming 1M attempts/sec): 0.24 seconds

Starting brute-force cracking...

Password cracked: abc
Time taken to crack: 0.13 seconds
Total combinations tested: 238329
Average operations per second: 1808574.13
```

## Code Details

### Allowed Characters
The set of allowed characters is hardcoded in the script:
```python
allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?/|"
```

### Functions

#### `password_crack_estimator(password, allowed_chars)`
Calculates the total number of combinations and estimates the cracking time based on the allowed characters and password length.

#### `brute_force_crack(password, allowed_chars)`
Attempts to brute-force the password by generating combinations of the allowed characters.

## Notes

- The script is for educational purposes only. Do not use it for unauthorized or malicious activities.
- The cracking time depends on the length and complexity of the password. Longer and more complex passwords take significantly more time to crack.
- The script assumes a cracking speed of 1,000,000 attempts per second for estimation purposes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
```

This `README.md` provides an overview of the project, including its purpose, features, requirements, usage, and important notes.
