s = str(input("Nhap chuoi: "))
if '!'  not in s:
        print(f"Chuoi sau khi bo xung dau cham than: '{s}!!!'")
else:
    print(f"Chuoi sau khi bo xung dau cham than: '{s}!!'")
    if '!!'  in s:
        print(f"Chuoi sau khi bo xung dau cham than: '{s}!!'")
    elif '!!!' in s:
        print(f"Chuoi sau khi bo xung dau cham than: '{s}'")