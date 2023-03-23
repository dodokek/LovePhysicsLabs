for a in range(-50, 50):
    for b in range(-50, 50):
        for c in range(-50, 50):
            if (2*a*b+b*c+c) == 273:
                if (a*b + b*c - a*c - b) == -70:
                    print(a, b, c)
                    print(a+b+c)