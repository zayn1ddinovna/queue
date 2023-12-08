unique = [3,3,3,8,3,3,3]

def find_unique(list):
    for x in list:
        if list.count(x)==1:
            return x


print(find_unique(unique))