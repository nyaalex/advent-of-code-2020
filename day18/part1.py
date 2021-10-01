def conv_line(line):
    output_queue = []
    op_stack = []
    for token in line:
        if token == ' ':
            continue
        elif token == '*' or token == '+':
            while op_stack and op_stack[-1] != '(':
                output_queue.append(op_stack.pop())
            op_stack.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            while op_stack[-1] != '(':
                output_queue.append(op_stack.pop())
            op_stack.pop()
        else:
            output_queue.append(int(token))
    output_queue += op_stack[::-1]
    return output_queue


def run_rpn(rpn):
    var_stack = []
    for token in rpn:
        if token == '+':
            a = var_stack.pop()
            b = var_stack.pop()
            var_stack.append(a + b)
        elif token == '*':
            a = var_stack.pop()
            b = var_stack.pop()
            var_stack.append(a * b)
        else:
            var_stack.append(token)
    return var_stack[0]


if __name__ == '__main__':
    total = 0

    for line in open('input'):
        total += run_rpn(conv_line(line.strip()))
    print(total)