immutable_var = 1, 2, 3, True, 'Love', '1'
print(immutable_var)
print(type(immutable_var))
print(immutable_var[0])
immutable_var[0]
immutable_var = [1, 2, 3], True, 'Love', '1'
print(type(immutable_var[0]), type(immutable_var[1]), type(immutable_var[2]))
immutable_var[0][1] = 7
print(immutable_var)