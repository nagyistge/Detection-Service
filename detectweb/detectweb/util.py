from __future__ import absolute_import

from hashlib import md5

def get_md5_hex(f):
    """
    Get md5 hex digest of a file.
    TODO: read in chunk to avoid big files.
    """
    if type(f) == str:
        f = open(f, 'r')

    f.seek(0)
    md5_hash = md5(f.read()).hexdigest()
    f.seek(0)
    return md5_hash
