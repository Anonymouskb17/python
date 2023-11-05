#gắn D bằng giá trị
D = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
# Sắp xếp các cặp key-value của từ điển D theo thứ tự tăng dần của key
sorted_items = sorted(D.items())
for key, value in sorted_items:
    print(value)