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
        if excluded_paths is None:
            return True
        for excluded_path in excluded_paths:
            if path == excluded_path or path == excluded_path + '/':
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header template """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user authorization template """
        return None
