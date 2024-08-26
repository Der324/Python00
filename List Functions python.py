lucky_numbers = [4, 8, 15, 16, 23,42]
friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Rusaro"]
friends.extend(lucky_numbers)

print(friends)

lucky_numbers = [4, 8, 15, 16, 23,42]
friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Rusaro"]
friends.append("Gisa")

print(friends)


friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Rusaro"]
friends.insert(2, "Bwiza")
print(friends)


friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Rusaro"]
friends.remove("Nkotanyi")

print(friends)


friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Rusaro"]
friends.clear()

print(friends)


friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Rusaro"]
friends.pop()

print(friends)

lucky_numbers = [4, 8, 15, 16, 23,42]
friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Rusaro"]
print(friends.index("Teta"))
print(lucky_numbers.index(15))


friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Teta",  "Rusaro"]
print(friends.count("Teta"))


friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Rusaro"]
friends.sort()

print(friends)

lucky_numbers = [4, 8, 15, 16, 23,42]
friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Rusaro"]
lucky_numbers.reverse()
friends.reverse()

print(lucky_numbers)
print(friends)

lucky_numbers = [4, 8, 15, 16, 23,42]
friends = ["Ntale", "Nkotanyi", "Rugamba", "Ntwali", "Teta", "Rusaro"]
friends2 = friends.copy()
lucky_numbers2 = lucky_numbers.copy()

print(friends2)
print(lucky_numbers2)