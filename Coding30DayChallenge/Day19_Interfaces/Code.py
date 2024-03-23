class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
      
      sqrt_n = int(n**0.5)
      divisors = []
      
      for i in range(1, sqrt_n+1):
        
        if n%i == 0:
          divisors.append(i)
          
          if(i != n):
            divisors.append(n//i)
      
      divisors.sort()      
      divisors_set = set(divisors)
      divisors = list(divisors_set)
      
      return(sum(divisors))


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)