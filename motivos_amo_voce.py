import random

motivos = [
    "porque você me faz rir sem fazer nada",
    "porque seu sorriso é o melhor do dia",
    "porque você é a pessoa mais gentil que conheço",
    "porque com você qualquer lugar é bom",
    "porque você me apoia em tudo",
    "porque sua voz acalma meu coração",
    "porque você é linda por dentro e por fora",
    "porque você é o melhor presente que a vida me deu",
    "porque eu sou muito mais feliz ao seu lado",
    "porque você é simplesmente incrível"
]

print("10 MOTIVOS PRA EU AMAR VOCÊ HOJE:")
print("-" * 35)
for i, motivo in enumerate(random.sample(motivos, 10), 1):
    print(f"{i}. {motivo}")
print("-" * 35)
input("Aperte Enter pra sair...")
