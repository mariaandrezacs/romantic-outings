import random

encontros = [
    "Filminho em casa com pipoca",
    "Piquenique no parque",
    "Jantar em um restaurante novo",
    "Noite de jogos de tabuleiro",
    "Cozinhar juntos uma receita nova",
    "Passeio de mãos dadas no shopping",
    "Sessão de fotos juntos",
    "Viagem de um dia pra um lugar novo",
    "Aula de dança em casa",
    "Dia de spa caseiro",
    "Pôr do sol num lugar bonito",
    "Maratona de série favorita"
]

print("SORTEADOR DE ENCONTROS")
print("-" * 30)
print(f"Próximo date ideal: {random.choice(encontros)}")
print("-" * 30)
input("Aperte Enter pra sair...")
