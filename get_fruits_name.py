def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    f=open(data, mode='r')
    s=f.read()
    list1=[]
    list2=[]
    for i in s.split('\n'):
        list1.append(i.split(','))
    for k in list1:
        list2.append(k[0])
    list2.pop(0)
    list2.pop(-1)
    return list2
print(get_frutis_name('fruits.csv'))

    