def solution(s):
    stack = []
    for c in s:
        
        if len(stack) ==0:
            stack.append(c)
            continue

        if stack[-1] == c:
            stack.pop()

        else :
            stack.append(c)

    print(stack)
    if len(stack) ==0:
        return 1
    
    else :
        return 0

# 삭제 시 다시 0부터 돌리고 삭제


solution(s= "baabaa");