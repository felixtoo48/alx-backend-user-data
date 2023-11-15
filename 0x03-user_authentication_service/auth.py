#!/usr/bin/env python3
""" auth file """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """ takes in password string and
    returns salted hash password in bytes
    """
    password_bytes = password.encode('utf-8')
    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ function for registering user after authentication """
        existing_user = self._db.find_user_by(email=email)
        if existing_user is not None:
            raise ValueError("User {self.email} already exists")

        hashed_password = _hash_password(password)

        # create a new user with the hashed password
        user = User(email=email, hashed_password=hashed_password)

        # Add the user to the database
        self._db.add_user(email=email, hashed_password=hashed_password)

        return user
