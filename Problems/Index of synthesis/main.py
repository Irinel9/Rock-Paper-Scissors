intrare = float(input())
if 1 <= intrare < 2:
    iesire = 'Analytic'
elif 2 <= intrare <= 3:
    iesire = 'Synthetic'
elif 3 < intrare < 4:
    iesire = 'Polysynthetic'
else:
    iesire = 'Intrarea este gresita'
print(iesire)
