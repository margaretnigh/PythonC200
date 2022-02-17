# Assignment6

Username: mknigh
Commit hash used for grading: 9a6066639dfab9549056ae8df61c1a8fce257717

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests (Part 1: Decode)   | 25           |
| Code Tests (Part 2: Grey Scale) | 25   |
| Docstrings  | 15           |
| Code Review & style   | 20           |
| Student Tests | 15    |

## Total Score: 58/100
Please double-check that your Canvas score reflects what is shown here.


## Code Tests (Part 1: Decode) (10/25 pts)

- Successfully writes to file: 6/6
- Written file has correct ppm format: 0/6
- `process_ppm` writes the correct contents to file: 0/6
- `color_translate` returns the correct string: 4/7


## Code Tests (Part 2: Grey Scale) (13/25 pts)

- Successfully writes to file: 6/6
- Written file has correct ppm format: 0/6
- Values in written file are within 0 and 255: 3/3
- `grey_scale` returns the correct string: 4/10


## Docstrings and Comments (15/15 pts)
Student's functions all have properly formatted docstrings in the right place
- `color_translate`: 5/5
- `process_ppm`: 5/5
- `grey_scale` : 5/5

TA Comments: 


## Code Review & style (20/20 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!
- `color_translate`: 4/4
- `process_ppm`: 4/4
- `main_part1` : 4/4
- `grey_scale` : 4/4
- `main` : 4/4

TA Comments: 

- Forbidden functions used (if any): _


## Student Tests (0/15 pts)
We check that you added reasonably comprehensive test cases to your `test_process_ppm.py` file.
- `color_translate`: 0/7.5
- `grey_scale` : 0/7.5

## Pytest Results
- Test test_format_1 threw error:
Traceback (most recent call last):
  File "2.5-RunAutograder.py", line 179, in <module>
    for x, y, y_actual, result in f():
  File "./a6_grader.py", line 78, in test_format_1
    out_cols = out_rows_cols.split()[0]
IndexError: list index out of range



- Test test_process_ppm on input ('files/small.ppm', 'files/small_out_part1.ppm', 'color_translate') should result in '  0   0   0   0   0   0   0   0   0   0   0   0\n  0   0   0   0   0   0   0   0   0   0   0   0\n  0   0   0   0   0   0   0   0   0   0   0   0\n  0   0   0   0   0   0   0   0   0   0   0   0\n  0   0   0   0   0   0   0   0   0   0   0   0\n  0   0   0   0   0   0   0   0   0   0   0   0'
  but your code gave '\n255\n\n0 0   0       0   0 0      0   0   0    0 0 0 \n0   0   0       0 0   0      0   0 0      0   0   0 \n0 0   0     0   0   0      0 0   0      0   0 0 \n0   0 0     0 0   0    0   0   0      0 0   0 \n0 0   0       0   0 0      0   0   0    0 0 0 \n0   0   0       0 0   0      0   0 0      0   0   0 \n'

- Test test_color_translate on input '1 2 3 4 5 6' should result in '153 255   0 153 255   0'
  but your code gave '153 2 0 153 5 0 '
- Test test_color_translate on input '10 20 30 40 50 60 70 80 90' should result in '153 255   0 153 255   0 153 255   0'
  but your code gave '153 20 0 153 50 0 153 80 0 '

- Test test_format_2 threw error:
Traceback (most recent call last):
  File "2.5-RunAutograder.py", line 179, in <module>
    for x, y, y_actual, result in f():
  File "./a6_grader.py", line 223, in test_format_2
    out_cols = out_rows_cols.split()[0]
IndexError: list index out of range



- Test test_grey_scale on input '10 20 30 40 50 60 70 80 90' should result in '37 37 37 87 87 87 139 139 139'
  but your code gave '38 38 38 88 88 88 140 140 140 '
- Test test_grey_scale on input '10 30 20 60 50 40 70 90 80' should result in '37 37 37 87 87 87 139 139 139'
  but your code gave '38 38 38 88 88 88 140 140 140 '
- Test test_grey_scale on input '153 0 255 255 153 0 256 257 258' should result in '255 255 255 255 255 255 255 255 255'
  but your code gave '225 225 225 225 225 225 225 225 225 '

