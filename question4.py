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
        # turn into a list
        line = line.split()
        # check if we are end of file
        if line[STUDENT_ID] != "999":
            # first line is always the answers
            if iteration == 0:
                answers = line
            else:
                # includes student id
                student_grade = line
                student_score = 0
                for i in range(0,len(answers)):
                    # check correct answer
                    if answers[i] == student_grade[i+1]:
                        student_score += 1
                    # check for incorrect answer
                    elif answers[i] != student_grade[i+1] and student_grade[i+1] != "x":
                        student_score -= 1
                # add score to the dict with student id is a key
                scores[student_grade[STUDENT_ID]] = student_score
            iteration += 1
    return scores

def main():
    data = openfile("grades.txt")
    output = find_grades(data)
    for key,value in output.items():
        print(" Student %s: Score : %s" %(str(key), str(value)))

main()