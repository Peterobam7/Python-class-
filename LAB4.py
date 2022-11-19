
#ЗАД 1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = my_list[::2]
print(even)

#ЗАД 2
d_= [4,9,6,7,4,2,0,55,4,3,77,8,5]

def list_(x):
    new_list= []
    s  = 0
    for i  in x:
        if i>=s:
            new_list.append(i)

            s= i

        else:
            s=i
            continue

    return new_list[1:]     


print(list_(d_))

#ЗАД 3

    

    
       



        

   

       

        

    



