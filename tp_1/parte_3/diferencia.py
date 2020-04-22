def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    diff_z = z1 - z2
    return dif_x, dif_y, diff_z

# Agregar pruebas
assert diferencia(16, -72, -52,55, 90, -31) == (-39, -162, -21)
assert diferencia(55, -88, -75, 38, 62, -12) == (17, -150, -63)
assert diferencia(1, 2, 3, 1, 2, 3) == (0, 0, 0)