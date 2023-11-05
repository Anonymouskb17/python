n = int(input("Nhap tam giac pascal "))


tamgiac = [[0 for j in range(i+1)] for i in range(n)]


for i in range(n):
    for j in range(i+1):
        if j == 0 or j == i:
            # Các giá trị trên cạnh của tam giác là 1
            tamgiac[i][j] = 1
        else:
            # Giá trị trung tâm của tam giác là tổng của hai giá trị phía trên nó
            tamgiac[i][j] = tamgiac[i-1][j-1] + tamgiac[i-1][j]

# In ra tam giác Pascal
for i in range(n):
    # Thêm khoảng trắng để căn giữa các giá trị trong mỗi hàng
    print(' '.join(str(tamgiac[i][j]) for j in range(i+1)).center(n*2))