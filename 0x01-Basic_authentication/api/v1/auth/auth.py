#!/usr/bin/env python3
""" managing API Authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ class for managing API Authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ defining require authentication """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths or path + "/" in excluded_paths:
            return False

        for e_path in excluded_paths:
            if e_path.endswith('*'):
                if path.startswith(i[:1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header template """
        if request is None:
            return None

        # If the request doesn't contain the header key 'Authorization',
        # return None
        if 'Authorization' not in request.headers:
            return None

        # Return the value of the 'Authorization' header in the request
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user authorization template """
        return None
