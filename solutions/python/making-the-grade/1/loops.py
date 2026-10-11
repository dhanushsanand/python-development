"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores:list[float]):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """
    new_scores = [round(score) for score in student_scores]
    return new_scores
    # for score in student_scores:
    #     rounded_score = 
    #     new_scores.append()


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
    fail = 0
    for score in student_scores:
        if score <= 40:
            fail+=1
    return fail


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """
    best = []
    for score in student_scores:
        if score >= threshold:
            best.append(score)
    return best


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    grade_intervals = (highest - 40)//4
    letter_scores = [41]
    for i in range(1,4):
        letter_scores.append(letter_scores[i-1] + grade_intervals)
    return letter_scores


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    ranking_list = []
    for i in range(len(student_scores)):
        pretty_print = f"{i+1}. {student_names[i]}: {student_scores[i]}"
        ranking_list.append(pretty_print)
    return ranking_list


def perfect_score(student_info:list[list]):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    perfect_student = []
    for item in student_info:
        if item[1] == 100:
            perfect_student = item
            break
    return perfect_student if perfect_student else []
