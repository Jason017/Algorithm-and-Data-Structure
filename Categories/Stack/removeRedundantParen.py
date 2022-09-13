def removeRedundantParantheses(s):
    stack = []
    res = ""

    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                continue
            tempStack = []
            while stack and len(stack[-1]) > 0:
                top = stack.pop()
                if stack and stack[-1] == "(":
                    stack.append(stack.pop() + top + c)
                else:
                    stack.append(top)
        else:
            if stack:
                if stack[-1] == "(":
                    stack.append(c)
                else:
                    stack.append(stack.pop()+c)
        print(stack)

    return res


# s = "(((a)))"
# removeRedundantParantheses(s)  # "(a)"

s = "((ab)(bc))d"
removeRedundantParantheses(s)  # "(ab)(bc)d"

# s = "()"
# removeRedundantParantheses(s)  # ""

# s = "((a)(bcd)(e))"
# removeRedundantParantheses(s)  # "(a)(bcd)(e)"
