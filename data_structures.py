#TASK 1
A = ((11,12),[21,22])
print(A[1])  # Output: [21, 22]

#TASK 2
A = ((11,12),[21,22])
print(A[0][1])  # Output: 12

#TASK 3 
L = [1, 2, 3]
L.append(['a', 'b'])
print(L)  # Output: [1, 2, 3, ['a', 'b']]

#TASK 4
A = ["hard rock", 10, 1.2]
del(A[0])
print(A)  # Output: [10, 1.2]

#TASK 5
A = [1, 2, 3, 4, 5]
B = A[:]
print(B)  # Output: [1, 2, 3, 4, 5]

#TASK 6
print(len(("disco",10,1.2, "hard rock",10)))  # Output: 5

#TASK 7
d = { "The Bodyguard":"1992", "Saturday Night Fever": "1977"}
values = list(d.values())
print(values)  # Output: ['1992', '1977']

#TASK 8
release_year_dict = {"The Bodyguard": 1992, "Saturday Night Fever": 1977}
print(release_year_dict.values())  # Output: dict_values([1992, 1977])

#TASK 9
V = {'1', '2'}
V.add('3')
print(V)  # Output: {'1', '2', '3'}


#TASK 10
print('1' in {'1', '2'})  # Output: True

