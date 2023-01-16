H,M = map(int,input().split())
T = H*60 + M +int(input())
print(T//60%24, T%60)