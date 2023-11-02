#!/usr/bin/env python3
""" function that returns a log message that is unclear/obscured """
import re

def filter_datum(fields, redaction, message, separator):
    """ function returning a hidden log message"""
    regex_pattern = r'{}(?={})'.format('|'.join(re.escape(field)
        for field in fields), re.escape(separator))
    return re.sub(regex_pattern, redaction, message)

