def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    f=open(data, mode='r')
    s=f.read()
    list1=[]
    list2=[]
    for i in s.split('\n'):
        list1.append(i.split(','))
    for k in list1:
        list2.append(k[-1])
    list2.pop(0)
    list2.pop(-1)
    n=0
    for j in list2:
        n+=float(j)
    return n
print(get_total_price('fruits.csv'))

    