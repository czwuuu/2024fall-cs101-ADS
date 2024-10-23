Haab = {'pop':1, 'no':2, 'zip':3, 'zotz':4, 'tzec':5, 'xul':6, 'yoxkin':7,
        'mol':8, 'chen':9, 'yax':10, 'zac':11, 'ceh':12, 'mac':13,
        'kankin':14, 'muan':15, 'pax':16, 'koyab':17, 'cumhu':18, 'uayet':19}
Tzolkin = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat',
           'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban',
           'eznab', 'canac', 'ahau']
def Haab_to_Tzolkin(date):
    day, month, year = date.split()
    day = int(day.rstrip('.'))
    year = int(year)
    absolute_days = year*365+(Haab[month]-1)*20+day

    year2 = str(absolute_days//260)
    absolute_days %= 260
    Tzolkin_day = str(absolute_days%13+1)+' '+Tzolkin[absolute_days%20]+' '+year2
    return Tzolkin_day


n = int(input())
Tzolkin_days = []
for i in range(n):
    Tzolkin_days.append(Haab_to_Tzolkin(input()))
print(n)
for days in Tzolkin_days:
    print(days)
