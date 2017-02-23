def video_score(tupl):
    return tupl[1]/videos[tupl[0]]

def endpoint_score(i):
    a, b = req_for_endpoints[i][1], len(endpoints[i])
    if a == 0 or b == 0: return 0
    return req_for_endpoints[i][0]/a/b

def cache_score(vid, cache):
    s = 0
    for i in range(E):
        for j in range(len(requests[i])):
            if vid == requests[i][j][0]:
                razdalja = 0
                # for k in range(len(endpoints[i])):
                #     if cache == endpoints[i][k][0]:
                #         razdalja = endpoints[i][k][1]
                #         break
                # if razdalja:
                s += requests[i][j][1]
    return s

# read the data
V, E, R, C, X = [int(i) for i in input().split()]
videos = list(map(int, input().split()))
endpoints = []
requests = [list() for i in range(E)]
to_dc = []
req_for_endpoints = [[0, 0] for i in range(E)]
neki = list(range(E))

for i in range(E):
    Ld, K = [int(j) for j in input().split()]
    temp = [0 for i in range(K)]
    for j in range(K):
        c, Lc = [int(_) for _ in input().split()]
        temp[j] = (c, Lc)
    endpoints.append(sorted(temp, key=lambda x: x[1]))
    to_dc.append(Ld)

for i in range(R):
    Rv, Re, Rn = [int(_) for _ in input().split()]
    requests[Re].append((Rv, Rn))
    req_for_endpoints[Re][0] += Rn
    req_for_endpoints[Re][1] += 1

# sort
for i in range(E):
    requests[i].sort(key=video_score, reverse=True)

# move videos
servers = [[] for i in range(C)]
server_space = [X for i in range(C)]

while True:
    print(len(neki))

    neki.sort(key=endpoint_score)
    while len(neki) > 0 and len(requests[neki[0]]) == 0:
        neki.pop(0)

    if len(neki) == 0: break
    asdf = neki[0]
    vid = requests[asdf].pop(0)

    available = endpoints[asdf]
    ok = False
    avaliable = sorted(zip([cache_score(vid[0], i) for i in available], available))
    avaliable = [i[1] for i in avaliable]

    for serv in available:
        if server_space[serv[0]] >= videos[vid[0]]:
            servers[serv[0]].append(vid[0])
            server_space[serv[0]] -= videos[vid[0]]

            req_for_endpoints[asdf][0] -= vid[1]
            req_for_endpoints[asdf][1] -= 1
            ok = True
            break
    if not ok:
        req_for_endpoints[asdf][0] -= vid[1]
        req_for_endpoints[asdf][1] -= 1


# print
su = sum([bool(i) for i in servers])
print(su)
for i, _ in enumerate(servers):
    if _: print(i, ' '.join(map(str, set(_))))
