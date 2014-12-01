def nbr_of_laps(x, y):
    #find the smallest number to devide both of x and y
    large_num = x if y>x else y
    for i in xrange(large_num,x*y+1,large_num):
        if i%x==0:
            return [i/x, i/y]
