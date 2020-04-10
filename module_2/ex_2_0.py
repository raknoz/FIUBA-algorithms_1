def main():
    print("Convierte medidas inglesas a sistema metrico")

    millas = int(input("Cuántas millas?: "))
    pies = int(input("Y cuántos pies?: "))
    pulgadas = int(input("Y cuántas pulgadas?: "))

    metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
    print(f"La longitud es de {metros} metros")

main()