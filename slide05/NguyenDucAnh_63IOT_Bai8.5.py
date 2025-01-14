def res(lenght):

    tup = set()

    tup.add("()")

    while True:
        s = set()
        for seq in tup:
     
            new_seq = f"({seq})"
            if len(new_seq) < lenght:
                s.add(new_seq)

         
            for tups in tup:
                kethop = seq + tups
                if len(kethop) < lenght:
                    s.add(kethop)

        if s.issubset(tup):
            break

        tup.update(s)


    return sorted(tup, key=lambda x: (len(x), x))


N = int(input("Nhap so N:"))
result = res(N)
print(result)
