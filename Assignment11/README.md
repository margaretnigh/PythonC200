# Assignment 11

- Username: mknigh
- Commit hash used for grading: 03e9d99d97261b96a49da8be491bdd61490f66e3

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 30         |
| Code Review & style   | 30         |
| Student tests         | 30         |
| Docstrings            | 10         |


## Total Score: 57/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (7/30 pts)
See Pytest output below for a detailed description of the tests
that failed.


## Code Review & style (30/30 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!

- Problem 1:
    - `check_number`: 3/3
    - `parse_date`: 6/6
    - TA Comments: No syntax errors. See errors below. Most functions not raising errors or doing so incorrectly

- Problem 2:
    - `_op1`: 4/4
    - `_op2`: 4/4
    - `clear`: 3/3
    - `e`: 1/1
    - `ln`: 1/1
    - `add`: 1/1
    - `div`: 1/1
    - `mult`: 1/1
    - `minus`: 1/1
    - `exp`: 1/1
    - `push`: 3/3
    - TA Comments: No syntax errors. See errors below. Most functions not raising errors or doing so incorrectly

- Forbidden functions used (if any): _


## Student Tests (20/30 pts)
- You had to provide 2 test case for each function/method,
  with the exception of the `calc.e` function.

- Problem 1:
    - `test_check_number`: 3/3
    - `test_date_syntax`: 3/3


- Problem 2:
    - `test_calc_e`: 3/3
    - `test_calc_ln`: 1.5/3
    - `test_calc_add`: 1.5/3
    - `test_calc_mult`: 1.5/3
    - `test_calc_minus`: 1.5/3
    - `test_calc_div`: 1.5/3
    - `test_calc_exp`: 1.5/3
    - `test_calc_push`: 3/3

- TA Comments: Only 1 test for most functions in part 2


## Docstrings and Comments (0/10 pts)
Student's functions all have properly formatted docstrings in the right place. You lose 1 point for each function that doesn't have proper docstrings or comment.

- Problem 1: Docstrings were given
- Problem 2: 0/10



TA Comments: 

## Pytest Results
```
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-6.2.5, py-1.9.0, pluggy-0.13.1
rootdir: /home/kbub/Fall-2021/GradingData/Assignment11/mknigh
plugins: assume-2.4.3
collected 68 items

test_a11.py FF..............FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF [ 88%]
FFFFFFF.                                                                 [100%]

=================================== FAILURES ===================================
_________________________ test_check_number[-3--1-10] __________________________

i = -3, low = -1, high = 10

    @pytest.mark.parametrize('i,low,high',
    [ (i,-1,10) for i in range(-3,11) ])
    def test_check_number(i,low,high):
        if i >= low and i <= high:
            assert i == a11.check_number(i,'foo',low,high)
        else:
            with pytest.raises(ValueError, match=f"Invalid foo {i}" ):
>               a11.check_number(i,'foo',low,high)
E               Failed: DID NOT RAISE <class 'ValueError'>

test_a11.py:14: Failed
_________________________ test_check_number[-2--1-10] __________________________

i = -2, low = -1, high = 10

    @pytest.mark.parametrize('i,low,high',
    [ (i,-1,10) for i in range(-3,11) ])
    def test_check_number(i,low,high):
        if i >= low and i <= high:
            assert i == a11.check_number(i,'foo',low,high)
        else:
            with pytest.raises(ValueError, match=f"Invalid foo {i}" ):
>               a11.check_number(i,'foo',low,high)
E               Failed: DID NOT RAISE <class 'ValueError'>

test_a11.py:14: Failed
___________________________ test_date_syntax2[12/03] ___________________________

input_str = '12/03'

    @pytest.mark.parametrize('input_str',[
    ('12/03'),
    ('12/03/abcd'),
    ('12/3/2000'),
    ('12/3/45'),
    ('1/23/2003'),
    ('11-22/2003')
    ])
    def test_date_syntax2(input_str):
        with pytest.raises(SyntaxError, match = f'Incorrect Date Syntax {input_str}' ):
>           a11.parse_date(input_str)

test_a11.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = '12/03'

    def parse_date(s):
        """
        Checks that s is a valid date mm/dd/yyyy or mm-dd-yyyy
        Raises SyntaxError if form is wrong or mm, dd,
        yyyy are not digit strings with correct number
        of digits.
        Raises ValueError if mm, dd, yyyy are not in legal ranges
        (checked in order mm, dd, yyyy)
    
        Returns (int(mm),int(dd),int(yyyy))
        """
    
        while True:
            if "-" or "/" in s:
                #seperate date by / or -  (mm/dd/yyyy or mm-dd-yyyy)
                if "-" in s:
                    new = s.split("-")
                elif "/" in s:
                    new = s.split("/")
                else:
                    raise SyntaxError
                if len(new) == 3:
                    month = new[0]
                    day = new[1]
                    year = new[2]
                else:
>                   raise SyntaxError
E                     File "<string>", line None
E                   SyntaxError: <no detail available>

a11.py:48: SyntaxError

During handling of the above exception, another exception occurred:

input_str = '12/03'

    @pytest.mark.parametrize('input_str',[
    ('12/03'),
    ('12/03/abcd'),
    ('12/3/2000'),
    ('12/3/45'),
    ('1/23/2003'),
    ('11-22/2003')
    ])
    def test_date_syntax2(input_str):
        with pytest.raises(SyntaxError, match = f'Incorrect Date Syntax {input_str}' ):
>           a11.parse_date(input_str)
E           AssertionError: Regex pattern 'Incorrect Date Syntax 12/03' does not match 'None'.

test_a11.py:33: AssertionError
________________________ test_date_syntax2[12/03/abcd] _________________________

input_str = '12/03/abcd'

    @pytest.mark.parametrize('input_str',[
    ('12/03'),
    ('12/03/abcd'),
    ('12/3/2000'),
    ('12/3/45'),
    ('1/23/2003'),
    ('11-22/2003')
    ])
    def test_date_syntax2(input_str):
        with pytest.raises(SyntaxError, match = f'Incorrect Date Syntax {input_str}' ):
>           a11.parse_date(input_str)

test_a11.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = '12/03/abcd'

    def parse_date(s):
        """
        Checks that s is a valid date mm/dd/yyyy or mm-dd-yyyy
        Raises SyntaxError if form is wrong or mm, dd,
        yyyy are not digit strings with correct number
        of digits.
        Raises ValueError if mm, dd, yyyy are not in legal ranges
        (checked in order mm, dd, yyyy)
    
        Returns (int(mm),int(dd),int(yyyy))
        """
    
        while True:
            if "-" or "/" in s:
                #seperate date by / or -  (mm/dd/yyyy or mm-dd-yyyy)
                if "-" in s:
                    new = s.split("-")
                elif "/" in s:
                    new = s.split("/")
                else:
                    raise SyntaxError
                if len(new) == 3:
                    month = new[0]
                    day = new[1]
                    year = new[2]
                else:
                    raise SyntaxError
                if month.isdigit() and day.isdigit() and year.isdigit():
                        mm = check_number(int(month),ValueError(f"Invalid Month {month}"),1,12)
                        dd = check_number(int(day),ValueError(f"Invalid Day {day}"),1,31)
                        yy = check_number(int(year),ValueError(f"Invalid Year {year}"),1900,2021)
                        if mm == int(month) and dd == int(day) and yy == int(year):
                            return (int(mm),int(dd),int(yy))
                        else:
                            #check for specific errors in date
                            if mm != int(month):
                                return mm
                            if dd != int(day):
                                return dd
                            if yy != int(year):
                               return yy
                else:
                    #not numbers
>                   raise ValueError
E                   ValueError

a11.py:65: ValueError
_________________________ test_date_syntax2[12/3/2000] _________________________

input_str = '12/3/2000'

    @pytest.mark.parametrize('input_str',[
    ('12/03'),
    ('12/03/abcd'),
    ('12/3/2000'),
    ('12/3/45'),
    ('1/23/2003'),
    ('11-22/2003')
    ])
    def test_date_syntax2(input_str):
        with pytest.raises(SyntaxError, match = f'Incorrect Date Syntax {input_str}' ):
>           a11.parse_date(input_str)
E           Failed: DID NOT RAISE <class 'SyntaxError'>

test_a11.py:33: Failed
__________________________ test_date_syntax2[12/3/45] __________________________

input_str = '12/3/45'

    @pytest.mark.parametrize('input_str',[
    ('12/03'),
    ('12/03/abcd'),
    ('12/3/2000'),
    ('12/3/45'),
    ('1/23/2003'),
    ('11-22/2003')
    ])
    def test_date_syntax2(input_str):
        with pytest.raises(SyntaxError, match = f'Incorrect Date Syntax {input_str}' ):
>           a11.parse_date(input_str)
E           Failed: DID NOT RAISE <class 'SyntaxError'>

test_a11.py:33: Failed
_________________________ test_date_syntax2[1/23/2003] _________________________

input_str = '1/23/2003'

    @pytest.mark.parametrize('input_str',[
    ('12/03'),
    ('12/03/abcd'),
    ('12/3/2000'),
    ('12/3/45'),
    ('1/23/2003'),
    ('11-22/2003')
    ])
    def test_date_syntax2(input_str):
        with pytest.raises(SyntaxError, match = f'Incorrect Date Syntax {input_str}' ):
>           a11.parse_date(input_str)
E           Failed: DID NOT RAISE <class 'SyntaxError'>

test_a11.py:33: Failed
________________________ test_date_syntax2[11-22/2003] _________________________

input_str = '11-22/2003'

    @pytest.mark.parametrize('input_str',[
    ('12/03'),
    ('12/03/abcd'),
    ('12/3/2000'),
    ('12/3/45'),
    ('1/23/2003'),
    ('11-22/2003')
    ])
    def test_date_syntax2(input_str):
        with pytest.raises(SyntaxError, match = f'Incorrect Date Syntax {input_str}' ):
>           a11.parse_date(input_str)

test_a11.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = '11-22/2003'

    def parse_date(s):
        """
        Checks that s is a valid date mm/dd/yyyy or mm-dd-yyyy
        Raises SyntaxError if form is wrong or mm, dd,
        yyyy are not digit strings with correct number
        of digits.
        Raises ValueError if mm, dd, yyyy are not in legal ranges
        (checked in order mm, dd, yyyy)
    
        Returns (int(mm),int(dd),int(yyyy))
        """
    
        while True:
            if "-" or "/" in s:
                #seperate date by / or -  (mm/dd/yyyy or mm-dd-yyyy)
                if "-" in s:
                    new = s.split("-")
                elif "/" in s:
                    new = s.split("/")
                else:
                    raise SyntaxError
                if len(new) == 3:
                    month = new[0]
                    day = new[1]
                    year = new[2]
                else:
>                   raise SyntaxError
E                     File "<string>", line None
E                   SyntaxError: <no detail available>

a11.py:48: SyntaxError

During handling of the above exception, another exception occurred:

input_str = '11-22/2003'

    @pytest.mark.parametrize('input_str',[
    ('12/03'),
    ('12/03/abcd'),
    ('12/3/2000'),
    ('12/3/45'),
    ('1/23/2003'),
    ('11-22/2003')
    ])
    def test_date_syntax2(input_str):
        with pytest.raises(SyntaxError, match = f'Incorrect Date Syntax {input_str}' ):
>           a11.parse_date(input_str)
E           AssertionError: Regex pattern 'Incorrect Date Syntax 11-22/2003' does not match 'None'.

test_a11.py:33: AssertionError
____________________ test_date_syntax3[00/02/2002-0-Month] _____________________

input_str = '00/02/2002', val = '0', msg = 'Month'

    @pytest.mark.parametrize('input_str,val, msg',[
        ('00/02/2002','0','Month'),
        ('33/02/2002','33','Month'),
        ('01/00/2002','0','Day'),
        ('01/33/2002','33','Day'),
        ('01-01-1800','1800','Year'),
        ('01-01-2022','2022','Year')
    ])
    
    def test_date_syntax3(input_str,val,msg):
        with pytest.raises(ValueError,match= f'Invalid {msg} {val}'):
>           a11.parse_date(input_str)
E           Failed: DID NOT RAISE <class 'ValueError'>

test_a11.py:46: Failed
____________________ test_date_syntax3[33/02/2002-33-Month] ____________________

input_str = '33/02/2002', val = '33', msg = 'Month'

    @pytest.mark.parametrize('input_str,val, msg',[
        ('00/02/2002','0','Month'),
        ('33/02/2002','33','Month'),
        ('01/00/2002','0','Day'),
        ('01/33/2002','33','Day'),
        ('01-01-1800','1800','Year'),
        ('01-01-2022','2022','Year')
    ])
    
    def test_date_syntax3(input_str,val,msg):
        with pytest.raises(ValueError,match= f'Invalid {msg} {val}'):
>           a11.parse_date(input_str)
E           Failed: DID NOT RAISE <class 'ValueError'>

test_a11.py:46: Failed
_____________________ test_date_syntax3[01/00/2002-0-Day] ______________________

input_str = '01/00/2002', val = '0', msg = 'Day'

    @pytest.mark.parametrize('input_str,val, msg',[
        ('00/02/2002','0','Month'),
        ('33/02/2002','33','Month'),
        ('01/00/2002','0','Day'),
        ('01/33/2002','33','Day'),
        ('01-01-1800','1800','Year'),
        ('01-01-2022','2022','Year')
    ])
    
    def test_date_syntax3(input_str,val,msg):
        with pytest.raises(ValueError,match= f'Invalid {msg} {val}'):
>           a11.parse_date(input_str)
E           Failed: DID NOT RAISE <class 'ValueError'>

test_a11.py:46: Failed
_____________________ test_date_syntax3[01/33/2002-33-Day] _____________________

input_str = '01/33/2002', val = '33', msg = 'Day'

    @pytest.mark.parametrize('input_str,val, msg',[
        ('00/02/2002','0','Month'),
        ('33/02/2002','33','Month'),
        ('01/00/2002','0','Day'),
        ('01/33/2002','33','Day'),
        ('01-01-1800','1800','Year'),
        ('01-01-2022','2022','Year')
    ])
    
    def test_date_syntax3(input_str,val,msg):
        with pytest.raises(ValueError,match= f'Invalid {msg} {val}'):
>           a11.parse_date(input_str)
E           Failed: DID NOT RAISE <class 'ValueError'>

test_a11.py:46: Failed
___________________ test_date_syntax3[01-01-1800-1800-Year] ____________________

input_str = '01-01-1800', val = '1800', msg = 'Year'

    @pytest.mark.parametrize('input_str,val, msg',[
        ('00/02/2002','0','Month'),
        ('33/02/2002','33','Month'),
        ('01/00/2002','0','Day'),
        ('01/33/2002','33','Day'),
        ('01-01-1800','1800','Year'),
        ('01-01-2022','2022','Year')
    ])
    
    def test_date_syntax3(input_str,val,msg):
        with pytest.raises(ValueError,match= f'Invalid {msg} {val}'):
>           a11.parse_date(input_str)
E           Failed: DID NOT RAISE <class 'ValueError'>

test_a11.py:46: Failed
___________________ test_date_syntax3[01-01-2022-2022-Year] ____________________

input_str = '01-01-2022', val = '2022', msg = 'Year'

    @pytest.mark.parametrize('input_str,val, msg',[
        ('00/02/2002','0','Month'),
        ('33/02/2002','33','Month'),
        ('01/00/2002','0','Day'),
        ('01/33/2002','33','Day'),
        ('01-01-1800','1800','Year'),
        ('01-01-2022','2022','Year')
    ])
    
    def test_date_syntax3(input_str,val,msg):
        with pytest.raises(ValueError,match= f'Invalid {msg} {val}'):
>           a11.parse_date(input_str)
E           Failed: DID NOT RAISE <class 'ValueError'>

test_a11.py:46: Failed
____________________________ test_plus[input_data0] ____________________________

input_data = (-9, -9)

    @pytest.mark.parametrize("input_data",data)
    def test_plus(input_data):
>       c.clear()

test_a11.py:59: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_plus[input_data1] ____________________________

input_data = (-5, -5)

    @pytest.mark.parametrize("input_data",data)
    def test_plus(input_data):
>       c.clear()

test_a11.py:59: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_plus[input_data2] ____________________________

input_data = (-1, -1)

    @pytest.mark.parametrize("input_data",data)
    def test_plus(input_data):
>       c.clear()

test_a11.py:59: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_plus[input_data3] ____________________________

input_data = (3, 3)

    @pytest.mark.parametrize("input_data",data)
    def test_plus(input_data):
>       c.clear()

test_a11.py:59: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_plus[input_data4] ____________________________

input_data = (7, 7)

    @pytest.mark.parametrize("input_data",data)
    def test_plus(input_data):
>       c.clear()

test_a11.py:59: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
___________________________ test_minus[input_data0] ____________________________

input_data = (-9, -9)

    @pytest.mark.parametrize("input_data",data)
    def test_minus(input_data):
>       c.clear()

test_a11.py:67: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
___________________________ test_minus[input_data1] ____________________________

input_data = (-5, -5)

    @pytest.mark.parametrize("input_data",data)
    def test_minus(input_data):
>       c.clear()

test_a11.py:67: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
___________________________ test_minus[input_data2] ____________________________

input_data = (-1, -1)

    @pytest.mark.parametrize("input_data",data)
    def test_minus(input_data):
>       c.clear()

test_a11.py:67: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
___________________________ test_minus[input_data3] ____________________________

input_data = (3, 3)

    @pytest.mark.parametrize("input_data",data)
    def test_minus(input_data):
>       c.clear()

test_a11.py:67: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
___________________________ test_minus[input_data4] ____________________________

input_data = (7, 7)

    @pytest.mark.parametrize("input_data",data)
    def test_minus(input_data):
>       c.clear()

test_a11.py:67: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_mult[input_data0] ____________________________

input_data = (-9, -9)

    @pytest.mark.parametrize("input_data",data)
    def test_mult(input_data):
>       c.clear()

test_a11.py:75: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_mult[input_data1] ____________________________

input_data = (-5, -5)

    @pytest.mark.parametrize("input_data",data)
    def test_mult(input_data):
>       c.clear()

test_a11.py:75: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_mult[input_data2] ____________________________

input_data = (-1, -1)

    @pytest.mark.parametrize("input_data",data)
    def test_mult(input_data):
>       c.clear()

test_a11.py:75: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_mult[input_data3] ____________________________

input_data = (3, 3)

    @pytest.mark.parametrize("input_data",data)
    def test_mult(input_data):
>       c.clear()

test_a11.py:75: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_mult[input_data4] ____________________________

input_data = (7, 7)

    @pytest.mark.parametrize("input_data",data)
    def test_mult(input_data):
>       c.clear()

test_a11.py:75: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_div[input_data0] _____________________________

input_data = (-9, -9)

    @pytest.mark.parametrize("input_data",data)
    def test_div(input_data):
>       c.clear()

test_a11.py:84: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_div[input_data1] _____________________________

input_data = (-5, -5)

    @pytest.mark.parametrize("input_data",data)
    def test_div(input_data):
>       c.clear()

test_a11.py:84: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_div[input_data2] _____________________________

input_data = (-1, -1)

    @pytest.mark.parametrize("input_data",data)
    def test_div(input_data):
>       c.clear()

test_a11.py:84: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_div[input_data3] _____________________________

input_data = (3, 3)

    @pytest.mark.parametrize("input_data",data)
    def test_div(input_data):
>       c.clear()

test_a11.py:84: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_div[input_data4] _____________________________

input_data = (7, 7)

    @pytest.mark.parametrize("input_data",data)
    def test_div(input_data):
>       c.clear()

test_a11.py:84: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_______________________________ test_div_except ________________________________

    def test_div_except():
>       c.clear()

test_a11.py:99: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
__________________________________ test_push ___________________________________

    def test_push():
>       c.clear()

test_a11.py:109: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________________________ test_ln1[1] __________________________________

input_data = 1

    @pytest.mark.parametrize('input_data',[(i) for i in range(1,10)])
    def test_ln1(input_data):
>       c.clear()

test_a11.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________________________ test_ln1[2] __________________________________

input_data = 2

    @pytest.mark.parametrize('input_data',[(i) for i in range(1,10)])
    def test_ln1(input_data):
>       c.clear()

test_a11.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________________________ test_ln1[3] __________________________________

input_data = 3

    @pytest.mark.parametrize('input_data',[(i) for i in range(1,10)])
    def test_ln1(input_data):
>       c.clear()

test_a11.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________________________ test_ln1[4] __________________________________

input_data = 4

    @pytest.mark.parametrize('input_data',[(i) for i in range(1,10)])
    def test_ln1(input_data):
>       c.clear()

test_a11.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________________________ test_ln1[5] __________________________________

input_data = 5

    @pytest.mark.parametrize('input_data',[(i) for i in range(1,10)])
    def test_ln1(input_data):
>       c.clear()

test_a11.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________________________ test_ln1[6] __________________________________

input_data = 6

    @pytest.mark.parametrize('input_data',[(i) for i in range(1,10)])
    def test_ln1(input_data):
>       c.clear()

test_a11.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________________________ test_ln1[7] __________________________________

input_data = 7

    @pytest.mark.parametrize('input_data',[(i) for i in range(1,10)])
    def test_ln1(input_data):
>       c.clear()

test_a11.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________________________ test_ln1[8] __________________________________

input_data = 8

    @pytest.mark.parametrize('input_data',[(i) for i in range(1,10)])
    def test_ln1(input_data):
>       c.clear()

test_a11.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_________________________________ test_ln1[9] __________________________________

input_data = 9

    @pytest.mark.parametrize('input_data',[(i) for i in range(1,10)])
    def test_ln1(input_data):
>       c.clear()

test_a11.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_exp[input_data0] _____________________________

input_data = (-9, -9)

    @pytest.mark.parametrize("input_data",data)
    def test_exp(input_data):
>       c.clear()

test_a11.py:126: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_exp[input_data1] _____________________________

input_data = (-5, -5)

    @pytest.mark.parametrize("input_data",data)
    def test_exp(input_data):
>       c.clear()

test_a11.py:126: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_exp[input_data2] _____________________________

input_data = (-1, -1)

    @pytest.mark.parametrize("input_data",data)
    def test_exp(input_data):
>       c.clear()

test_a11.py:126: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_exp[input_data3] _____________________________

input_data = (3, 3)

    @pytest.mark.parametrize("input_data",data)
    def test_exp(input_data):
>       c.clear()

test_a11.py:126: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________ test_exp[input_data4] _____________________________

input_data = (7, 7)

    @pytest.mark.parametrize("input_data",data)
    def test_exp(input_data):
>       c.clear()

test_a11.py:126: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
____________________________________ test_e ____________________________________

    def test_e():
>       c.clear()

test_a11.py:133: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
________________________________ test_ln_except ________________________________

    def test_ln_except():
>       c.clear()

test_a11.py:138: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
_______________________________ test_add_except ________________________________

    def test_add_except():
>       c.clear()

test_a11.py:147: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
a11.py:148: in clear
    self.clear()
a11.py:148: in clear
    self.clear()
E   RecursionError: maximum recursion depth exceeded
!!! Recursion detected (same locals & position)
=========================== short test summary info ============================
FAILED test_a11.py::test_check_number[-3--1-10] - Failed: DID NOT RAISE <clas...
FAILED test_a11.py::test_check_number[-2--1-10] - Failed: DID NOT RAISE <clas...
FAILED test_a11.py::test_date_syntax2[12/03] - AssertionError: Regex pattern ...
FAILED test_a11.py::test_date_syntax2[12/03/abcd] - ValueError
FAILED test_a11.py::test_date_syntax2[12/3/2000] - Failed: DID NOT RAISE <cla...
FAILED test_a11.py::test_date_syntax2[12/3/45] - Failed: DID NOT RAISE <class...
FAILED test_a11.py::test_date_syntax2[1/23/2003] - Failed: DID NOT RAISE <cla...
FAILED test_a11.py::test_date_syntax2[11-22/2003] - AssertionError: Regex pat...
FAILED test_a11.py::test_date_syntax3[00/02/2002-0-Month] - Failed: DID NOT R...
FAILED test_a11.py::test_date_syntax3[33/02/2002-33-Month] - Failed: DID NOT ...
FAILED test_a11.py::test_date_syntax3[01/00/2002-0-Day] - Failed: DID NOT RAI...
FAILED test_a11.py::test_date_syntax3[01/33/2002-33-Day] - Failed: DID NOT RA...
FAILED test_a11.py::test_date_syntax3[01-01-1800-1800-Year] - Failed: DID NOT...
FAILED test_a11.py::test_date_syntax3[01-01-2022-2022-Year] - Failed: DID NOT...
FAILED test_a11.py::test_plus[input_data0] - RecursionError: maximum recursio...
FAILED test_a11.py::test_plus[input_data1] - RecursionError: maximum recursio...
FAILED test_a11.py::test_plus[input_data2] - RecursionError: maximum recursio...
FAILED test_a11.py::test_plus[input_data3] - RecursionError: maximum recursio...
FAILED test_a11.py::test_plus[input_data4] - RecursionError: maximum recursio...
FAILED test_a11.py::test_minus[input_data0] - RecursionError: maximum recursi...
FAILED test_a11.py::test_minus[input_data1] - RecursionError: maximum recursi...
FAILED test_a11.py::test_minus[input_data2] - RecursionError: maximum recursi...
FAILED test_a11.py::test_minus[input_data3] - RecursionError: maximum recursi...
FAILED test_a11.py::test_minus[input_data4] - RecursionError: maximum recursi...
FAILED test_a11.py::test_mult[input_data0] - RecursionError: maximum recursio...
FAILED test_a11.py::test_mult[input_data1] - RecursionError: maximum recursio...
FAILED test_a11.py::test_mult[input_data2] - RecursionError: maximum recursio...
FAILED test_a11.py::test_mult[input_data3] - RecursionError: maximum recursio...
FAILED test_a11.py::test_mult[input_data4] - RecursionError: maximum recursio...
FAILED test_a11.py::test_div[input_data0] - RecursionError: maximum recursion...
FAILED test_a11.py::test_div[input_data1] - RecursionError: maximum recursion...
FAILED test_a11.py::test_div[input_data2] - RecursionError: maximum recursion...
FAILED test_a11.py::test_div[input_data3] - RecursionError: maximum recursion...
FAILED test_a11.py::test_div[input_data4] - RecursionError: maximum recursion...
FAILED test_a11.py::test_div_except - RecursionError: maximum recursion depth...
FAILED test_a11.py::test_push - RecursionError: maximum recursion depth exceeded
FAILED test_a11.py::test_ln1[1] - RecursionError: maximum recursion depth exc...
FAILED test_a11.py::test_ln1[2] - RecursionError: maximum recursion depth exc...
FAILED test_a11.py::test_ln1[3] - RecursionError: maximum recursion depth exc...
FAILED test_a11.py::test_ln1[4] - RecursionError: maximum recursion depth exc...
FAILED test_a11.py::test_ln1[5] - RecursionError: maximum recursion depth exc...
FAILED test_a11.py::test_ln1[6] - RecursionError: maximum recursion depth exc...
FAILED test_a11.py::test_ln1[7] - RecursionError: maximum recursion depth exc...
FAILED test_a11.py::test_ln1[8] - RecursionError: maximum recursion depth exc...
FAILED test_a11.py::test_ln1[9] - RecursionError: maximum recursion depth exc...
FAILED test_a11.py::test_exp[input_data0] - RecursionError: maximum recursion...
FAILED test_a11.py::test_exp[input_data1] - RecursionError: maximum recursion...
FAILED test_a11.py::test_exp[input_data2] - RecursionError: maximum recursion...
FAILED test_a11.py::test_exp[input_data3] - RecursionError: maximum recursion...
FAILED test_a11.py::test_exp[input_data4] - RecursionError: maximum recursion...
FAILED test_a11.py::test_e - RecursionError: maximum recursion depth exceeded
FAILED test_a11.py::test_ln_except - RecursionError: maximum recursion depth ...
FAILED test_a11.py::test_add_except - RecursionError: maximum recursion depth...
======================== 53 failed, 15 passed in 0.74s =========================

```