# Assignment 7

Username: mknigh
Commit hash used for grading: 06253bb6c0b19edfc684dd01ede81fae9fb9fa01

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Lab checkoff  | 10                 |
| Code Tests   | 30                  |
| Docstrings  | 20                   |
| Code Review & style   | 30         |
| Student Tests | 10                 |

## Total Score: 70/100
Please double-check that your Canvas score reflects what is shown here. 


## Lab checkoff (10/10 pts)
The lab checkoff was waived for HW7 so all students get full points for lab check-off.


## Code Tests (0/30 pts)
 
- `process`: 0/6
- `read_ppm`: 0/6
- `write_ppm`: 0/3
- Written file has correct header:0/3
- `scale`: 0/12



## Docstrings and Comments (20/20 pts)
Student's functions all have properly formatted docstrings in the right place.
- `process`: 5/5
- `read_ppm`: 5/5
- `write_ppm`: 5/5
- `scale`: 5/5


TA Comments: 



## Code Review & style (30/30 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!
- `process`: 6/6
- `read_ppm`: 6/6
- `write_ppm`: 6/6
- `scale`: 6/6
- `main` (the function ask the user for row_scale and col_scale (i.e. input), checked that user entered an integer): 6/6

TA Comments: 

- Forbidden functions used (if any): _


## Student Tests (10/10 pts)
We check that you added reasonably comprehensive test cases to your `test_ppm_process.py` file.
- `test_process`: 5/5
- `test_scale`: 5/5



## Pytest Results
- Test test_read_ppm on input 'files/small.ppm' should result in 'the file being correctly read in'
  but your code gave 'the file being incorrectly read in'

- Test test_write_ppm threw error:
Traceback (most recent call last):
  File "2.5-RunAutograder.py", line 178, in <module>
    for x, y, y_actual, result in f():
  File "./a7_grader.py", line 35, in test_write_ppm
    ppm_process.write_ppm(test_list, "files/small_test.ppm")
  File "./ppm_process.py", line 76, in write_ppm
    filename.write()
AttributeError: 'str' object has no attribute 'write'



- Test test_format_write_ppm threw error:
Traceback (most recent call last):
  File "2.5-RunAutograder.py", line 178, in <module>
    for x, y, y_actual, result in f():
  File "./a7_grader.py", line 66, in test_format_write_ppm
    cols = rows_cols.split()[0]
IndexError: list index out of range



- Test test_process on input ['10 11 12 13 14 15', '20 21 22 23 24 25'] should result in [[10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25]]
  but your code gave []
- Test test_process on input [' 10   11  12 13 14 15  ', '  20 21    22 23    24 25'] should result in [[10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25]]
  but your code gave []
- Test test_process on input ['10\t11\n12 13 14 15\n', '\t20 \t 21\t\t 22 23 24 25'] should result in [[10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25]]
  but your code gave []
- Test test_process on input ['10 11', '12 13 14 15', '', '20', '    21 22 23 24 25'] should result in [[10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25]]
  but your code gave [[[20]]]

- Test test_scale on input ([[10, 11, 12, 13, 14, 15, 16, 17, 18], [20, 21, 22, 23, 24, 25, 26, 27, 28], [30, 31, 32, 33, 34, 35, 36, 37, 38]], 1, 1) should result in [[10, 11, 12, 13, 14, 15, 16, 17, 18], [20, 21, 22, 23, 24, 25, 26, 27, 28], [30, 31, 32, 33, 34, 35, 36, 37, 38]]
  but your code gave [[20, 21, 22, 23, 24, 25, 26, 27, 28], [20, 21, 22, 23, 24, 25, 26, 27, 28], [20, 21, 22, 23, 24, 25, 26, 27, 28]]
- Test test_scale on input ([[10, 11, 12, 13, 14, 15, 16, 17, 18], [20, 21, 22, 23, 24, 25, 26, 27, 28], [30, 31, 32, 33, 34, 35, 36, 37, 38]], 3, 1) should result in [[10, 11, 12, 13, 14, 15, 16, 17, 18]]
  but your code gave [[20, 21, 22, 23, 24, 25, 26, 27, 28]]
- Test test_scale on input ([[10, 11, 12, 13, 14, 15, 16, 17, 18], [20, 21, 22, 23, 24, 25, 26, 27, 28], [30, 31, 32, 33, 34, 35, 36, 37, 38]], 1, 3) should result in [[10, 11, 12], [20, 21, 22], [30, 31, 32]]
  but your code gave []
- Test test_scale on input ([[10, 11, 12, 13, 14, 15, 16, 17, 18], [20, 21, 22, 23, 24, 25, 26, 27, 28], [30, 31, 32, 33, 34, 35, 36, 37, 38]], 2, 2) should result in [[10, 11, 12, 16, 17, 18], [30, 31, 32, 36, 37, 38]]
  but your code gave [[30, 31, 32, 33, 34, 35, 36, 37, 38]]

