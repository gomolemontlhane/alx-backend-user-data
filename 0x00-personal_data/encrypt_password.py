#!/usr/bin/env python3
"""
A module for encrypting passwords using bcrypt.
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """Generate a hashed password using bcrypt."""
    # Convert the password string to bytes
    password_bytes = password.encode('utf-8')
    # Generate the salt and hash the password
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the provided password matches the hashed password."""
    # Convert the password string to bytes
    password_bytes = password.encode('utf-8')
    # Compare the hashed password with the provided password
    return bcrypt.checkpw(password_bytes, hashed_password)

if __name__ == "__main__":
    # Example usage
    password = "my_secure_password"
    hashed = hash_password(password)
    print(f"Hashed password: {hashed}")

    # Check if the password is valid
    if is_valid(hashed, password):
        print("Password is valid!")
    else:
        print("Invalid password.")
