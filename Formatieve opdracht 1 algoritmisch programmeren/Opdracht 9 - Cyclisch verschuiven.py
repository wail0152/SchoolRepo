def shift(ch, n):
    return f"{ord(ch) >> n:b}" if n > 0 else f"{ord(ch) << abs(n):b}"
