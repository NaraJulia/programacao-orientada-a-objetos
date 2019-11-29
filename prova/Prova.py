with open("usuarios.txt") as arq1:
    with open("relatorio.txt","w") as arq2:
      print("ACMC Inc Uso do espaço em disco pelos usuarios",file=arq2)
      print("----------------------------------------------",file=arq2)
      for x in arq1:
          print(x,file=arq2)
