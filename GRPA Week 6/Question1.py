# heterogeneous - multi line
def get_student_details():
    '''
    Get the student details over multiple lines

    Input format:

    name
    age
    rollno

    Return: name:str, age:int, rollno:int
    '''
    name, age, rollno = input(),int(input()),int(input())
    return name, age, rollno

# heterogeneous - single line 
def get_student_details_same_line():
    '''
    Get the student details from the same line

    Input format:(separated by space)

    name age rollno

    Return: name:str, age:int, rollno:int
    '''
    name, age , rollno = input().split()
    age, rollno =int(age), int(rollno)
    
    return name, age, rollno

# homogeneous - single line
def get_comma_separated_integers():
    '''
    Get a list of comma separated integers from input

    Return: numbers:list[int]
    '''
    numbers= list(map(int,input().split(",")))

    return numbers

# homogeneous - multi-line - definite
def get_n_float_numbers():
    '''
    Get n float numbers with one number in each line 
    and the first line has n.

    Input Format:
    n
    num1
    num2
    ...
    numn

    Return: nums:list[float]
    '''
    n=int(input())
    nums=[float(input()) for i in range(n)]

    return nums

# homogeneous - multi-line - indefinite
def get_nums_until_end():
    '''
    Get float numbers with one number in each line 
    until the input is "end"(case insensitive)

    Input Format:
    num1
    num2
    ...
    numx
    End

    Return: nums:list[float]
    '''
    nums=[]
    while True:
        num=input()
        if num.lower()=="end":
            break
        nums.append(float(num))    

    return nums

# hybrid - single line
def get_batsman_runs():
    '''
    Get batsman name, number and runs as a list

    Input format: (separated by space)
    name no run1 run2 run3 ...

    Return: name:str, no:int, runs:list[int]
    '''
    name, no, *runs=input().split()
    no=int(no)
    runs=list(map(int,runs))

    return name, no, runs

# key value 
def get_course_scores():
    '''
    Get course name and scores of the over multiple lines where 
    course name and scores are separated by a hypen in each line.
    First line corresponds to the number or entries.

    Input format:
    2
    course1-score1
    course2-score2

    Return: dict[str,int] - with course name as key and score as value
    '''
    n=int(input())
    #course_scores={}
    #for i in range(n):
    course_scores = [input().split('-') for i in range(n)]
    course_scores={course: int(score) for course, score in course_scores}

    return course_scores

# dict with list as values
def get_all_batsman_runs():
    '''
    Given the batsman name and the comma separated runs 
    where both are seperted by a hypen in multiple lines, 
    create a dictionary with batsman name and list of runs as value.
    The number of lines is given in the first line

    Input format:
    3
    batsman1-1,2,1,4,6,2,2,1
    batsman2-2,2,6,4,1
    batsman3-6,1,2,4,4,2

    Return: dict[str,list[int]] - with batsman name as key and list of runs as values
    '''
    n=int(input())
    batsman_runs =[input().split('-') for i in range(n)]
    batsman_runs= { 
        name:list(map(int,runs.split(',')))
        for name, runs in batsman_runs
    }
    return batsman_runs

# csv - list of dicts
    n = int(input().strip())
    student_data = []

    for _ in range(n):
        rollno, city, age, course1, course2, course3 = input().strip().split(',')
        rollno, age, course1, course2, course3 = map(int, [rollno, age, course1, course2, course3])
        student_data.append({
            "rollno": rollno,
            "city": city,
            "age": age,
            "course1": course1,
            "course2": course2,
            "course3": course3,
        })
        return student_data

# list of dicts
def get_student_data_over_multiple_lines():
    '''
    Given each attribute as described above in given over multiple lines 
    and multiple entries are given create a dictionary as described above.

    Input format:
    n
    1
    citya
    23
    86
    69
    86
    2
    cityb
    19
    78
    65
    89
    ...
    n
    cityx
    35
    89
    57
    76
    '''

    student_data=[
        { 
            "rollno":int(input()), "city": input(), "age": int(input()), 
            "course1":int(input()), "course2":int(input()), "course3": int(input()),
        }
        for i in range(int(input()))
    ]
    return student_data

# this will read the function name from the input.
func = eval(input()) 

# this will read the actual output that is required which is the second line
expected_output = eval(input())

# The remaining of the input should be read by your function
actual_output = func()

if expected_output != actual_output:
    print("Your output doesn't match the expected output.")
print(actual_output)
