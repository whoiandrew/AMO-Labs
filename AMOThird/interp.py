def lagr(arr_xs, arr_ys, x):
    res = 0
    for i in range(len(arr_xs)):
        pr = 1
        for j in range(len(arr_xs)):
            if i != j:
                pr *= ((x-arr_xs[j])/(arr_xs[i] - arr_xs[j]))
        res += pr*arr_ys[i]
    return res







