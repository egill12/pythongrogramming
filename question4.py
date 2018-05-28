def openfile(filename):
    '''

    :param filename:
    :return:
    '''
    with open(filename) as f:
        return f.readlines()

def find_grades(data):
    '''
    :param data:
    :return:
    '''
    STUDENT_ID = 0
    iteration = 0
    scores = {}
    for line in data:
        if line[STUDENT_ID] != "XXX":
            if iteration == 0:
                answers = line.split()
            else:
                # includes student id
                student_grade = line.split()
                student_score = 0
                for i in range(0,len(answers)):
                    # check correct answer
                    if answers[i] == student_grade[i+1]:
                        student_score += 1
                    # check for incorrect answer
                    elif answers[i] != student_grade[i+1] and student_grade[i+1] != "x":
                        student_score -= 1
                scores[student_grade[STUDENT_ID]] == student_score
    return scores

print(find_grades(openfile("grades.txt")))