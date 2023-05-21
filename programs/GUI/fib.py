def series_list(user_input):
    num = int(user_input)
    series = []
    a = 1
    b = 0
    for i in range(num):
        c = a + b
        a = b
        b = c
        series.append(a)
    return series


print(series_list(0))
