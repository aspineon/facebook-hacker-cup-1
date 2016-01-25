import sys
def priceIsCorrect(moneys, target):
    count = 0
    for i in xrange(len(moneys)):
        currSum = 0
        if moneys[i] + currSum <= target:
            currSum += moneys[i]
            count += 1
        else:
            continue
        for j in xrange(i+1, len(moneys)):
            if moneys[j] + currSum <= target:
                currSum += moneys[j]
                count += 1
            else:
                break
    return count

f = open("the_price_is_correct_example_input.txt", "r")
num = f.readline().strip()
for i in xrange(1, int(num)+1):
    target = int(f.readline().strip().split()[1])
    moneys = map(int, f.readline().strip().split())
    count = priceIsCorrect(moneys, target)
    print "Case #%s: %s" % (i, count)

