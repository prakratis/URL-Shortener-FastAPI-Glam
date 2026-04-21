import string

# This is our library of characters
ALPHABET = string.digits + string.ascii_lowercase + string.ascii_uppercase

def encode_base62(num: int) -> str:
    """
    Converts a database ID (integer) into a Base62 string.
    Example: 100 -> '1C'
    """
    if num == 0:
        return ALPHABET[0]
    
    arr = []
    base = len(ALPHABET)
    while num:
        num, rem = divmod(num, base)
        arr.append(ALPHABET[rem])
    
    # We reverse it because the math generates the digits backwards
    arr.reverse()
    return ''.join(arr)