"""
Functions to work with names
"""

import re


REPLACE_REGEX = re.compile(r"([^\w]|\s)")
SUB_CHAR = '-'

def display_name_to_kube_name(display_name: str) -> str:
    """Converts human readable display name to kubernetes name"""
    return REPLACE_REGEX.sub(SUB_CHAR, display_name.strip().lower())

def add_kube_name_prefix(kube_name: str, prefix: str) -> str:
    """Adds prefix to kubernetes name"""
    return prefix + SUB_CHAR + kube_name
