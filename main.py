import itertools
import time

def password_crack_estimator(password, allowed_chars):
    """
    Estimates the time required to crack the password based on brute-force attempts.
    """
    total_combinations = sum(len(allowed_chars)**i for i in range(1, len(password) + 1))
    attempts_per_second = 1_000_000  # Assumed number of attempts per second for estimation
    estimated_time_seconds = total_combinations / attempts_per_second
    return total_combinations, estimated_time_seconds

def brute_force_crack(password, allowed_chars):
    """
    Cracks the password using brute-force and measures the actual time taken.
    """
    start_time = time.time()
    total_attempts = 0
    for length in range(1, len(password) + 1):
        for attempt in itertools.product(allowed_chars, repeat=length):
            total_attempts += 1
            attempt = ''.join(attempt)
            if attempt == password:
                end_time = time.time()
                time_taken = end_time - start_time
                operations_per_second = total_attempts / time_taken
                return attempt, time_taken, total_attempts, operations_per_second
    return None, None, None, None  # Should never reach here if password is valid

if __name__ == "__main__":
    # Hardcoded allowed characters
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?/|"

    # Get input from user
    password = input("Enter the password to test: ")

    print("\nEstimating cracking time...")
    total_combinations, estimated_time = password_crack_estimator(password, allowed_chars)
    print(f"Total combinations to test: {total_combinations}")
    print(f"Estimated time to crack (assuming 1M attempts/sec): {estimated_time:.2f} seconds")

    print("\nStarting brute-force cracking...")
    cracked_password, actual_time, total_attempts, operations_per_second = brute_force_crack(password, allowed_chars)
    if cracked_password:
        print(f"\nPassword cracked: {cracked_password}")
        print(f"Time taken to crack: {actual_time:.2f} seconds")
        print(f"Total combinations tested: {total_attempts}")
        print(f"Average operations per second: {operations_per_second:.2f}")
    else:
        print("Failed to crack the password.")
