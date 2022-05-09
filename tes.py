from datetime import timedelta

hr1 = 11
mm1 = 00
hr2 = 0
mm2 = 8


def multiplicar(hr1, mm1, mm2):
    time1 = timedelta(hours=hr1, minutes=mm1)
    print(time1)
    res = str(time1 * mm2)
    print(res)
    if 'days' in res:
        hora = res.split('days, ')
        dia = hora[0]
        dia = 24 * int(dia)
        print(f'dias = {dia}')
        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        mm = hrs[1]
        result_conv = (f'{tothoras}:{mm}')
        print(result_conv)
    elif 'day' in res:
        hora = res.split('day, ')
        dia = hora[0]
        dia = 24 * int(dia)
        hr = hora[1]
        hrs = hr.split(':')
        tothoras = dia + int(hrs[0])
        mm = hrs[1]
        result_conv = (f'{tothoras}:{mm}')
        print(result_conv)
    else:
        hora = res.split(':')
        hr = hora[0]
        mm = hora[1]
        result_conv = (f'{hr}:{mm}')
        return result_conv

multiplicar(hr1, mm1, mm2)





