def calculator(a, b, c):
    result = {}
    
    result[1] = ((b * b) - (4 * a * c)) / (2 * a)
    result[2] = ((b * b) - (4 * a * c)) // (2 * a)
    result[3] = (b * b - 4 * a * c) / (2 * a)
    result[4] =  b * b - 4 * a * c / 2 * a
    result[5] = (b * b) - (4 * a * c / 2 * a)
    result[6] =  1 / 2 * b
    result[7] = b / 2

    for k,v in result.items():
        print(f'Calculo {k} = {v}')
    
calculator(10.0, 100.0, 1000.0)