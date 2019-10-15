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

def stogo_skaiciavimas():
    ilgis = input('Iveskite ilgi: ')
    plotis = input('Iveskite ploti: ')
    kaina_kvadrato = input('Iveskite kvadrato kaina')
    kaina = int(ilgis) * int(plotis) * int(kaina_kvadrato)
    print(f'Stogo kaina yra: {kaina}')

def tinkavimo_skaiciavimas():
    ilgis = input('Iveskite ilgi: ')
    plotis = input('Iveskite ploti: ')
    kaina_kvadrato = input('Iveskite kvadrato kaina: ')
    kaina = int(ilgis) * int(plotis) * int(kaina_kvadrato)
    print(f'Tinkavimo kaina yra: {kaina}')

def dazymo_skaiciavimas():
    ilgis = input('Iveskite ilgi: ')
    plotis = input('Iveskite ploti: ')
    kaina_kvadrato = input('Iveskite kvadrato kaina: ')
    kaina = int(ilgis) * int(plotis) * int(kaina_kvadrato)
    print(f'Dazymo kaina yra: {kaina}')

def darbo_tipas():
    pamatas = pamato_skaiciavimas
    muras = murinijimo_skaiciavimas
    stogas = stogo_skaiciavimas
    tinkas = stogo_skaiciavimas
    dazymas = dazymo_skaiciavimas
    print(f'Pasirinkite viena is siu darbu: pamatas, murijimas, stogas, tinkavimas, dazymas: {pamatas}, {muras}, {stogas}, {tinkas}, {dazymas}')
darbo_tipas()