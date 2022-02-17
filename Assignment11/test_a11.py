import pytest
import a11
import math

### problem 1
# Note, we've included tests for exceptions
# You need to provide tests for non-exception cases
def test_check_number():
    assert type(a11.check_number(1, 'Month', 1, 12)) == int
    assert a11.check_number(1, 'Month', 1, 12) == 1
    assert a11.check_number(12, 'Month', 1, 12) == 12

def test_date_syntax():
    assert type(a11.parse_date('01/21/2002')) == tuple
    assert a11.parse_date('01/21/2002') == (1, 21, 2002)
    assert a11.parse_date('01-21-2002') == (1, 21, 2002)
    
def test_check_number_exception():
    low = 0
    high = 10
    for i in range(-3,11):
        if i >= low and i <= high:
            assert i == a11.check_number(i,'foo',low,high)
        else:
            with pytest.raises(ValueError, match=f"Invalid foo {i}" ):
                assert i == a11.check_number(i,'foo',low,high)



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
        a11.parse_date(input_str)

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
        a11.parse_date(input_str)


######### Problem 2
# we've included tests for exceptions at the end

c = a11.calc()

def test_work():
    for e in ["c","3","4","+"]:
        result = c.work(e)
    assert result == '7.0'

def test_calc_e():
    c.clear()
    result = c.e()
    assert type(result) == float
    assert result == math.e

def test_calc_ln():
    for i in ['c', 'e', 'ln']:
        result = c.work(i)
    assert result == '1.0'

def test_calc_add():
    for i in ['c', '1', '2', '+']:
        result = c.work(i)
    assert result == '3.0'

def test_calc_mult():
    for i in ['c', '1', '2', '*']:
        result = c.work(i)
    assert result == '2.0'

def test_calc_minus():  
    for i in ['c', '1', '2', '-']:
        result = c.work(i)
    assert result == '-1.0'

def test_calc_div():
    for i in ['c', '1', '2', '/']:
        result = c.work(i)
    assert result == '0.5'

def test_calc_exp():
    for i in ['c', '1', '2', '^']:
        result = c.work(i)
    assert result == '1.0'

def test_push():
    c.clear()
    c.push(0)
    assert type(c.s.s) == list
    assert type(c.s.s[0]) == float
    c.clear()
    assert c.s.s == []

data = list(zip(range(-10,10),range(-10,10)))

def test_div_except():
    c.clear()
    c.push(3)
    c.push(1.0)
    c.push(0.0)
    s = str(c)
    with pytest.raises(ZeroDivisionError,match='division by zero'):
        c.div()
    assert s == str(c)
  
def test_push_except():
    c.clear()
    c.push(3)
    c.push(4)
    s = str(c)
    v = 'ab'
    with pytest.raises(ValueError, match =f"could not convert string to float: '{v}'"):
        c.push(v)
    assert s == str(c)

def test_ln_except():
    c.clear()
    c.push(7)
    c.push(0)
    s = str(c)
    with pytest.raises(ValueError, match="math domain error"):
        c.ln()
    assert s == str(c)

def test_add_except():
    c.clear()
    c.push(7)
    s = str(c)
    with pytest.raises(IndexError,match="list index out of range"):
        c.add()
    assert str(c) == s