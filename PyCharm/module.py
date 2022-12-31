def del1(type="even"):
    def del2(b):
        if type == 'even':
            b = [num for idx, num  in enumerate(b) if num % 2 != 0]
            return b
        else:
            b = [num for idx, num in enumerate(b) if num % 2 == 0]
            return b
    return del2