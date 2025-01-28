def is_palindrome(num):
    str_szam = str(num)
    return str_szam == str_szam[::-1]


print(is_palindrome(121))