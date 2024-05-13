def prod_non_zero_diag(x):
    res = 1
    for i in range(min(len(x), len(x[0]))):
        if x[i][i] != 0:
            res *= x[i][i]
    return res


def are_multisets_equal(x, y):
    return sorted(x) == sorted(y)


def max_after_zero(x):
    ind = -1
    for i in range(len(x) - 1):
        if x[i] == 0 and (ind == -1 or x[i + 1] > x[ind]):
            ind = i + 1
    return -1 if ind == -1 else x[ind]


def convert_image(img, coefs):
    m = []
    for i in range(len(img)):
        m.append([])
        for j in range(len(img[i])):
            m[-1].append(img[i][j][0] * coefs[0] +
                     img[i][j][1] * coefs[1] +
                     img[i][j][2] * coefs[2])
    return m


def run_length_encoding(x):
    ret1 = []
    ret2 = []
    cnt = 1
    x.append(x[-1] + 1)
    for i in range(1, len(x) - 1):
        if x[i] != x[i - 1]:
            ret1.append(x[i - 1])
            ret2.append(cnt)
            cnt = 1
        else:
            cnt += 1
    return ret1, ret2


def pairwise_distance(x, y):
    m = [[0] * len(y) for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y)):
            m[i][j] = ((x[i][0] - y[j][0]) ** 2 + (x[i][1] - y[j][1]) ** 2) ** 0.5
    return m

