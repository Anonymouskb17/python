# def count_exchange_plans(N, M):
#     dp = [[0 for j in range(6)] for i in range(N+1)]
#     for i in range(N+1):
#         dp[i][0] = 0
#     for j in range(6):
#         dp[0][j] = 1
#     for i in range(1, N+1):
#         for j in range(1, 6):
#             dp[i][j] = dp[i][j-1]
#             for k in range(1, min(N//j, M//j)+1):
#                 dp[i][j] += dp[i-j*k][j-1]
#     return dp[N][5]

# N = int(input("Nhap N: "))
# M = int(input("Nhap M: "))
# print("So phuong an doi tien la:", count_exchange_plans(M, N))






# def dem(tien, soluong, m):
#     if soluong== 0:
#         return 1
#     if soluong<0 or not soluong:
#         return 0
#     count=0
#     for i in range(len(tien)):
#         if tien[i]<=m:
#             count+= dem(tien[i:],count - tien[i],m)
#             return count
# tien =[ 5000,2000,1000,500,200]
# n = int(input("Nhap n:"))
# m = int(input("Nhap m:"))
# print(dem(tien,n,m))

# def count_coin_change(coins, amount, m):
#     if amount == 0:
#         return 1
#     if amount < 0 or not coins:
#         return 0
#     count = 0
#     for i in range(len(coins)):
#         if coins[i] <= m:
#             count += count_coin_change(coins[i], amount - coins[i], m)
#     return count
# coins = [5000, 2000, 1000,500,200]
# n = int(input("Nhap n:"))
# m = int(input("Nhap m:"))
# print(count_coin_change(coins, n, m))


# def count_ways(N, M, coins):
#     if N == 0 or M == 0:
#         return 1
#     count = 0
#     for i in range(len(coins)):
#         if coins[i] <= N:
#             count += count_ways(N - coins[i], M - 1, coins[i:])
#     return count

# N = int(input("Nhập giá trị n: "))
# #M = int(input("Nhập giá trị m: "))


# coins = [5000, 2000, 1000, 500, 200]
# soluong =[0,0,0,0,0]
# for i in soluong:
#     soluong[i] = N/coins[i]
#     N %= coins[i]
# print (coins[i],"lay duoc", soluong[i])

# # num_ways = count_ways(N, M, coins)

# # # In kết quả
# # print("Số phương án đổi tiền là:", num_ways)


# def count_ways(N, coins, max_coins):
#     # Khởi tạo danh sách DP với giá trị ban đầu là 0
#     DP = [0] * (N+1)
    
#     # Khởi tạo danh sách số lượng xu với giá trị ban đầu là 1
#     num_coins = [1] * len(coins)
    
#     # Khởi tạo giá trị ban đầu cho trường hợp đặc biệt
#     DP[0] = 1
    
#     # Tính toán số phương án đổi tiền cho mỗi mệnh giá và số tiền cần đổi
#     for i in range(len(coins)):
#         for j in range(coins[i], N+1):
#             DP[j] += DP[j-coins[i]]
#             num_coins[i] += DP[j-coins[i]]
#             if num_coins[i] > max_coins:
#                 num_coins[i] = max_coins
    
#     # Trả về số phương án đổi tiền cần tìm
#     return DP[N]


# # Nhập giá trị n và giới hạn số lượng xu từ bàn phím
# N = int(input("Nhập giá trị n: "))
# M = int(input("Nhập giới hạn số lượng xu: "))

# # Các loại tiền kim loại của Việt Nam
# coins = [5000, 2000, 1000, 500, 200]

# # Tính số phương án đổi tiền
# num_ways = count_ways(N, coins, M)

# # In kết quả
# print("Số phương án đổi tiền là:", num_ways)



list = [5000, 2000, 1000, 500, 200]
def back(n,m,i=0,soto=0,sotien=0):
    ii = 0
    if i == 4:
        if (n-sotien)%list[4]==0 and (n-sotien)//list[4]+soto<=m: return 1
        else: return 0
    else:
        a = max( 0,   ((n-sotien)-(m-soto)*list[i+1])//list[i]   )
        b = m-soto 
        for j in range(a, b+1):
            tmp = sotien + j * list[i]
            if tmp == n: ii+=1
            elif tmp<n: ii+=back(n,m,i+1,soto+j,tmp)
            else: return ii
        return ii
n = int(input("N = "))
m = int(input("M = "))
print(f"Co {back(n,m)} phuong an doi tien")