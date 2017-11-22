def tickets(people):
    print(people)
    dinero25 = 0
    dinero50 = 0
    dinero100 = 0
    for i in people:
        if i == 25:
            dinero25 += 1
        if i == 50:
            if dinero25 >= 1:
                dinero25 -= 1
                dinero50 += 1
            else:
                return "NO"
        if i == 100:
            if dinero25 >= 1 and dinero50 >= 1:
                dinero25 -= 2
                dinero50 -= 1
                dinero100 += 1
            elif dinero25 >= 3:
                dinero25 -= 4
                dinero100 += 1
            else:
                return "NO"
    return "YES"