from decimal import Decimal, getcontext

getcontext().prec = 4
print(Decimal(1) / Decimal(7))