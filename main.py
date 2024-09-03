numbers=[917895462130,919875641230,9195969878,99342039483932,7283327323]
num_list_all=[]
for number in numbers:
    if len(str(number))>10:
        num_list=[]
        for i in range(len(str(number))-1,1,-1):
            num_list.append((str(number))[i])
        new_num="".join(num_list[ ::-1])
        num_list_all.append(new_num)
    else:
        num_list_all.append(number)    
print(num_list_all)    