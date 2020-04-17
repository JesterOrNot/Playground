from math import log
from typing import Callable, Type


def interest_equation(func: Callable[[Type, float, float, float, float], float]) -> Callable[[Type, float, float, float, float], float]:
    def inner(cls, a, b, c, d) -> float:
        return round(func(cls, a, b, c, d), 2)
    return inner

class Interest:
    """
    P=principle

    r=rate

    t=time

    A = Value of investment

    n = number of times to calculate
        Anually n=1
        semi-anually n=2
        quarterly n=4
        monthly n=12
        weekly n=52
        daily n=365
    """

    @classmethod
    def get_solver(cls, variable: str) -> Callable[[float, float, float, float], float]:
        missing_var = variable.lower()
        if missing_var == 'a':
            return cls.compound_interest_a
        elif missing_var == 'p':
            return cls.compound_interest_p
        elif missing_var == 't':
            return cls.compound_interest_t
        elif missing_var == 'r':
            return cls.compound_interest_r
        else:
            raise ValueError("Invalid variable name")

    @staticmethod
    @interest_equation
    def compound_interest_a(cls, P: float, r: float, n: float, t: float) -> float:
        return P*(1+(r/n))**(t*n)

    @staticmethod
    @interest_equation
    def compound_interest_p(cls, A: float, r: float, n: float, t: float) -> float:
        return A / (1 + r/n)**(n*t)

    @staticmethod
    @interest_equation
    def compound_interest_r(cls, A: float, P: float, n: float, t: float) -> float:
        return log((A/P)**(1/(n*t))-1)

    @staticmethod
    @interest_equation
    def compound_interest_t(cls, A: float, P: float, n: float, r: float) -> float:
        return log(A/P) / (n * log(1 + r / n))

    @staticmethod
    def get_equation_a(cls, P: float, r: float, n: float, t: float) -> str:
        return "A = {}*(1+{}/{})**({}*{})".format(P, r, n, t, n)


if __name__ == "__main__":
    app = Interest()
    solver = app.get_solver('a')
    print(solver(3300, 0.22, 1, 3))
