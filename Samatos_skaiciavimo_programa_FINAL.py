pamatas = [
    ('Iveskite beginiu metru skaiciu ', 'beginis metras'),
    ('Iveskite kvadrato kaina ', 'kaina'),
]
murijimas = [
    ('Iveskite ilgio metru skaiciu ', 'metras'),
    ('Iveskite ploti ', 'metras'),
    ('Iveskite kvadrato kaina ', 'kaina'),
]
stogas = [
    ('Iveskite ilgio metru skaiciu ', 'metras'),
    ('Iveskite ploti ', 'metras'),
    ('Iveskite kvadrato kaina ', 'kaina'),

]
tinkas = [
    ('Iveskite ilgio metru skaiciu ', 'metras'),
    ('Iveskite ploti ', 'metras'),
    ('Iveskite kvadrato kaina ', 'kaina'),
]
dazymas = [
    ('Iveskite ilgio metru skaiciu ', 'metras'),
    ('Iveskite ploti ', 'metras'),
    ('Iveskite kvadrato kaina ', 'kaina'),
]
def perskaityti_vartotojo_ivesti(laukai):
    """Perskaito nurodytus laukus ir iskviecia skaiciavimo funkcija kuri panaudota ivestus laukus"""
    atsakymai = []
    for klausimas, lauko_pavadinimas in laukai:
        try:
            atsakymas = int(input(klausimas))
        except ValueError:
            print('Sis laukas privalo buti sveikas skaicius, paleiskite programa is naujo ir bandykite vel.')
            exit()
        atsakymai.append((lauko_pavadinimas, atsakymas))
    skaiciavimas(atsakymai, laukai)

def skaiciavimas(atsakymu_sarasas, laukai):
    """Skaiciuoja galutine kaina ir isveda atsakyma"""
    i=0
    kaina = 1
    while i < len(laukai):
        kaina = kaina * atsakymu_sarasas[i][1]
        i=i+1
    print(f'Darbo kaina {kaina}.')

ivestis = input('Iveskit darbo tipa: ')

if ivestis == 'pamatas':
    perskaityti_vartotojo_ivesti(pamatas)
elif ivestis == 'murijimas':
    perskaityti_vartotojo_ivesti(murijimas)
elif ivestis == 'stogas':
    perskaityti_vartotojo_ivesti(stogas)
elif ivestis == 'tinkas':
    perskaityti_vartotojo_ivesti(tinkas)
elif ivestis == 'dazymas':
    perskaityti_vartotojo_ivesti(dazymas)
else:
    print('Tokio darbo nera. Paleiskite programa is naujo ir rasyk be klaidu')
