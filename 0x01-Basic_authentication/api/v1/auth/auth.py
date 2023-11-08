#!/usr/bin/env python3
""" managing API Authentication """
from flask import request

class Auth():
    """ class for managing API Authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ defining require authentication"""
    def authorization_header(self, request=None) -> str:
        """ """
        return
    def current_user(self, request=None) -> TypeVar('User'):
        """ """
        return
