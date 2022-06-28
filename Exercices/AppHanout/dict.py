eleves = [{"name": "moaad", "notes": 14.5}, {"name": "ahmad", "notes": 18.25}, {"name": "salah", "notes": 9}]

for eleve in eleves:
    for key in eleve:
        print(key + ": " + str(eleve[key]))
