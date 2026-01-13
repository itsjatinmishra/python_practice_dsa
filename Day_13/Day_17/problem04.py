#Explain me this code: 
expr_input = input("Enter the expression please: ")
expr = []

for item in expr_input:
    expr.append(item)

stack = []

for i in range(len(expr)):
    print(i)
    if expr[i] in ['{', '(', '[']:
        stack.append(expr[i])

    elif expr[i] in ['}', ')', ']']:
        if len(stack) == 0:
            stack.append("error")
            break

        top = stack.pop()

        if (top == '(' and expr[i] != ')') or \
           (top == '[' and expr[i] != ']') or \
           (top == '{' and expr[i] != '}'):
            stack.append("error")
            break

if stack:
    print("Unbalanced")
else:
    print("Balanced")