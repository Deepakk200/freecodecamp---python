def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    operators = []
    second_operands = []
    answers = []

    for problem in problems:
        parts = problem.split()
        first_operand = parts[0]
        operator = parts[1]
        second_operand = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)

        if operator == '+':
            answers.append(str(int(first_operand) + int(second_operand)))
        else:
            answers.append(str(int(first_operand) - int(second_operand)))

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        line1 += first_operands[i].rjust(width) + "    "
        line2 += operators[i] + " " + second_operands[i].rjust(width - 2) + "    "
        line3 += "-" * width + "    "
        if show_answers:
            line4 += answers[i].rjust(width) + "    "

    if show_answers:
        return line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()
    else:
        return line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

# Example usage
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')
