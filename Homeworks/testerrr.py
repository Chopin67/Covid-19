import salarytest

for name in (
        'Teresa Sullivan',
        'Sullivan, Teresa',
        '161048349',
        'Ali Reza Forghani Esfahani',
        'pamela-neff',
        'Thomas Jefferson'
        ):
    job, money, rank = salarytest.report(name)
    print(name, 'is a', job, 'and makes', money, '(rank', str(rank)+')')
