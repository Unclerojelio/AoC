import sys

lines = sys.stdin.readlines()
lines = [line.rstrip() for line in lines]
group = []
groups = []

def process(groups):
    answers = set()
    declarations = []
    for group in groups:
        for answer in group:
            for letter in answer:
                answers.add(letter)
        declarations.append(answers)
        answers = set()
    return declarations

def alternate_process(groups):
    answer_set = set()
    declarations = []
    for group in groups:
        num_in_group = len(group)
        declaration = []
        for answers in group:
            for answer in answers:
                declaration.append(answer)
        #print(declaration)
        for answer in declaration:
            if declaration.count(answer) == num_in_group:
                answer_set.add(answer)
        declarations.append(answer_set)
        answer_set = set()
    return declarations


def count_answers(declarations):
    count = 0
    for answers in declarations:
        count += len(answers)
    return count

for line in lines:
    if len(line) == 0:
        groups.append(group)
        group = []
    else:
        group.append(line)
groups.append(group)
#alternate_process(groups)

print(f"Part 1: {count_answers(process(groups))} Part 2: {count_answers(alternate_process(groups))}")