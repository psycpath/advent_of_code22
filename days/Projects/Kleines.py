def consecutive_zeros(binary):
    max = 0
    x = 0
    for number in binary:
        if number == 0:
            x += 1
        else:
            if x > max:
                max = x
                x == 0
