def gt(n):
    if n<2:
        return 1
    else:
        return n*gt(n-1)

print(gt(4))