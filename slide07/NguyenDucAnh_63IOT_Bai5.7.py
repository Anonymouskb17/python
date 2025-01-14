gia = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
can = {"banana": 6, "orange": 32, "pear": 15}
tonggiatri = {fruit: gia.get(fruit, 0) * can.get(fruit, 0) for fruit in set(gia) | set(can)}
thutu = sorted(tonggiatri.items(), key=lambda x: x[1], reverse=True)

for fruit, value in thutu:
    print(f"{fruit} {value}")
    

