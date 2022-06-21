import arithmetic.add
import arithmetic.sub as sub

from arithmetic.mul import mul
from arithmetic import dev

def letscook(x, y, oper):
    r = 0
    if oper == "+":
        r = arithmetic.add.add(x, y)

    elif oper == "-":
        r = sub.sub(x, y)

    elif oper == "*":
        r = mul(x, y)
        
    else:
        r = dev.dev(x, y)

    print("{} {} {} = {}".format(x, oper, y, r))

x, y = 3, 8

letscook(x, y, "+")
letscook(x, y, "-")
letscook(x, y, "*")
letscook(x, y, "/")