total_tasks = 100
correct_ans = int(input("Provide the number of correct answers: "))
grade = correct_ans/total_tasks
grade = int(grade)
if grade >= 0.5:
    print("Test passed")
