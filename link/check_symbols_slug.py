def check_symbols(slug):
    allowed_symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~"
    coincidence = all(False for symbol in slug if symbol not in allowed_symbols)
    return coincidence