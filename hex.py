def if_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

print(if_hex('abcde1234968498498464654A'))