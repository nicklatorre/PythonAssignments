import random
score = random.randint(60,100)
print "Your score is {}".format(score)

def grade(mark):
    if mark >= 90:
        grade = "A"
    if mark >= 80 and mark < 90:
        grade = "B"
    if mark >= 70 and mark <80:
        grade = "C"
    if mark <70:
        grade = "D"
    print "Score: {}; Your grade is {}".format(mark,grade)
