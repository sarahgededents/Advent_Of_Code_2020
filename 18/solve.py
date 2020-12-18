with open("input") as inp:
    lines_op = [line for line in inp]


def eval_expr(expression, precedence=('+', '*')):
    def eat(expected):
        nonlocal i
        if expression[i] == expected:
            i += 1
            return True
        return False

    def expr(p=0):
        nonlocal i
        if p >= len(precedence):
            return terminal()
        val = expr(p+1)
        while i < len(expression) and expression[i] in precedence[p]:
            if eat('+'):
                val += expr(p+1)
            elif eat('*'):
                val *= expr(p+1)
        return val

    def terminal():
        nonlocal i
        val = None
        if expression[i].isdigit():
            val = int(expression[i])
            i += 1
        elif eat('('):
            val = expr()
            assert eat(')')
        return val
    i = 0
    expression = expression.replace(' ', '')
    return expr()


print("Part 1:", sum(eval_expr(line, ('*+',)) for line in lines_op))
print("Part 2:", sum(eval_expr(line, ('*', '+')) for line in lines_op))
