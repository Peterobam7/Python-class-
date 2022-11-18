
#ЗАД 1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = my_list[::2]
print(even)

#ЗАД 2

d_= [2,0,3,5,6,3,2,4,88,9]

s = 0

list_= []

for i  in d_:

    if i>s: 
        list_.append(i)

        s=i

        

    else:

        s=i

        continue 
print (list_[1:])
    



