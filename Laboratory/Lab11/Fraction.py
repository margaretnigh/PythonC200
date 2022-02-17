
class MyFraction:
    """
    This class allows for the representation of fractions.
    """
    def __init__(self, numerator, denominator):
        """
        This class will make a fraction:
               numerator 
        ---------------------------
              denominator
        """
        self.numerator = numerator
        self.denominator = denominator
        pass

    def evaluate(self):
        """
        This function will return the fraction evaluated into a decimal
        """
        return self.numerator / self.denominator
        pass
    def __add__(self, other):
        """
        Adds 2 fractions together. 
        Handles addition by making the denominators the same.
        a   c           ad + cb
        - + -    <-->   -------
        b   d             bd
        """
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator

        new_num = (a*d + c*b)
        new_denom = (b * d)
        return MyFraction(new_num,new_denom)

        pass
    def __sub__(self, other):
        """
        Subtracts 2 fractions. 
        Handles addition by making the denominators the same.
        a   c           ad - cb
        - - -    <-->   -------
        b   d             bd
        """
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator

        new_num = (a*d - c*b)
        new_denom = (b * d)
        return MyFraction(new_num,new_denom)
        pass

    def __mul__(self, other):
        """
        Multiplies 2 fractions. 
        a   c           a*c
        - * -    <-->   ---
        b   d           b*d
        """
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator

        new_num = (a*c)
        new_denom = (b * d)
        return MyFraction(new_num,new_denom)
        pass

    def __str__(self):
        """
        Makes a fraction representation
        Example:
        f = 4/5
        """
        a = self.numerator
        b = self.denominator
        return str(a) + "/" + str(b)
        pass

    def __eq__(self, other):
        """
        Compare two instance of Fraction to see if they are equal.
        Here we check that the parts are equal rather than using evaluate()
        to demonstrate how you might do this without the 'float' type.
        """
        if self.numerator == other.numerator:
            if self.denominator == other.denominator:
                return True
            else:
                return False
        else:
            return False
        pass


    def __lt__(self, other):
        """
        Compare two instance of Fraction to see if one is less than the other.
        a   b         
        - < -    <-->   ad < bc
        b   c
        if b, d share the same sign, and is
                 <-->   ad > bc
        if b, d have opposite signs.
        
        For more information, see:
            https://math.stackexchange.com/questions/2979431/does-cross-multiply-
always-work-for-inequalities-if-both-denominators-are-both-p
        """
        return self.evaluate() < other.evaluate() 
        pass
    def __le__(self, other):
        """
        Compare two instance of Fraction to see if one is less than or equal the 
other.
        Note that you can conveniently make use of __lt__ and __eq__
        """
        return (self < other) or (self == other)
        pass

    def __gt__(self, other):
        """
        Compare two instance of Fraction to see if one is greater than the other
        Note that you can conveniently make use of __le__
        """
        return not((self < other) or (self == other))
        pass

    def __ge__(self, other):
        """
        Compare two instance of Fraction to see if one is greater than or equal the
other
        Note that you can conveniently make use of __lt__
        """
        return (self > other) or (self == other)
        pass
