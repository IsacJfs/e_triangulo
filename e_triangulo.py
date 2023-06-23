print("\n", "="*30, "\n")
print("É Triangulo?")
print("Digite três valores numéricos \n\
O programa ira detalhar o triangulo:\n")
l1 = float(input("Primeiro valor: "))
l2 = float(input("Segundo valor: "))
l3 = float(input("Terceiro valor: "))
print("\n", "="*30, "\n")


def e_triangulo(lado1: float, lado2: float, lado3: float) -> tuple:
    """
    Função que recebe três valores de retas e verifica se formam um triangulo e qual o tipo.
    :param lado1: (float) qualquer valor > 0
    :param lado2: (float) qualquer valor > 0
    :param lado3: (float) qualquer valor > 0
    :return: (bool, str) bool: True se for triangulo, str: tipo do triângulo
    """
    # Analisa sé é triangulo e qual o tipo do triângulo
    lados = {lado1, lado2, lado3}  # Foi utilizado a função set para eliminar valores iguais
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        # algoritmo para determinar se três retas são um triângulo
        if len(lados) == 1:  # dois valores eliminados, então os três são iguais
            return True, "Equilátero"
        elif len(lados) == 2:  # um valor eliminado, então dois são iguais
            return True, "Isósceles"
        elif len(lados) == 3:  # Nenhum valor eliminado, então três diferentes
            return True, "Escaleno"
    else:
        return False, "Inválido"


resultado, tipo = e_triangulo(l1, l2, l3)
if resultado:
    print(f"É um triângulo do tipo {tipo}")
else:
    print(f"{tipo}, um triângulo não pode ser formado com esses valores.")
print("\n", "="*30, "\n")
