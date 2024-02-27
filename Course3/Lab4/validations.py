#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Memeriksa apakah username yang diterima memenuhi syarat yang dibutuhkan."""
    if type(username) != str:
        raise TypeError("username harus berupa string")
    if minlen < 1:
        raise ValueError("minlen harus setidaknya 1")

    # Username tidak boleh lebih pendek dari minlen
    if len(username) < minlen:
        return False
    # Username hanya boleh menggunakan huruf, angka, titik, dan garis bawah
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Username tidak boleh diawali dengan angka
    if username[0].isdigit():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
