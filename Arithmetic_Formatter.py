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


        

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
