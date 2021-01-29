def impozit(intrare):
    if 0 < intrare <= 15527:
        procent = 0
    elif 15528 <= intrare <= 42707:
        procent = 15
    elif 42708 <= intrare <= 132406:
        procent = 25
    else:
        procent = 28
    return round(intrare * procent / 100), procent


venit = int(input())
calculated_tax, percent = impozit(venit)
print(f'The tax for {venit} is {percent}%. That is {calculated_tax} dollars!')
