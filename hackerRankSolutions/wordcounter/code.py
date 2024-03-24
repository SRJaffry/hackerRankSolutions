# Problem URL : https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

n = int(input())

word_list = [input().lower() for _ in range(n)]

word_counter = Counter(word_list)

print(len(word_counter.keys()))
print(*word_counter.values())