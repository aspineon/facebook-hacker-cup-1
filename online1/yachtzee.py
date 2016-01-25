import sys

def squareSum(cArr, R):
    sqsum = 0
    csum = 0
    for c in cArr:
        if csum+c <= R:
            sqsum += c * c;
            csum += c
        else:
            sqsum += (R-csum) * (R-csum)
            break
    return sqsum

def yacht(N, A, B, cArr):
    cSum = sum(cArr)
    csqSum = squareSum(cArr, cSum)
    Adiv = A / cSum
    Arem = A % cSum
    Asqsum = squareSum(cArr, Arem)
    Bdiv = B / cSum
    Brem = B % cSum
    Bsqsum = squareSum(cArr, Brem)
    ABdif = Bdiv - Adiv
    return ABdif * csqSum - Asqsum + Bsqsum

f = open(sys.argv[1], 'r')
num = f.readline().strip()
for i in xrange(1, int(num)+1):
    N, A, B = map(int, f.readline().split())
    cArr = map(int, f.readline().split())
    res = yacht(N, A, B, cArr)
    ans = float(res) / 2.0 / float(B-A)
    print 'Case #' + str(i)+ ':', ans

