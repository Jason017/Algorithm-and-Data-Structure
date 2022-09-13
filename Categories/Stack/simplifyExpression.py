def simplify(string):
    n = len(string)

    # resultant stringing of max length equal to length of input string
    res = [None] * n
    index = 0
    i = 0

    s = []
    s.append(0)

    while (i < n):
        if (string[i] == '(' and i == 0):
            i += 1
            continue

        if (string[i] == '+'):
            # If top is 1, flip the operator
            if (s[-1] == 1):
                res[index] = '-'
                index += 1
            # If top is 0, append the same operator
            if (s[-1] == 0):
                res[index] = '+'
                index += 1
        elif (string[i] == '-'):
            if (s[-1] == 1):
                res[index] = '+'
                index += 1
            elif (s[-1] == 0):
                res[index] = '-'
                index += 1
        elif (string[i] == '(' and i > 0):
            if (string[i - 1] == '-'):
                # x is opposite to the top of stack
                x = 0 if (s[-1] == 1) else 1
                s.append(x)
            # append value equal to top of the stack
            elif (string[i - 1] == '+'):
                s.append(s[-1])

        # If closing parentheses pop
        # the stack once
        elif (string[i] == ')'):
            s.pop()
        # copy the character to the result
        else:
            res[index] = string[i]
            index += 1
        i += 1
    return "".join([r for r in res if r])


s1 = "(a-(b+c)+d)"
s2 = "a-(b-c-(d+e))-f"
print(simplify(s1))
print(simplify(s2))
