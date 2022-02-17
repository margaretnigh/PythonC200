### Problem 1

def check_number(i,msg,low,high):
    """
    Checks that integer i is in correct range  low..high (inclusive)
    i (int) the number
    msg (s) error message fragment (one of 'Month', 'Day', or 'Year')
    low (int) low end of range
    high (int) high end of range

    returns i or raises Error(...)
    """
    while True:
        if i >= low and i <= high:
            return i
        else:
            #raise error
            return msg
    pass


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
                raise ValueError
        else:
            #not correct format
            raise SyntaxError

if __name__ == '__main__':
    while True:
        try:
            s = input("Input a date: ")
            if s and s[0] == 'q':  # quit
                break
            print(parse_date(s))
        except SyntaxError as e:
            print(e)
            pass
        except ValueError as e:
            print(e)
            pass

### Problem 2

import math

class stack:
    def __init__(self):
        self.s = []

    def pop(self):
        top = self.s[0]
        self.s = self.s[1:]
        return top

    def push(self,item):
        self.s = [item] + self.s

    def empty(self):
        return self.s == []

    def peek(self):
        return self.s[0] if len(self.s) else None
        
    def __str__(self):
        return str(self.s)
        
class calc:
    def __init__(self):
        self.s = stack()

    def _op1(self,f):
        # f is a function that takes one operand
        # apply f to top item in stack.
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on
        a = self.s.s[0:]
        try:
            top = self.s.pop()
            self.push(f(top))
            return self.s.s[0]
        except Exception as e:
            self.s = a
            print(self.s)
            raise e
        


    def _op2(self,f):
        # f is a function that takes two operands
        # apply f to top two items in stack.  top 
        # element is first argument, second element is second argument
        # in the event of an exception, leave the
        # stack unchanged and pass the exception on
        a = self.s.s[0:]
        try:
            top = self.s.pop()
            sec  = self.s.pop()
            self.push(f(top,sec))
            return self.s.s[0]
        except Exception as e:
            self.s = a
            raise e

    def clear(self):
        # clear the stack
        self.clear() 

    def e(self):
        # push math.e on stack
        self.s.push(math.e)
        return self.s.s[0]

    def ln(self):
        # compute math.log(top of stack) (see math module)
        # use _op1
        return self._op2(lambda x: math.log(x))

    def add(self):
        # add top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x, y: x + y)
        pass

    def div(self):
        # divide top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x, y: x / y)
        pass

    def mult(self):
        # multiply top two elements on stack 
        # use _op2
        # return top element or exception
        return self._op2(lambda x, y: x * y)
        pass

    def minus(self):
        # subtract top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x, y: x - y)
        pass

    def exp(self):
        # compute x**y with top two elements on stack 
        # use _op2 
        # return top element or exception
        return self._op2(lambda x, y: y**x)
    
    def push(self,data):
        # push float(data) onto stack
        a = self.s
        try:
            data = float(data)
        except Exception as e:
            self.s = a
            raise e
        else:
            self.s.push(data)

    def work(self,data):
        try:
            if data == 'c':
                self.clear()
                return "Starting new computation"
            elif data == 'e':
                return str(self.e())
            elif data == 'ln':
                return str(self.ln())
            elif data == '+':
                return str(self.add())
            elif data == '-':
                return str(self.minus())
            elif data == '*':
                return str(self.mult())
            elif data == '/':
                return str(self.div())
            elif data == '^':
                return str(self.exp())
            else:
                str(self.push(data))
        except Exception as e:
            return str(e)
    
    def __str__(self):
        return str(self.s)

if __name__ == "__main__":
    i = 0
    w = calc()
    while True:
        # uncomment the following to help debugging
        # print(w)
        data = input(f"{i}: ").strip()
        if data == 'q':
            print('Terminated')
            break
        else:
            result = w.work(data)
            if result != None:
                print(result)
        i = 0 if data == 'c' else i+1   