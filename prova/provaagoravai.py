with open("usuarios.txt" ) as arq1:
    with open("relatorio.txt", "w") as arq2:

        def converte(byts):
            return (int(byts) /1024 / 1024)

        lista_dados = []
        lista_usuario = []
        lista_porcentagem = []
        soma = 0
        
        for i in arq1:
            i = i.strip()
            usuario ,dados = i.split()
            lista_dados.append(dados)
            lista_usuario.append(usuario)
            porcentagem = (int(dados)*100 )
            lista_porcentagem.append(porcentagem)
            soma += int(dados)
           
        print("ACMC Inc Uso do espaço em disco pelos usuarios",file=arq2)
        print("----------------------------------------------------------",file=arq2)
        print("Nr.        Usuario        Espaço Utilizado        % do uso",file=arq2)

        
        for posiçao in range(0,len(lista_usuario)):
            print('{}      {}       {:>8.2f}MB         {:>6.2f} %'.format(posiçao+1,lista_usuario[posiçao].center(15),converte(lista_dados[posiçao]),int(lista_porcentagem[posiçao])/soma), file=arq2)        
        soma = (soma/1024/1024)
        print(' ', file=arq2)
        print('Espaço total ocupado: {:.2f} MB'.format(soma), file=arq2)  
        print('Espaço médio ocupado: {:.2f} MB'.format(soma/len(lista_usuario)), file=arq2)