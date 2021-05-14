class Expression:
    pass


class Times(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + " * " + str(self.right) + ")"


class Plus(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + " + " + str(self.right) + ")"


class Const(Expression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Var(Expression):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name



e1 = Times(Const(3), Plus(Var("y"), Var("x")))
#                *                        +
#              /   \                    /   \
#             3    (y + x)             y     x

e2 = Plus(Times(Const(3), Var("y")), Var("x"))
#                +                        *
#              /   \                    /   \
#        (3 * y)    x                  3     y

print(e1)
print(e2)


env = {"x": 2, "y": 4}
print(eval(str(e1), env))
print(eval(str(e2), env))

