radnici = [
{'ime': 'Milos', 'plata': 58000, 'godine': 29},
{'ime': 'Fangio', 'plata': 98000, 'godine': 51},
{'ime': 'Marko', 'plata': 76000, 'godine': 24}
]

prosek_plata = sum(r['plata'] for r in radnici) / len(radnici)
prosek_godina = sum(r['godine'] for r in radnici) / len(radnici)

print(f"Prosek plate: {prosek_plata}")
print(f"Prosek godina: {prosek_godina}")
