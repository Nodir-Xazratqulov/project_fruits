def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    f=open(data, mode='r')
    s=f.read()
    list1=[]
    list2=[]
    for i in s.split('\n'):
        list1.append(i.split(','))
    for k in list1:
        list2.append(k[-1])
    
   
   
    n=(list2[1])
    
    for j in list2[1:]:
        
        if float(j)<float(n): 
            n=j
            
    s=list2.index(n)
    
    return list1[s][0]
print(get_cheapest_fruit('fruits.csv'))
    # your code here
    