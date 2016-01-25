import sys

def ladder(XH):
    cost = 0
    bucket = [XH[0]]
    hmax = XH[0][1]
    for i in xrange(1,len(XH)):
        xi = XH[i][0]
        height = XH[i][1]
        if height > hmax:
            bucket = [XH[i]]
            hmax = XH[i][0]
        else:
            for xh in reversed(bucket):
                if xh[1] > height:
                    break
                elif xh[1] == height:
                    cost += (xi - xh[0]) * (xi - xh[0])
            bucket += [XH[i]]
    return cost % 1000000007

f = open(sys.argv[1], 'r')
num = f.readline().strip()
for idx in xrange(1, int(num)+1):
    N = int(f.readline())
    XH = []
    for n in range(N):
        x, h = map(int, f.readline().split())
        XH += [[x, h]]
    XH.sort(key=lambda x: x[0])
    res = ladder(XH)
    print 'Case #'+str(idx)+':', res

