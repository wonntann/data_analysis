import numpy as np

# constant
CURVE_CENTER = 80

# numpy array, 1D and shape of (8,) and type()=int64
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])

# function to handle curved grades
def curve(grades):
    # takes average of all scores using .mean()
    average = grades.mean()
    change = CURVE_CENTER - average
    # vectorization
    new_grades = grades + change
    # broadcasting
    # limit values to a set of min and max set values
    # grades --> ensures that each newly curved grade doesn't go lower than the original grade
    # 100 is broadcast against every element in new_grades, ensure none of the newly curved grades exceeds a perfect score
    return np.clip(new_grades, grades, 100)

curve(grades)    