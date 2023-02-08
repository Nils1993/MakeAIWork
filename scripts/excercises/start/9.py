price = float(input('Wat kostte het eten?'))
tip_percentage = int(input('Hoeveel procent fooi wil je geven?'))

tip = price / 100 * tip_percentage

print(f'tip: €{round(tip , 2)}')
print(f'totaal: €{round(price + tip , 2)}')