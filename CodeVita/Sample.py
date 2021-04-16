T = int(input()) 
for i in range(1, T + 1):
    N, M = [int(s) for s in input().split(" ")]
    print("Case #\{}: {} {}".format(i, N + M, N * M))