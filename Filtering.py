

def filtering(problem, steps):
    problem.update()
    print(str(problem))
    iterator = 0
    while iterator < steps:
        problem.predict()
        problem.time_step()
        problem.update()
        print(str(problem))
        iterator += 1
