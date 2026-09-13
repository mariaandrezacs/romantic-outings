from datetime import date

data_inicio = date(2024, 6, 15)  # mude para a data de vocês
hoje = date.today()
dias = (hoje - data_inicio).days
anos = dias // 365
meses = (dias % 365) // 30

print("=" * 40)
print("   NOSSO CONTADOR DE NAMORO")
print("=" * 40)
print(f"Juntos há: {dias} dias")
print(f"Isso dá cerca de: {anos} ano(s) e {meses} mês(es)")
print("=" * 40)
input("Aperte Enter pra sair...")
