def pamato_skaiciavimas():
    beginis_metras = input('Iveskite beginiu metru kieki: ')
    pamato_kaina = input('Iveskite metro kaina ')
    try:
        kaina = int(beginis_metras) * int(pamato_kaina)
        print(f'Pamato kaina yra: {kaina}')
    except Exception as e:
        print('Turetu buti skaiciai o ne raides')
   

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
    galimi_pasirinkimai = ['pamatas', 'murijimas', 'stogas', 'tinkavimas', 'dazymas']
    pasirinktas_darbas = input('Pasirinkite viena is siu darbu: pamatas, murijimas, stogas, tinkavimas, dazymas')
    if pasirinktas_darbas in galimi_pasirinkimai:
        if pasirinktas_darbas == 'pamatas':
            pamato_skaiciavimas()
    else:
        print('Pasirinkite is', galimi_pasirinkimai)

darbo_tipas()