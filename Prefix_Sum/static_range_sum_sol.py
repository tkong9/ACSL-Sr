def psum(a):
    psum = [0]
    for num in a:
        psum.append(psum[-1] + num)  # psum[-1] is the last element in the list
    return psum


N, Q = map(int, input().split())
a = list(map(int, input().split()))
p = psum(a)

for i in range(Q):
    l, r = map(int, input().split())
    print(p[r] - p[l])