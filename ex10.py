def fun_par(l):
    par = []
    for n in l:
        if n % 2 == 0:
            par.append(n)
    return par
print(fun_par([12,6,8,10,46,44]))