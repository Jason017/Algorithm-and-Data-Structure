# https://www.geeksforgeeks.org/balance-a-string-after-removing-extra-brackets/


def balancedString(str):
    count = 0
    res = ""

    for i in range(len(str)):
        if str[i] == '(':
            res += str[i]
            count += 1
        elif str[i] == ')' and count != 0:
            res += str[i]
            count -= 1
        elif str[i] != ')':
            res += str[i]

    if (count != 0):
        for i in range(count):
            res += ")"
    return res


print(balancedString("gau)ra)v(ku(mar(rajput))"))
