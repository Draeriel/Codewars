def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        por100 = p0 * percent / 100
        p0 = p0 + por100 + aug
        years += 1
    return years