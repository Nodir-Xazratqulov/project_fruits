def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code 
    f=open(data, mode='r')
    s=f.read()
    list1=[]
    list2=[]
    for i in s.split('\n'):
        list1.append(i.split(','))
    for k in list1:
        list2.append(k[-1])
    list2.pop(0)
   
   
    n=(list2[0])
    for j in list2:
        if float(j)<float(n): 
            n=j
            # print(n)
    s=list2.index(n)
    return s
print(get_cheapest_fruit_id('fruits.csv'))

