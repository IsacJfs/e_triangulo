print("\n", "="*30, "\n")
print("É Triangulo?")
print("Digite três valores numéricos \n\
O programa ira detalhar o triangulo:\n")
l1 = float(input("Primeiro valor: "))
l2 = float(input("Segundo valor: "))
l3 = float(input("Terceiro valor: "))
print("\n", "="*30, "\n")


def e_triangulo(lado1, lado2, lado3):
    # Analisa sé é triangulo e qual o tipo do triângulo
    lados = {lado1, lado2, lado3}  # Foi utilizado a função set para eliminar valores iguais
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        # Algoritmo para determinar se três retas são um triângulo
        print("Os valores correspondem a um Triangulo do tipo:")
    if len(lados) == 1:  # dois valores eliminados, então os três são iguais
        return print("Equilátero - três lados iguais;")
    if len(lados) == 2:  # um valor eliminado, então dois são iguais
        return print("Isósceles - quaisquer dois lados iguais;")
    if len(lados) == 3:  # Nenhum valor eliminado, então três diferentes
        return print("Escaleno - três lados diferentes;")
    else:
        return print("Os valores não correspondem a um Triangulo")


e_triangulo(l1, l2, l3)
print("\n", "="*30, "\n")
