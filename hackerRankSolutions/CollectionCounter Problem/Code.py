# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())

Lshoes = list(map(int, input().split()))

N = int(input())

earnings = 0;

Shoes_Counter = Counter(Lshoes)
AvailableShoeSizes = list(Shoes_Counter.keys())

for i in range(N):
    Customer_offer = list(map(int, input().split()))

    if Customer_offer[0] in AvailableShoeSizes and Shoes_Counter[Customer_offer[0]] > 0:
        earnings += Customer_offer[1]
        Shoes_Counter[Customer_offer[0]] -= 1
        
    
print(earnings)

