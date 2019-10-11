"""
darbai = {
    'pamatas': '40',
    'murinimas': '8',
    'stogas': '35',
    'tinkavimas': '7'
}
"""
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

darbo_tipas = input('Pasirinkite viena is siu darbu: pamatas, murijimas, stogas, tinkavimas, dazymas: ')
"""
def pamato_skaiciavimas():
    beginis_metras = input('Iveskite beginiu metru kieki: ')
    pamato_kaina = input('Iveskite metro kaina ')
    kaina = int(beginis_metras) * int(pamato_kaina)
    print(f'Pamato kaina yra: {kaina}')

def murinijimo_skaiciavimas():
    perimetro_ilgis = input('Iveskite perimetro ilgi: ')
    aukstis = input('Iveskite auksti: ')
    kaina_kvadrato = input('Iveskite kvadrato kaina: ')
    kaina = int(perimetro_ilgis) * int(aukstis) * int(kaina_kvadrato)
    print(f'Murinijimo kaina yra: {kaina}')
murinijimo_skaiciavimas()