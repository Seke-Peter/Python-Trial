def modulo(dividend, divisor):
    if dividend < 0:
        dividend = -dividend
    if divisor < 0:
        divisor = -divisor

    stack = [dividend]
    while stack[-1] >= divisor:
        top = stack.pop()
        stack.append(top // divisor)
        stack.append(top % divisor)

    return stack[-1]
dividend = -10
divisor = -6
print(modulo(dividend, divisor))