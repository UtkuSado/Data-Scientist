K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for i in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, N)

print(results)