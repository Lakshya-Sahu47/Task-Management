"""Authentication and account business logic."""

from __future__ import annotations

from typing import Optional

from werkzeug.security import check_password_hash, generate_password_hash

from task_management.extensions import db
from task_management.models.user import User
from task_management.services import log_activity


class AuthError(Exception):
    """Raised for any authentication/registration business-rule violation."""


def register_user(
    *, username: str, email: str, password: str, role: str = "employee"
) -> User:
    """Create a new user account with a securely hashed password.

    Raises AuthError if the username or email is already taken.
    """
    if User.query.filter_by(username=username).first() is not None:
        raise AuthError(f"Username '{username}' is already taken.")
    if User.query.filter_by(email=email).first() is not None:
        raise AuthError(f"Email '{email}' is already registered.")

    user = User(
        username=username,
        email=email,
        password_hash=generate_password_hash(password),
        role=role,
    )
    db.session.add(user)
    db.session.flush()  # populate user.id for the log entry below

    log_activity(user_id=user.id, action="user_registered", target_type="User", target_id=user.id)
    db.session.commit()
    return user


def authenticate_user(*, username: str, password: str) -> User:
    """Verify credentials and return the matching user.

    Raises AuthError if the username doesn't exist or the password is wrong.
    Deliberately uses the same error message for both cases to avoid
    leaking which usernames exist.
    """
    user = User.query.filter_by(username=username).first()
    if user is None or not check_password_hash(user.password_hash, password):
        raise AuthError("Invalid username or password.")

    log_activity(user_id=user.id, action="user_login")
    db.session.commit()
    return user


def change_password(*, user_id: int, current_password: str, new_password: str) -> User:
    """Change a user's password after verifying their current one."""
    user = get_user_by_id(user_id)
    if not check_password_hash(user.password_hash, current_password):
        raise AuthError("Current password is incorrect.")

    user.password_hash = generate_password_hash(new_password)
    log_activity(user_id=user.id, action="password_changed", target_type="User", target_id=user.id)
    db.session.commit()
    return user


def get_user_by_id(user_id: int) -> User:
    """Fetch a user by primary key, raising AuthError if not found."""
    user: Optional[User] = User.query.get(user_id)
    if user is None:
        raise AuthError(f"No user found with id={user_id}.")
    return user
