##Find the Mean


def mean(L1,l):
    mean1 = 0
    mean2 = 0
    try:
        sum1 = 0
        for j in L1:
            sum1 += j
        mean1 = sum1/len(L1)

        sum2 = 0
        for h in l:
            sum2 += h
        mean2 = sum2/len(l)
    except (ZeroDivisionError, IndexError):
        sum1 = 0
        for j in L1:
            sum1 += j
        mean1 = sum1 / len(L1)
        return mean1, mean2

