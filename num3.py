
#/***************************************************************************************
#*    Title: <StackOverflow source code>
#*    Author: <Stefan Pochmann>
#*    Date: <Sep 25, 2017>
#*    Code version: <Python 3.7.4>
#*    Availability: <https://stackoverflow.com/a/46406563>
#*
#***************************************************************************************/

def StrToInt(num):
    result = 0
    for digit in num:
        result *= 10
        for d in '0123456789':
            result += digit > d
    return result

#/***************************************************************************************
#*    Title: <StackOverflow source code>
#*    Author: <Amardip Kumar>
#*    Date: <Aug 28, 2018>
#*    Code version: <Python 3.7.4>
#*    Availability: <https://stackoverflow.com/a/52061649>
#*
#***************************************************************************************/

def IntToStr(num):
    is_negative = False
    if num:
        num, is_negative = num, True
    s = []
    while True:
        s.append(chr(ord('0') + num % 10))
        num //= 10
        if num == 0:
            break
    return "".join(reversed(s))


def product(num1, num2):
    a = StrToInt(num1)
    b = StrToInt(num2)
    product = a * b
    final = IntToStr(product)
    return final

