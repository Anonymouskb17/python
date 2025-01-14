
# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
# if A == B and A != C:
#     if A > C:
#         print("Xep tang dan: ", C,A)
#     else:
#         print("Xep tang dan: ", A,C)
# elif A == C and A != B:
#     if A > B:
#         print("Xep tang dan: ", B,A)
#     else:
#         print("Xep tang dan: ", A,B)
# elif A == B == C:
#     print("Xep tang dan: ", A)
# else:
#     arr = [A, B, C]
#     arr.sort()
#     print("Xep tang dan: ", arr[0], arr[1],arr[2])


# a = input("A = ")
# b = input("B = ")
# c = input("C = ")

# if a != b and b != c and a != c:
#     if a < b < c:
#         a, c = c, a
#     elif a < c < b:
#         a, b, c = b, c, a 
#     elif b < a < c:
#         a, b, c = c, a, b
#     elif b < c < a: 
#         b, c = c, b
#     elif c < a < b:
#         a, b = b, a
#     elif a < b == c:
#         a, c = c, a
#     elif b < a == c:
#         b , c = c, b
#     elif a == b < c:
#         a, c = c, a
#     elif a == c < b:
#         a, b = b, a
 
# if a == b == c:
#  print("Xep tang dan:", a)
# elif a == b:
#  print("Xep tang dan:", c, b)
# elif b == c:
#  print("Xep tang dan:", c, a)
# else:
#  print("Xep tang dan:", c, b, a)

a = input("A = ")
b = input("B = ")
c = input("C = ")

if a != b and b != c and a != c:
    if a < b < c:
        a, c = c, a
    elif a < c < b:
        a, b, c = b, c, a 
    elif b < a < c:
        a, b, c = c, a, b
    elif b < c < a:
        b, c = c, b
    elif c < a < b:
        a, b = b, a
elif a < b == c:
 a, c = c, a
elif b < a == c:
 b, c = c, b
elif a == b < c:
 a, c = c, a
elif a == c < b:
 a, b = b, a
 
if a == b == c:
 print("Xep tang dan:", a)
elif a == b:
 print("Xep tang dan:", c, b)
elif b == c:
 print("Xep tang dan:", c, a)
else:
 print("Xep tang dan:", c, b, a)