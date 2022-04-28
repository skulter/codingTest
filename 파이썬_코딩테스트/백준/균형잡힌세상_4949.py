# import sys

# while 1:
#     array = []
#     word = sys.stdin.readline().rstrip()
#     if word == '.':
#         break
#     for i in word:
#         if i == '(' or i == '[':
#             array.append(i)
#         if (i == ')' or i == ']') and len(array) >= 1:
#             char = array.pop()
#             if char == '(' and i == ')':
#                 continue
#             elif char == '[' and i == ']':
#                 continue
#             else:
#                 array.append(char)
#     if len(array) >= 1:
#         print('no')
#     else:
#         print('yes')
while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')