#!/usr/bin/env python3
""" auth file """

import bcrypt


def _hash_password(password: str) -> bytes:
    """ takes in password string and
    returns salted hash password in bytes
    """
    password_bytes = password.encode('utf-8')
    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')
