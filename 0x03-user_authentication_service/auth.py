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

    def create_session(self, email: str) -> str:
        """Create a session for the user and return the session ID."""
        try:
            existing_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            session_id = _generate_uuid()
            self._db.update_user(existing_user.id, session_id=session_id)
            return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """ method finding user using session id """
        try:
            if session_id:
                existing_user = self._db.find_user_by(session_id=session_id)
                return existing_user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroy session by updating corresponding user id to None
        """
        if user_id:
            existing_user = self._db.find_user_by(id=user_id)
            self._db.update_user(existing_user.id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ generate and reset user's password token """
        try:
            existing_user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(existing_user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError
