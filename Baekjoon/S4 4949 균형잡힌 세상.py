while True:
    stack = []
    temp = True
    str = input()
    
    if str == ".":
        break
    
    for i in str:
        if i == "(" or i == "[":
            stack.append(i)
        
        elif i == ")":
            if not stack or stack[-1] == "[":
                temp = False
                break
            elif stack[-1] == "(":
                stack.pop()
        
        elif i == "]":
            if not stack or stack[-1] == "(":
                temp = False
                break
            elif stack[-1] == "[":
                stack.pop()
    
    if temp == True and not stack:
        print("yes")
    else:
        print("no")
