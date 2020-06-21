#indece          0   1  2  4  5
lugares_vagos = [10, 2, 1, 3, 0]
#sala            1   2  3  4  5
print("CINEMA")
print(" ")
print("*"*60)
while True:
  sala = int(input("Sala (0 sai): " ))
  if sala == 0:
    print("Fim")
    break
  if sala > len(lugares_vagos) or sala < 1:
    print("Sala inválida")
  elif lugares_vagos[sala-1] == 0:
    print("Desculpas, sala lotada!")
  else:
    ingresso = int(input(f"Quantos ingressos você deseja - ({lugares_vagos[sala-1]}) vagos: "))
    if ingresso > lugares_vagos[sala-1]:
      print("Esse número de ingressos não esta dispónivel.")
    elif ingresso <= 0:
      print("Quantidade de ingressos inválida!")
    else:
      lugares_vagos[sala-1] -= ingresso
      print(f"{ingresso} ingresso vendidos")

  print("*"*50)
  print("UTILIZAÇÃO DAS SALAS")

  for indice, valor in enumerate(lugares_vagos):
    print(f"Sala {indice+1} - {valor} lugar(es) vago(s)")