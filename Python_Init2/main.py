import arithmetic as arith

def letscook(x, y, oper):
    r = 0
    if oper == "+":
        r = arith.add(x, y)

    elif oper == "-":
        r = arith.sub(x, y)

    elif oper == "*":
        r = arith.mul(x, y)
        
    else:
        r = arith.dev(x, y)

    print("{} {} {} = {}".format(x, oper, y, r))

x, y = 3, 8

letscook(x, y, "+")
letscook(x, y, "-")
letscook(x, y, "*")
letscook(x, y, "/")