
import dretrive as dr
import dvisual as dv
import pandas as pd
df = dr.get_data('train.xls')
lis = ['Outlet_Id', 'Item_Outlet_Sales']
df = dr.get_req_att(df, lis)

# no empty values
'''
lis = df['Item_Outlet_Sales']
count = 0
for itr in lis:
    if pd.isna(itr):
        count += 1
print(count)
'''

#no cleaning required
shop_list = df['Outlet_Id']
std_shop_list = dr.get_unqiue_list(shop_list)
sale_list = df['Item_Outlet_Sales']
sales = []

for shop in std_shop_list:
    count = 0
    for itr in range(len(shop_list)):
        if shop == shop_list[itr]:
            count += sale_list[itr]

    sales.append(count)

dv.bargraph(std_shop_list, sales)
