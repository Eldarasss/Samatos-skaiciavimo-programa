"""
darbai = {
    'pamatas': '40',
    'murinimas': '8',
    'stogas': '35',
    'tinkavimas': '7'
}
"""

pamatas = 60
murijimas = 500
stogas = 120
tinkavimas = 650
dazymas = 650


pamatas_kaina_beg_m = 40
murijimas_kaina_m2 = 8
stogas_kaina_m2 = 35
tinkavimas_kaina_m2 = 7
dazymas_kaina_m2 = 10

def darbo_kainos_skaiciavimas(darbo_tipas, kvadratura):
    darbo_kaina = int(darbo_tipas) * int(kvadratura)
    return darbo_kaina

uzsakymo_kiekis = input('Suveskite uzsakymo kieki: ')
uzsakymo_vieneto_kaina = input('Suveskite vieneto kaina: ')
print(f'Darbu kaina yra: {darbo_kainos_skaiciavimas(uzsakymo_kiekis, uzsakymo_vieneto_kaina)}')

