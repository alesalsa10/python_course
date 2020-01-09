class Superlist(list):  # list inside a class
    def __len__(self):
        return 1000


super_list1 = Superlist()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
