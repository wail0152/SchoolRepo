def shift(ch, n):
    return "{0:b}".format(ord(ch) >> n) if n > 0 else "{0:b}".format(ord(ch) << abs(n))
