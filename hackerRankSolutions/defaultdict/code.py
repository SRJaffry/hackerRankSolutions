from collections import defaultdict

N, M = map(int, input().split())

A = defaultdict(list)
B = defaultdict(list)

for i in range(N):
    A['list'].append(input())

for i in range(M):
    B['list'].append(input())

idx = []

for i in range(M):

    index_list = []
    word = B['list'][i]
    
    for index, value in enumerate(A['list']):        
        if word == value:
            index_list.append(index)

    if len(index_list) > 0:
        print(*[x+1 for x in index_list])
    else:
        print('-1')


