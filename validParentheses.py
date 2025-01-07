def validParentheses(s):
    # couple = {
    #     '}': '{',
    #     ')': '(',
    #     ']': '[',
    #     '{': '}',
    #     '(': ')',
    #     '[': ']'
    # }

    # reverse = s[::-1]
    # print(s)
    # print(reverse)
    # if len(s) % 2 != 0:
    #     return False
    # else:
    #     for i in s:
    #         for j in reverse:
    #             # print(s.find(i))
    #             # print(s.find(couple[i]))
    #             # print(s.find(j) + s.find(couple[i]) % 2 != 0)
    #             if s.find(i) + s.find(couple[i]) % 2 != 0 and (s.find(i) != -1 and s.find(couple[i]) != -1):
    #                 return True
    #             elif i != couple[j]:
    #                 return False
    #             return True
    a = []
    for i in s:
        if i in '{([':
            a.append(i)
        else:
            # if not a or (i == ')' and a[-1] != '(') or (i == ']' and a[-1] != '[') or (i == '}' and a[-1] != '{'):
            if not a or (i == ')' and a[-1] != '(') or (i == ']' and a[-1] != '[') or (i == '}' and a[-1] != '{'):
                return False
            a.pop()
        
    return len(a) == 0
        
    
    
a = validParentheses('([{})')
# a = validParentheses('([)]')
print(a)