from Operacoes import Operacoes as op

proposicao = "p>(qv(p^q)^(p^q))>q^(q>p)^~p=~p".lower()




prop = op(proposicao)
print(prop.getListLetters())

print(prop.getByParentese())
print(prop.getProposicao())

print(prop.getOperacoes("^"))
print(prop.getProposicao())

print(prop.getOperacoes(">"))
print(prop.getProposicao())

print(prop.getOperacoes("~"))
print(prop.getProposicao())

print(prop.getOperacoes("="))
print(prop.getProposicao())


str(bin(0)).split("b")[1].zfill(2)