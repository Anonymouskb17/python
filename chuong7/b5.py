prices = { "banana": 4, "apple": 2, "orange": 1.5, "pear": 3 }
stock = { "banana": 6, "orange": 32, "pear": 15 }


# xep = sorted(prices.values(), reverse=True)
# print(xep)
# s = []

# for i in sorted(prices, key=prices.get, reverse=True):
#     s.append((i, prices[i]))
#     print(i)
    
# print(s)

# for i in prices.values(): print(sorted(prices, key= prices.items, reverse= True))

    
    
        
# d = list()
# d.items(prices,stock)
# print(d)
# # d = {}
# # a= {d.items(prices,stock)}

# # print(a)

prices = {"apple": 20, "banana": 10, "orange": 15, "grape": 25}
stock = {"apple": 10, "banana": 20, "orange": 15, "grape": 5}
s=[]
total_values = {k: v * prices[k] for k, v in stock.items()}


sorted_fruits = sorted(total_values.keys(), key=lambda x: total_values[x], reverse=True)
for i in sorted(prices,key=prices.get,reverse=True ):
    s.append((i, prices[i]))


for fruit in sorted_fruits:
    print(fruit)

print(s)
