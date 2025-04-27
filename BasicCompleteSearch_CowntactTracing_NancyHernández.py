n, t = map(int, input().split())            #ingresar los datos de la sig. forma (4 5 (por ejemplo))
if n < 2 or n > 100:                       
    print("la cantidad de vacas debe ser entre 2 a 100")
if t < 1 or t > 250:
    print("la cantidad de interacciones debe ser entre 1 y 250")
estado_vacas=list(map(int, input().split()))                      #ingresar así (ejemplo: 1 1 0 0)
if len(estado_vacas)!=n:
    print("los números deben ser iguales a la cantidad de vacas")
else:
    pass
for x in estado_vacas:
    if x!=0 and x!=1:
        print("Solo se pueden agregar 0 y 1 para el estado de las vacas")
    else:
        pass
interacciones=[]
for i in range(t):
    tiempo, x, y=map(int, input().split())
    interacciones.append((tiempo, x, y))                   #ingresarlas separadas (ejemplo: 3 1 3)
    if tiempo<=0:
        print("El tiempo debe ser mayor a cero")
    if x<1 or x>n or y<1 or y>n:
        print("los números deben estar entre el rango total de vacas")
    elif x==y:
        print("una vaca no puede interactuar consigo misma")
    else:
        pass
interacciones.sort()
paciente_cero=0
kmin=250
kmax=-1
posibles_ceros=[]
for paciente_cero in range(n):
    for k in range(251):
        infectados=[False]*n
        contagios=[0]*n
        infectados[paciente_cero]=True
        for tiempo, x, y in interacciones:
            x -= 1
            y -= 1
            if infectados[x] and contagios[x] < k:
                if not infectados[y]:
                   infectados[y] = True
                   contagios[x] += 1
            if infectados[y] and contagios[y] < k:
                if not infectados[x]:
                   infectados[x] = True
                   contagios[y] += 1
        estado_final_simulado = [1 if v else 0 for v in infectados]
        if estado_final_simulado == estado_vacas:
            if k < kmin:
                kmin = k
            if k > kmax:
                kmax = k
            if paciente_cero not in posibles_ceros:
                posibles_ceros.append(paciente_cero)
print(len(posibles_ceros), kmin, "Infinito" if kmax == 250 else kmax)  #nota el problema es de dificultad very hard

  

                
        

    
    

    



 


