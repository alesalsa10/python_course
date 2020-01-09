class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList([1, 2, 3, 5, 6])

print(len(super_list1))
super_list1.append(5)

