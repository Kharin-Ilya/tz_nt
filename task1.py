import sys

n, m = int(sys.argv[1]), int(sys.argv[2])
k = 1
while True:
    print(k, end='')
    k = 1 + (k + m - 2) % n
    if k == 1:
        break    
print()