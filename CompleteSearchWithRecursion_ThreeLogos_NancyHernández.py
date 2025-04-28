import math
def validaciones(r, s, t, u, x, y):
    empresaA = r * s
    empresaB = t * u
    empresaC = x * y
    verificacion = empresaA + empresaB + empresaC 
    lado_area = int(math.sqrt(verificacion))     
    if lado_area * lado_area == verificacion: 
        for (l1, a1) in ((r, s), (s, r)):
            for (l2, a2) in ((t, u), (u, t)):
                for (l3, a3) in ((x, y), (y, x)):
                    if l1 + l2 + l3 == lado_area and max(a1, a2, a3) == lado_area:
                        matriz = [["A"] * l1 + ["B"] * l2 + ["C"] * l3 for _ in range(a1)]
                        return lado_area, matriz
                    if max(l1, l2, l3) == lado_area and a1 + a2 + a3 == lado_area:
                        matriz = []
                        matriz += [["A"] * l1 + ["B"] * (lado_area - l1) for _ in range(a1)]
                        matriz += [["B"] * l2 + ["C"] * (lado_area - l2) for _ in range(a2)]
                        matriz += [["C"] * l3 + ["A"] * (lado_area - l3) for _ in range(a3)]
                        return lado_area, matriz
        return -1 
    else:
        return -1 
r, s, t, u, x, y = list(map(int, input().split()))
resultado = validaciones(r, s, t, u, x, y)
if resultado == -1:
    print("-1")
else:
    lado_area, matriz = resultado
    print(lado_area)
    for fila in matriz:
        print("".join(fila)) #nota el problema es de dificultad hard
