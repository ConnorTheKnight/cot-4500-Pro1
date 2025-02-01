# cot-4500-Pro1
Compiling via the terminal:
    On windows this program can be compiled using the command:
        python src/main/assignment1.py
    On Mac/Linux this program can be compiled using the command:
        python src/main/assignment1.py
Input formatting:
Each algorithm has their own input formatting requirements each lited below

    Algorithm 1 : Approximation Algorithm For Square Root of 2
        the 1st line of the input should be the digit 1
        the 2nd line of the input should be an initial value greater than the square root of 2 formatted as a float
        the 3rd of the input line should be the tolerance formatted as a float

        Example:
        with the inital value of 12 and a tolerance of 0.001 the input would be:
            1
            12
            0.001

    Algorithm 2 : The Bisection Method for finding the roots of a polynomial
        the 1st line of the input should be the digit 2
        the 2nd line of the input should be the x value of a point A formatted as a float
        the 3rd line of the input should be the x value of a point B such that F(A) and F(B) do not have the same sign formatted as a float
        the 4th line of the input should be the tolerance formatted as a float
        the 5th line of the input should be the maximum number of iterations for this algorithm to run formatted as a positive integer
        the 6th line of the input should be the number of terms in the polynomial k formatted as a postive integer
        the next k pairs of lines of the input will provide the information for each term of the polynomial
            the first line of each pair should be the coefficient of each term formatted as a float
            the second line of each pair should be the exponent of that term of the polynomial

        Example:
        with an A value of -1, a B value of 1, a tolerance of 0.001, a maximum number of iterations of 100, on the polynomial x^7+3x^2+3 the input would be:
            2
            -1
            1
            0.001
            100
            3
            1
            7
            3
            2
            3
            0
        
    Algorithm 3 : Fixed-Point Iteration on a Polynomial
        the 1st line of the input should be the digit 3
        the 2nd line of the input should be an initial approximation formatted as a float
        the 3rd line of the input should be the tolerance formatted as a float
        the 4th line of the input should be the maximum number of iterations for this algorithm to run formatted as a positive integer
        the 5th line of the input should be the number of terms in the polynomial k formatted as a postive integer
        the next k pairs of lines of the input will provide the information for each term of the polynomial
            the first line of each pair should be the coefficient of each term formatted as a float
            the second line of each pair should be the exponent of that term of the polynomial

        Example:
        with an initial approximation of 1, a tolerance of 0.001, a maximum number of iterations of 100, on the polynomial x^2+4 the input would be:
            3
            1
            0.001
            100
            2
            1
            2
            4
            0
        
    Algorithm 4 : The Newton-Raphson Method 
        the 1st line of the input should be the digit 4
        the 2nd line of the input should be the x value of an estimated point close to the root formatted as a float
        the 3rd line of the input should be the tolerance formatted as a float
        the 4th line of the input should be the maximum number of iterations for this algorithm to run formatted as a positive integer
        the 5th line of the input should be the number of terms in the polynomial k formatted as a postive integer
        the next k pairs of lines of the input will provide the information for each term of the polynomial
            the first line of each pair should be the coefficient of each term formatted as a float
            the second line of each pair should be the exponent of that term of the polynomial
        
        Example:
        with an initial approximation of 5, a tolerance of 0.001, a maximum number of iterations of 100, on the polynomial x^7+3x^0.5+3 the input would be:
            4
            5
            0.001
            100
            3
            1
            7
            3
            0.5
            3
            0
Using requirements.txt
    This program uses no third party libraries to run, so this file can be left empty
