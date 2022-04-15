"""
This module was made out of necessity for generating one time HMAC
based TOTP (Time based OTP) password using HMAC-SHA algorithm.
Following SHA algorithms are supported: SHA1, SHA224, SHA256,
SHA384, SHA512.

https://tools.ietf.org/html/rfc6238
https://docs.python.org/3/library/hashlib.html


version:1.0.0
author: Aniket Hande
license: MIT
"""

import hmac
import base64
import struct
import hashlib
import time
import array
import math

MULTIPLIER = 8

def _generate(secret_, intervals_no_, sha_, digits_):
    s = _add_required_padding(secret_)
    key = base64.b32decode(s, True)
    msg = struct.pack(">Q", intervals_no_)
    h = hmac.new(key, msg, digestmod=sha_).hexdigest()
    return _truncate(h)[-digits_:]

def _truncate(hmac_sha_):
    """
    truncate SHA value.
    """
    offset = int(hmac_sha_[-1], 16)
    binary = int(hmac_sha_[(offset *2):((offset*2)+8)], 16) & 0x7FFFFFFF
    return str(binary)

def _add_required_padding(key_):
    """
    Add padding '=='.
    """
    if len(key_) % MULTIPLIER:
        key_ += '=' * (MULTIPLIER - len(key_) % MULTIPLIER)
    return key_

def _get_sha(sha_):
    """
    Set HASH algorithm to use.
    """
    hashlib_ = {
        1: hashlib.sha1,
        224: hashlib.sha224,
        256: hashlib.sha256,
        384: hashlib.sha384,
        512: hashlib.sha512,
    }
    return hashlib_.get(sha_, hashlib.sha1)


def get_totp(secret_, interval_=30, sha_=1, digits_=6, c_time_=time.time()):
    """
    Get time based OTP using given secret and time.
    secret: base32 encoded string.
    interval: TOTP interval length.
    sha_: hashlib digest method.
    digits: output token length.
    c_time: current time.
    """
    encoded_secret = base64.b32encode(secret_)
    interval = int(math.floor(c_time_))//interval_
    sha = _get_sha(sha_)
    return _generate(encoded_secret, interval, sha, digits_)

__all__ = ['get_totp']

# End.
