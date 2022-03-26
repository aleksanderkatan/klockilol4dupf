def honk(x):
    if x <= 0:
        return ""
    return "(HO" + honk(x-1) + "NK)"


print(honk(4))
