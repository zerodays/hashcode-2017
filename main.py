V, E, R, C, X = [int(i) for i in input().split()]
videos = list(map(int, input().split()))
endpoints = []
requests = [list() for i in range(E)]
to_dc = []


for i in range(E):
    Ld, K = [int(j) for j in input().split()]
    temp = [0 for i in range(K)]
    for j in range(K):
        c, Lc = [int(_) for _ in input().split()]
        temp[j] = (c, Lc)
    endpoints.append(temp)
    to_dc.append(Ld)

for i in range(R):
    Rv, Re, Rn = [int(_) for _ in input().split()]
    requests[Re].append((Rv, Rn))
