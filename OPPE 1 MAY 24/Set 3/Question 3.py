def courses_sorted_by_enrollment(student_courses: dict) -> list:
    '''
    Given a dictionary of student roll numbers with the list of courses they chose,
    find the courses sorted from the most number of enrollments to the least.
    '''
    # Count enrollments for each course
    course_count = {}
    for courses in student_courses.values():
        for course in courses:
            course_count[course] = course_count.get(course, 0) + 1

    # Sort courses by enrollment count in descending order
    sorted_courses = sorted(course_count, key=course_count.get, reverse=True)
    
    return sorted_courses
