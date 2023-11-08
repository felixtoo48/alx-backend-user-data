#!/usr/bin/env python3
""" managing API Authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ class for managing API Authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ defining require authentication """
        if path is None:
            return True
        if not excluded_paths:
            return True
        for excluded_paths in excluded_paths:
            # Check if path or path with a trailing slash is in excluded_path
            if path == excluded_path or path == excluded_path + '/':
                return False
        # If the path is not in the list of excluded paths, return True
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header template """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user authorization template """
        return None
