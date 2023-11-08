#!/usr/bin/env python3
""" managing API Authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ class for managing API Authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ defining require authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization header template """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user authorization template """
        return None
