narx = 100000

yosh = int(input("Yoshingizni kiriting: "))


if yosh <= 6:
    chegirma = 50
elif 7 <= yosh <= 17:
    chegirma = 20
elif yosh > 60:
    chegirma = 30
else:
    chegirma = 0

narx = narx * (100 - chegirma) / 100

print(f"Yakuniy narx: {narx} so'm ({chegirma}% chegirma qo'llanildi)")