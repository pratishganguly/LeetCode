def longestValidParentheses(s: str) -> int:
    stack = [-1]
    s_len = len(s)
    max_length = 0
    for i in range(0,s_len):
        if s[i]==')':
            stack.pop()
            if stack:
                max_length = max(i - stack[-1], max_length)
            else:
                stack.append(i)
        else:
            stack.append(i)
    return max_length
  
 if _name__ == '__main_':
    print(longestValidParentheses(''))
    print(longestValidParentheses('()'))
    print(longestValidParentheses(')()'))
    print(longestValidParentheses('(())'))
    print(longestValidParentheses('(()()()())'))
    print(longestValidParentheses('))(()()()())'))
    print(longestValidParentheses('(()()()())(('))
    print(longestValidParentheses('(((((())'))
    print(longestValidParentheses('(())))))'))
    print(longestValidParentheses('))))))))(())'))
    print(longestValidParentheses('(())(((((((('))
