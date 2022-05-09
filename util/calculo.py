from datetime import timedelta

def somar(hr1, mm1, hr2, mm2):
    time1 = timedelta(hours = hr1, minutes = mm1)
    time2 = timedelta(hours = hr2, minutes = mm2)
    rest = time1 + time2
    soma = str(rest)
    if 'days' in soma:
        hora = soma.split('days, ')
        dia = hora[0]
        dia = 24 * int(dia)

        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        mm = hrs[1]
        result_conv = (f'{tothoras}:{mm}')
        return result_conv
    elif 'day' in soma:
        hora = soma.split('day, ')
        dia = hora[0]
        dia = 24 * int(dia)
        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        mm = hrs[1]
        result_conv = (f'{tothoras}:{mm}')
        return result_conv
    else:
        hora = soma.split(':')
        hr = hora[0]
        mm = hora[1]
        result_conv = (f'{hr}:{mm}')
        return result_conv

def subtrair(hr1, mm1, hr2, mm2):
    time1 = timedelta(hours=hr1, minutes=mm1)
    time2 = timedelta(hours=hr2, minutes=mm2)
    rest = time1 - time2
    res = str(rest)
    if 'days' in res:
        hora = res.split('days, ')
        dia = hora[0]
        dia = 24 * int(dia)
        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        result_conv = (f'{tothoras}:{int(hrs[1])}')
        return result_conv
    elif 'day' in res:
        hora = res.split('day, ')
        dia = hora[0]
        dia = 24 * int(dia)
        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        result_conv = (f'{tothoras}:{int(hrs[1])}')
        return result_conv
    else:
        hora = res.split(':')
        hr = hora[0]
        mm = hora[1]
        result_conv = (f'{hr}:{mm}')
        return result_conv

def adicnot(hr1, mm1):
    time1 = timedelta(hours=hr1, minutes=mm1)
    int = 0.142859
    res = time1 + (time1 * int)
    return res


def multiplicar(hr1, mm1, mm2):
    time1 = timedelta(hours=hr1, minutes=mm1)
    rest = time1 * mm2
    res = str(rest)
    if 'days' in res:
        hora = res.split('days, ')
        dia = hora[0]
        dia = 24 * int(dia)

        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        mm = hrs[1]
        result_conv = (f'{tothoras}:{mm}')
        return result_conv
    elif 'day' in res:
        hora = res.split('day, ')
        dia = hora[0]
        dia = 24 * int(dia)
        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        mm = hrs[1]
        result_conv = (f'{tothoras}:{mm}')
        return result_conv
    else:
        hora = res.split(':')
        hr = hora[0]
        mm = hora[1]
        result_conv = (f'{hr}:{mm}')
        return result_conv

def dividir(hr1, mm1, mm2):
    time1 = timedelta(hours=hr1, minutes=mm1)
    rest = time1 / mm2
    res = str(rest)

    if 'days' in res:

        hora = res.split('days, ')
        dia = hora[0]
        dia = 24 * int(dia)

        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        mm = hrs[1]
        result_conv = (f'{tothoras}:{mm}')
        return result_conv
    elif 'day' in res:
        hora = res.split('day, ')
        dia = hora[0]
        dia = 24 * int(dia)
        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        mm = hrs[1]
        result_conv = (f'{tothoras}:{mm}')
        return result_conv
    else:
        hora = res.split(':')
        hr = hora[0]
        mm = hora[1]
        result_conv = (f'{hr}:{mm}')
        return result_conv

def percent(hr1, mm1, mm2):
    time1 = timedelta(hours=hr1, minutes=mm1)
    rest = time1 + time1 * (mm2 / 100)
    res = str(rest)

    if 'days' in res:

        hora = res.split('days, ')
        dia = hora[0]
        dia = 24 * int(dia)

        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        mm = hrs[1]
        result_conv = (f'{tothoras}:{mm}')
        return result_conv
    elif 'day' in res:
        hora = res.split('day, ')
        dia = hora[0]
        dia = 24 * int(dia)
        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        mm = hrs[1]
        result_conv = (f'{tothoras}:{mm}')
        return result_conv
    else:
        hora = res.split(':')
        hr = hora[0]
        mm = hora[1]
        result_conv = (f'{hr}:{mm}')
        return result_conv