#!/usr/bin/env python3
"""
Testing module for Flask app endpoints
"""

import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Registers a new user."""
    response = requests.post(
        f"{BASE_URL}/users",
        data={
            "email": email,
            "password": password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempts to log in with the wrong password."""
    response = requests.post(
        f"{BASE_URL}/login",
        data={
            "email": email,
            "password": password})
    # Assuming the login endpoint returns 401 for incorrect credentials
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Logs in and returns the session ID."""
    response = requests.post(
        f"{BASE_URL}/login",
        data={
            "email": email,
            "password": password})
    assert response.status_code == 200
    return response.json().get("session_id")


def profile_unlogged() -> None:
    """Attempts to access the profile without logging in."""
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403
    # Assuming the profile endpoint requires login


def profile_logged(session_id: str) -> None:
    """Attempts to access the profile while logged in."""
    response = requests.get(
        f"{BASE_URL}/profile",
        cookies={
            "session_id": session_id})
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """Logs out and invalidates the session."""
    response = requests.post(
        f"{BASE_URL}/logout",
        cookies={
            "session_id": session_id})
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """Requests a password reset token."""
    response = requests.post(
        f"{BASE_URL}/reset_password",
        data={
            "email": email})
    assert response.status_code == 200
    return response.json().get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Updates the password with a reset token."""
    response = requests.post(
        f"{BASE_URL}/update_password",
        data={
            "email": email,
            "reset_token": reset_token,
            "new_password": new_password})
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
