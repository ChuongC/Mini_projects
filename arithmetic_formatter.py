
def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    first = []
    second = []
    dashes = []
    results = []

    for p in problems:
        parts = p.split()
        left, op, right = parts
        if op != "+" and op != "-":
            return "Error: Operator must be '+' or '-'."

        if not left.isdigit() or not right.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = int(max(len(left), len(right)) + 2)

        first.append(left.rjust(width,' '))
        second.append(op + right.rjust(width - 1, ' '))
        dashes.append("-" * width)
        if show_answers:
            if op=="+":
                result = int(left) + int(right)
            if op=="-":
                result = int(left) - int(right)
            results.append(str(result).rjust(width))
    
    problems = '    '.join(first) + '\n' + '    '.join(second) + '\n' + '    '.join(dashes)
    if show_answers:
        problems += ('\n' + '    '.join(results))

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')