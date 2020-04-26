class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        s = 1
        if(n==1):
            return 1
        else:
            limit = int(n/2) + 1
            for i in range(2, limit):
                if(n%i==0):
                    s = s+i
            return s+n
        pass


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
