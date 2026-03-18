matn = "Salom Dunyo"

unlilar = "aeiouAEIOU"

count = 0

for harf in matn:
    if harf in unlilar:
        count += 1

print(count)