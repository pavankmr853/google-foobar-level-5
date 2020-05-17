def solution(s):
    # Your code here
 import math
import decimal

irrational_number = decimal.Decimal('1.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273')
complement = decimal.Decimal('3.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501')


decimal.getcontext().prec = 100

def sumOfBeattySeq(current_irrational_number, n):
    if n > 0:
        if current_irrational_number > 2:
            return sumOfBeattySeq(irrational_number, n) + (n * (n + 1))
        else:
            m = long(decimal.Decimal(current_irrational_number - 1) * n)


            return (n + m) * (n + m + 1) / 2 - sumOfBeattySeq(complement, m)

    return 0


def solution(n):
    return str(long(sumOfBeattySeq(irrational_number, long(n))))
