# Assignment 9

- Username: mknigh
- Commit hash used for grading: cfa78757be3f989b745f47386ededcf1b2ea9145

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests   | 50                  |
| Docstrings  | 15                   |
| Code Review & style   | 20         |
| Student Tests | 15                 |  


## Total Score: 70/100
Please double-check that your Canvas score reflects what is shown here. 



## Code Tests (20.0/50 pts)
 
- `pop`: 2/2
- `error`: 6/6


- `get_dic`: 0/5
- `get_state_pop`: 0/5
- `scd`: 0/4
- `ccc`: 0/6
- `sdd`: 0/5
- `usdd`: 0/5


- `simpson`: 12.0/12


## Docstrings and Comments (15/15 pts)
Student's functions all have properly formatted docstrings in the right place. You loose 1,5 point for each function that doesn't have proper docstrings or comment.

- Problem 1: 3/3
- Problem 2: 10/10
- Problem 3: 2/2


TA Comments: 



## Code Review & style (20/20 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!

- Problem 1:
    - `pop`: 2/2
    - `error`: 2/2
    - TA Comments: 

- Problem 2:
    - `scd`: 2/2
    - `ccc`: 2/2
    - `sdd`: 2/2
    - `usdd`: 2/2
    - `get_dic`: 2/2
    - `get_state_pop`: 2/2
    - TA Comments: Your logic seems right. although I didn't run your file without the error. You are not handling the directory right. 

- Problem 3:
    - `simpson`: 4/4
    - TA Comments: 


- Forbidden functions used (if any): _


## Student Tests (15/15 pts)
We check that you added reasonably comprehensive test cases to your `test_a9.py` file. 

- `test_pop`: 4/4
- `test_error`: 4/4
- `test_get_data`: 3/3
- `test_simpson`: 4/4



## Pytest Results
- Test test_error threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 29, in test_error
    yield x, y, (a9.error(x)), (round(a9.error(x), 2) == round(y, 2))
  File "./a9.py", line 46, in error
    avg = avg * (100/len(data))
ZeroDivisionError: division by zero



- Test test_get_dic threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 40, in test_get_dic
    test_dic = a9.get_dic("us-counties.csv")
  File "./a9.py", line 176, in get_dic
    with open('./Assignment9/' + file_path, newline='') as csvfile:
FileNotFoundError: [Errno 2] No such file or directory: './Assignment9/us-counties.csv'



- Test test_state_pop threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 53, in test_state_pop
    test_state_pop = a9.get_state_pop("sp.csv")
  File "./a9.py", line 213, in get_state_pop
    with open('./Assignment9/' + file_path, newline='') as csvfile:
FileNotFoundError: [Errno 2] No such file or directory: './Assignment9/sp.csv'



- Test test_scd threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 63, in test_scd
    test_dic = a9.get_dic("us-counties.csv")
  File "./a9.py", line 176, in get_dic
    with open('./Assignment9/' + file_path, newline='') as csvfile:
FileNotFoundError: [Errno 2] No such file or directory: './Assignment9/us-counties.csv'



- Test test_ccc threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 74, in test_ccc
    test_dic = a9.get_dic("us-counties.csv")
  File "./a9.py", line 176, in get_dic
    with open('./Assignment9/' + file_path, newline='') as csvfile:
FileNotFoundError: [Errno 2] No such file or directory: './Assignment9/us-counties.csv'



- Test test_sdd threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 97, in test_sdd
    test_dic = a9.get_dic("us-counties.csv")
  File "./a9.py", line 176, in get_dic
    with open('./Assignment9/' + file_path, newline='') as csvfile:
FileNotFoundError: [Errno 2] No such file or directory: './Assignment9/us-counties.csv'



- Test test_usdd threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 110, in test_usdd
    test_dic = a9.get_dic("us-counties.csv")
  File "./a9.py", line 176, in get_dic
    with open('./Assignment9/' + file_path, newline='') as csvfile:
FileNotFoundError: [Errno 2] No such file or directory: './Assignment9/us-counties.csv'



