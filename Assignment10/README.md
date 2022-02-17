# Assignment 10

- Username: mknigh
- Commit hash used for grading: d117426cfca9ea492d0f55da285cf0f93cdcc7df

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests   | 50                  |
| Code Review & style   | 40         |
| Docstrings  | 10                   |


## Total Score: 92/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (43/50 pts)
 
- `sel_sqrt`: 4/4
- `inchtomtuple_lc`: 0/3
- `intomtuple_map`: 3/3

- `bmi_lc`: 3/3
- `bmi_map`: 3/3
- `bmi_cat`: 0/4

- `wbubble_sort`: 15/15
- `rsel_sort`: 15/15



## Code Review & style (39/40 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!

- Problem 1:
    - `sel_sqrt`: 2/2
    - `inchtomtuple_lc`: 4/5
    - `intomtuple_map`: 5/5
    - TA Comments: You had issues with rounding and you you can write in fewer lines. 

- Problem 2:
    - `bmi_calc`: 3/3
    - `bmi_lc`: 5/5
    - `bmi_map`: 5/5
    - `bmi_cat`: 5/5
    - TA Comments: 

- Problem 3:
    - `wbubble_sort`: 5/5
    - TA Comments: 

- Problem 4:
    - `rsel_sort`: 5/5
    - TA Comments:

- Forbidden functions used (if any): _



## Docstrings and Comments (10/10 pts)
Student's functions all have properly formatted docstrings in the right place. You loose 1-5 point for each function that doesn't have proper docstrings or comment.

- Problem 1: 3/3
- Problem 2: 4/4
- Problem 3: 1/1
- Problem 4: 2/2


TA Comments: 




## Pytest Results
- Test test_inchtomtuple_lc on input [86, 68, 50, 78, 54, 71, 48, 60, 89, 57] should result in [(86, 2.1844), (68, 1.7272), (50, 1.27), (78, 1.9812), (54, 1.3716), (71, 1.8034), (48, 1.2192), (60, 1.524), (89, 2.2606), (57, 1.4478)]
  but your code gave [(86, 0.0), (68, 0.0254), (50, 0.0508), (78, 0.0762), (54, 0.1016), (71, 0.127), (48, 0.1524), (60, 0.1778), (89, 0.2032), (57, 0.2286)]
- Test test_inchtomtuple_lc on input [59, 48, 89, 61, 75, 54, 82, 75, 77, 68] should result in [(59, 1.4986), (48, 1.2192), (89, 2.2606), (61, 1.5494), (75, 1.905), (54, 1.3716), (82, 2.0828), (75, 1.905), (77, 1.9558), (68, 1.7272)]
  but your code gave [(59, 0.0), (48, 0.0254), (89, 0.0508), (61, 0.0762), (75, 0.1016), (54, 0.127), (82, 0.1524), (75, 0.1778), (77, 0.2032), (68, 0.2286)]
- Test test_inchtomtuple_lc on input [87, 86, 82, 86, 79, 52, 63, 73, 59, 62] should result in [(87, 2.2098), (86, 2.1844), (82, 2.0828), (86, 2.1844), (79, 2.0066), (52, 1.3208), (63, 1.6002), (73, 1.8542), (59, 1.4986), (62, 1.5748)]
  but your code gave [(87, 0.0), (86, 0.0254), (82, 0.0508), (86, 0.0762), (79, 0.1016), (52, 0.127), (63, 0.1524), (73, 0.1778), (59, 0.2032), (62, 0.2286)]

- Test test_bmi_cat on input [18.5, 39.22, 19.73, 91.54, 44.1, 41.08, 36.9, 34.06, 16.36, 13.65] should result in [(18.5, 'Normal Weight'), (39.22, 'Obese'), (19.73, 'Normal Weight'), (91.54, 'Obese'), (44.1, 'Obese'), (41.08, 'Obese'), (36.9, 'Obese'), (34.06, 'Obese'), (16.36, 'Underweight'), (13.65, 'Underweight')]
  but your code gave [(18.5, 'normal'), (39.22, 'obese'), (19.73, 'normal'), (91.54, 'obese'), (44.1, 'obese'), (41.08, 'obese'), (36.9, 'obese'), (34.06, 'obese'), (16.36, 'underweight'), (13.65, 'underweight')]
- Test test_bmi_cat on input [51.01, 81.47, 69.91, 21.87, 57.89, 35.98, 21.96, 30.74, 32.95, 62.68] should result in [(51.01, 'Obese'), (81.47, 'Obese'), (69.91, 'Obese'), (21.87, 'Normal Weight'), (57.89, 'Obese'), (35.98, 'Obese'), (21.96, 'Normal Weight'), (30.74, 'Obese'), (32.95, 'Obese'), (62.68, 'Obese')]
  but your code gave [(51.01, 'obese'), (81.47, 'obese'), (69.91, 'obese'), (21.87, 'normal'), (57.89, 'obese'), (35.98, 'obese'), (21.96, 'normal'), (30.74, 'obese'), (32.95, 'obese'), (62.68, 'obese')]
- Test test_bmi_cat on input [16.55, 29.01, 25.98, 86.35, 20.4, 9.57, 34.76, 24.4, 66.82, 56.94] should result in [(16.55, 'Underweight'), (29.01, 'Overweight'), (25.98, 'Overweight'), (86.35, 'Obese'), (20.4, 'Normal Weight'), (9.57, 'Underweight'), (34.76, 'Obese'), (24.4, 'Normal Weight'), (66.82, 'Obese'), (56.94, 'Obese')]
  but your code gave [(16.55, 'underweight'), (29.01, 'overweight'), (25.98, 'overweight'), (86.35, 'obese'), (20.4, 'normal'), (9.57, 'underweight'), (34.76, 'obese'), (24.4, 'normal'), (66.82, 'obese'), (56.94, 'obese')]
- Test test_bmi_cat on input [-35, 0, 300] should result in [(-35, 'Underweight'), (0, 'Underweight'), (300, 'Obese')]
  but your code gave [(-35, 'underweight'), (0, 'underweight'), (300, 'obese')]

