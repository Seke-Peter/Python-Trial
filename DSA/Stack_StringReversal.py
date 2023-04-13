
def reverse_string(name):
    stack = []
    for char in name:
        stack.append(char)
    name = ""
    while len(stack) > 0:
        name += stack.pop()
    return name
name = "florence"
print(reverse_string(name))

