def min_dist(D1: [float], D2: [float]) -> float:
    """
    Time complexity: O(NlogM)
    """
    if D1 == None or D2 == None or len(D1) == 0 or len(D2) == 0:
        return 0
    if len(D1) < len(D2):
        temp = D1
        D1 = D2
        D2 = temp

    D2 = sorted(D2)
    res = float('inf')
    for x in D1:
        start, end = 0, len(D2) - 1
        while start < end:
            mid = int(start + (end - start) / 2)
            if D2[mid] < x:
                start = mid + 1
            else:
                end = mid
        dist = abs(D2[start] - x) if start < len(D2) else float('inf')
        dist = min(dist, abs(D2[start - 1] - x)) if start > 0 else dist
        res = min(res, dist)
    return res

if __name__ == '__main__':
    assert min_dist([1, 2, 3, 4], [1, 2, 3, 4]) == 0
    assert min_dist([1, 3, 5, 7, 9], [2, 6, 8]) == 1
    assert min_dist([5, 1.2, 8], [-3, 2, 6]) == 0.8
    assert min_dist([5, 1, 8.7], [-3, 2, 6]) == 1
    assert min_dist([5, -1.2, 8], [float('inf')]) == float('inf')
    assert min_dist([5, -1.2, 8], [-float('inf')]) == float('inf')
    assert min_dist([-float('inf')], [-float('inf')]) == float('inf')

