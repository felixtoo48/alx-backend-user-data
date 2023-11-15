#!/usr/bin/env python3
""" auth file """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """ takes in password string and
    returns salted hash password in bytes
    """
    password_bytes = password.encode('utf-8')
    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_bytes


def _generate_uuid() -> str:
    """ function to generate uuid """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ function for registering user after authentication """
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user is not None:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:

            hashed_password = _hash_password(password)

            # create a new user with the hashed password
            user = User(email=email, hashed_password=hashed_password)

            # Add the user to the database
            self._db.add_user(email=email, hashed_password=hashed_password)

            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ validating login, by checking if the user exists, if so
        check password, if it matches return true
        """
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user and bcrypt.checkpw(password.encode('utf-8'),
                                                existing_user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False
