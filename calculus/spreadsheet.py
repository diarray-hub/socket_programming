from collections.abc import Iterable

# A dict describing every functions in the Calculus class
DESCRIPTIONS = [
    "1: factorial(n: int) -> int: Returns the factorial of the given n (mathematically: n!).\n",
    "2: catalan(n: int) -> int: Returns the n-th number of the Catalan sequence.\n",
    "3: floor(n: float) -> int: Returns the floor of n as an integral.\n",
    "4: ceil(n: float) -> int: Returns the ceiling of n as an integral.\n",
    "5: are_divisible(num1: int | float, num2: int | float) -> bool: Returns whether or not num1 is divisible by num2.\n",
    "6: list_div(n: int) -> list: Returns a list of all divisors of n.\n",
    "7: is_prime(n: int) -> bool: Returns whether or not n is a prime number.\n",
    "8: primelist(n: int) -> list: Returns a list of all prime numbers less than or equal to n.\n",
    "9: digitsum(n: int| float) -> int: Returns the sum of all the digits in a given number n.\n",
    "10: all_negative(iterable: Iterable) -> bool: Returns True if all items in an iterable are negative numbers.\n",
    "11: all_positive(iterable: Iterable) -> bool: Returns True if all items in an iterable are positive numbers.\n",
    "12: all_null(iterable: Iterable) -> bool: Returns True if all items in an iterable are null.\n",
    "13: Zeller_algorithm(day: int, month: int, year: int) -> str: Returns the week day of a given date.\n",
    "14: gcd(a: int, b: int) -> int: Returns the greatest common divisor between a and b.\n",
    "15: lcm(a, b) -> int: Returns the least common multiple between a and b.\n"
]

# Group all the function in a utility class
class Calculus:
    @staticmethod
    def factorial(n: int) -> int:
        """This function will return the factorial of the given n (mathematically: n!)

        Args:
            n (int): A positive integer to compute its factorial 

        Returns:
            int: factorial of n (n!)
        """
        assert n >= 0, "Argument for this function should be a positive integer"
        if n < 2:
            # Return 1 if n = 0 or 1
            return 1
        factorial = 1
        for ints in range(2, n+1):
            factorial *= ints
        return factorial
    
    @staticmethod
    def catalan(n: int) -> int:
        """This function will return the catalan number corresponding to the given n.
        In combinatorial mathematics, the Catalan numbers are a sequence of natural numbers that occur in various counting problems, 
        often involving recursively defined objects. They are named after the French-Belgian mathematician Eugène Charles Catalan.

        Args:
            n (int): A positive integer to compute its factorial

        Returns:
            int: n th number of the catalan sequence
        """
        # This is the formula to compute the n th number in the the catalan sequence for a give n
        return Calculus.factorial(n=2*n) / (Calculus.factorial(n=n+1) * Calculus.factorial(n=n))
    
    @staticmethod
    def floor(n: float) -> int:
        """Returns the floor of n as an Integral.
        This is the largest integer <= n.

        Args:
            n (float): Any positive or negative float number 

        Returns:
            int: floor of n
        """
        assert isinstance(n, float), "For this function, n should be a floating point number"
        if n >= 0 or int(n) - n == 0:
            # Return the integer part of n if n is positive or is a rounded negative number like -3.0
            return int(n)
        return int(n) - 1
    
    @staticmethod
    def ceil(n: float) -> int:
        """Returns the ceiling of n as an Integral.
        This is the smallest integer >= n.

        Args:
            n (float): Any positive or negative float number 

        Returns:
            int: ceiling of n
        """
        assert isinstance(n, float), "For this function, n should be a floating point number"
        if n <= 0 or int(n) - n == 0:
            # Return the integer part of n if n is negative or is a rounded positive number like 3.0
            return int(n)
        return int(n) + 1
    
    @staticmethod
    def are_divisible(num1: int | float, num2: int | float) -> bool:
        """Returns whether or not num1 is divisible by num2

        Args:
            num1 (int | float): The number to be divided
            num2 (int | float): The number to divide num1 by

        Returns:
            bool: The corresponding boolean value
        """
        if num1 % num2 != 0:
            return False
        return True
    
    @staticmethod
    def list_div(n: int) -> list:
        """Returns a list of all divisors of n

        Args:
            n (int): Any positive integer

        Returns:
            list: All the divisors of n in in python list
        """
        assert isinstance(n, int), "Argument for this function should be an integer"
        listdiv = []
        for i in range(1,(n//2) + 1):
            if Calculus.are_divisible(num1=n, num2=i):
                listdiv.append(i)
        listdiv.append(n)
        return listdiv

    @staticmethod
    def is_prime(n: int) -> bool:
        """Returns whether or not n is a prime number

        Args:
            n (int): Any positive integer

        Returns:
            bool: The corresponding boolean value
        """
        assert isinstance(n, int) and n > 1, "Argument for this function should be an integer greater than 1"
        if(len(Calculus.list_div(n)) == 2):
            return True
        return False

    @staticmethod
    def primelist(n: int) -> list:
        """Returns a list of all prme numbers less than or equal to n

        Args:
            n (int): Any positive integer

        Returns:
            list: All the prime numbers less than or equal to n in in python list
        """
        list_primes = []
        for i in range(2, n+1):
            if Calculus.is_prime(i):
                list_primes.append(i)
        return list_primes

    @staticmethod
    def digitsum(n: int| float) -> int:
        """Returns the sum of all the digits in a given number n
        To avoid any RecursionError this integer should be a non negative value

        Args:
            n (int| float): Any positive number

        Returns:
            int: Sum of the digits, exemple 10 if 64 given
        """
        assert n >= 0, "This function can't be called with a negative value" 
        if n//10 == 0:
            return n
        return n%10 + Calculus.digitsum(n//10)

    @staticmethod
    def all_negative(iterable: Iterable) -> bool:
        """Returns True if all items in an iterable are negative numbers

        Args:
            iterable (Iterable): Any python iterable (list, tuple etc...)

        Returns:
            bool: The corresponding Boolean value
        """
        for item in iterable:
            if item > 0:
                return False
        return True

    @staticmethod
    def all_positive(iterable: Iterable) -> bool:
        """Returns True if all items in an iterable are positive numbers

        Args:
            iterable (Iterable): Any python iterable (list, tuple etc...)

        Returns:
            bool: The corresponding Boolean value
        """
        for item in iterable:
            if item < 0:
                return False
        return True
    
    @staticmethod
    def all_null(iterable: Iterable) -> bool:
        """Returns True if all items in an iterable are null

        Args:
            iterable (Iterable): Any python iterable (list, tuple etc...)

        Returns:
            bool: The corresponding Boolean value
        """
        return True if Calculus.all_negative(iterable=iterable) and Calculus.all_positive(iterable=iterable) else False

    @staticmethod
    def Zeller_algorithm(day: int, month: int, year: int):
        """Returns the week day of a given date 
        
        These formulas are based on the observation that the day of the week progresses in a predictable manner 
        based upon each subpart of that date. Each term within the formula is used to calculate the offset needed to obtain the correct day of the week.
        Zeller's algorithm is an well known algorithm created by Cristian Zeller
        which permit to find the day of the week corresponding to a given date
        the original formula of Zeller look like below:
        day_of_week = (d + floor(13 * (m + 1) / 5) + y + floor(y / 4) - floor(y / 100) + floor(y / 400)) % 7
        where floor(x) mimic a function whom round the nearest integer less or equal to x (the base number or integer part).
        In python we've got the built-in module function math.floor.
        Note that some details are changed in my interpretation of Zeller's algo
        In the original algo mapping look like below after Gregorian calendar
            0:Saturday
            ...
            ...
            6:Friday
        In mine, I will manage to get a natural ISO-day mapping like
            1:Monday
            ...
            ...
            7:Sunday 
        """
        week_days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
        
        twodigits = str(year)
        if (len(twodigits) == 2): 
            """If the given year has a number of digits less than 3 then we will add 1900 to it
            since day of the week repeats in a fixed cycle of 7 days, so adding or subtracting 
            a multiple of 7 to the year will not change the day of the week.
            We need to do so cause of century's presence in the formula and cannot get 0 there.
            """
            year += 1900
            
        if (month == 1 or month == 2): #In this algorithm January and February are counted as months 13 and 14 of the previous year
            year -= 1
            month += 12
        year_in_century = year % 100 # year in the century
        century = year // 100   # to find the  zero-based century of the given year
        
        day_of_week = (day + Calculus.floor(2.6 * month + 2.6) + year_in_century + Calculus.floor(year_in_century / 4) + Calculus.floor(century / 4) - 2 * century)% 7
        # to get ISO-day equivalent
        day_of_week = ((day_of_week + 5) % 7) + 1
        return week_days[day_of_week]
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Returns the greatest common divisor between a and b
        
        This function uses Euclid's algorithm to find the greatest common divisor of two numbers a and b. 
        The algorithm repeatedly replaces a with b and b with a % b until b becomes 0. The final value of a is the GCD."""
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Returns the least common multiple between a and b
        
        This function calculates the least common multiple using the relationship between GCD and LCM. 
        It uses the formula: LCM(a, b) = |a * b| / GCD(a, b), and it includes a check to handle cases where one or both of the numbers are zero."""
        return abs(a * b) // Calculus.gcd(a, b) if a and b else 0
