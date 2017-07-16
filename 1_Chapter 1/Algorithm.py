## This function determine the run time and correctness of the algorithm.

def algorithm_development(problem_spec):
    correct = false
    while not correct or not fast_enough(running_time):
        algorithm = devise_algorithm(problem_spec)
        correct = analyze_correctness(algorithm)
        running_time = analyze_efficiency(algorithm_development)
    return algorithm