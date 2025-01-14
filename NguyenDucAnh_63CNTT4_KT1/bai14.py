def generate_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)
    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(' '.join(str(num) for num in row))

n = int(input("Nhập số dòng của tam giác Pascal: "))
triangle = generate_pascal_triangle(n)
print_pascal_triangle(triangle)
        
        