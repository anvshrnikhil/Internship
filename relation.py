
''' from the result we can consider that primary key(Item_Id, Outlet_Id)'''
import dretrive as dr

df = dr.get_data('train.xls')

lis = ['Item_Id', 'Outlet_Id']

df = dr.get_req_att(df, lis)

#print(df)

shop_list = list(df['Outlet_Id'])
item_list = list(df['Item_Id'])

std_shop_list = list(set(shop_list))

relation = {}

for itr in std_shop_list:
    temp = []
    for inner_itr in range(len(shop_list)):
        if itr == shop_list[inner_itr]:
            temp.append(item_list[inner_itr])
    relation[itr] = temp

count = 0
for itr in relation:
    #print(itr)
    #print(relation[itr])
    print(len(relation[itr]))
    print(len(set(relation[itr])))
    count += len(relation[itr])
print(count)

'''
#testing

print(relation['OUT010'])
print(len(relation['OUT010']))
print(len(set(relation['OUT010'])))
'''
