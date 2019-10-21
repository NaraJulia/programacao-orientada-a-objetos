Questao 7
primeiro = int(input("Primeiro numero:"))
segundo  = int(input("Segundo numero:"))
terceiro = int(input("Terceiro numero:"))
Nmaior = primeiro
if (segundo > Nmaior):
    Nmaior = segundo
if (terceiro > Nmaior):
    Nmaior = terceiro
print("Maior:",Nmaior)
Nmenor = primeiro
if (segundo < Nmenor):
    Nmenor = segundo
if (terceiro < Nmenor):
    Nmenor = terceiro
print("Menor:",Nmenor)