n = int(input())  #aqui el usuario va a ingresar el número de vacas
vacas_norte=[]
vacas_este=[]
parada_norte=0
parada_este=0
contador1=0
contador2=0
for i in range(n):
    d, x, y=input().split()    #en ese apartada se deben ingresar los datos de la sig. manera
    contador1=i               # N 2 3 (es un ejemplo) o E 1 5                                                           
    if d == "N":
        vacas_norte.append((int(x), int(y), contador1))
    elif d =="E":
        vacas_este.append((int(x), int(y), contador1))
resultadoN=[0]*len(vacas_norte)
resultadoE=[0]*len(vacas_este)
parada_este=[0]*len(vacas_este)
parada_norte=[0]*len(vacas_norte)
for i in range(len(vacas_norte)):
    for j in range(len(vacas_este)):
        if vacas_norte[i][0]>vacas_este[j][0]and vacas_norte[i][1]<vacas_este[j][1]:
            tiempo_norte= vacas_este[j][1]-vacas_norte[i][1]
            tiempo_este= vacas_norte[i][0]-vacas_este[j][0]
            if tiempo_norte==tiempo_este:
                continue
            elif tiempo_norte>tiempo_este:
                if parada_norte[i]==0 :
                    parada_norte[i]=tiempo_norte
                elif parada_norte[i]>=tiempo_norte:
                       parada_norte[i]=tiempo_norte                    
            
            elif tiempo_norte<tiempo_este:
                if parada_este[j]==0:
                    parada_este[j]=tiempo_este
                elif parada_este[j]>=tiempo_este:
                       parada_este[j]=tiempo_este     
resultados=[None]*n
for i in range(len(vacas_norte)):
    if parada_norte[i]==0:
        resultados[vacas_norte[i][2]]="Infinito" 
    else:
        resultados[vacas_norte[i][2]]=parada_norte[i]
for j in range(len(vacas_este)):
    if parada_este[j]==0:
        resultados[vacas_este[j][2]]="Infinito" 
    elif parada_este!=0:
        resultados[vacas_este[j][2]]=parada_norte[j]
for x in range(n):
    print(resultados[x])   #el problema es de dificultad "very hard"
          


        



