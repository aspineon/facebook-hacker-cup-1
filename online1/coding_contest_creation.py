import sys

def codingChallenge(dd):
    add = 0
    sel = []
    for d in dd:
        if sel == []:
            sel += [d]
            continue
        d0 = sel[-1]
        if d <= d0:
            add += 4 - len(sel)
            sel = [d]
        elif d > d0 + 10:
            while d > d0 + 10:
                d0 += 10
                sel += [d0]
                add +=1
                if len(sel) >= 4:
                    sel = []
                    break
            sel += [d]
        else:
            sel += [d]
        if len(sel) >= 4:
            sel = []
    res = add
    if len(sel) != 0: 
        res += 4 - len(sel)
    return res

f = open(sys.argv[1], 'r')
num = f.readline().strip()
for i in xrange(1, int(num)+1):
    n = int(f.readline().strip())
    difficulties = map(int, f.readline().strip().split())
    res = codingChallenge(difficulties)
    print 'Case #' + str(i) + ':', res
