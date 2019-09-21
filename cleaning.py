
import dretrive as dr
import pandas as pd


df = dr.get_data('train.xls')

att_lis = ['Item_Weight', 'Item_Fat_Content', 'Item_Type', 'Outlet_Id', 'Item_Outlet_Sales', 'Item_MRP']

df = dr.get_req_att(df, att_lis)

iweight = list(df['Item_Weight'])
ifat = list(df['Item_Fat_Content'])
itype = list(df['Item_Type'])
shopid = list(df['Outlet_Id'])
sales = list(df['Item_Outlet_Sales'])
mrp = list(df['Item_MRP'])

print('sales error count : ', dr.count_nan(sales))

'''
count_out019 = 0
for itr in range(len(iweight)):
    #' ' '
    #if (ifat[itr] == 'Low Fat' or ifat[itr] == 'LF' or ifat[itr] == 'low fat') and itype[itr] == 'Baking Goods' and shopid[itr] == 'OUT027' :
    #   print(iweight[itr], " ", sales[itr], " ", mrp[itr])
    #' ' '
    if shopid[itr] == 'OUT019':
        count_out019 += 1
'''
#print(count_out019)


for outer_itr in list(dr.get_unqiue_list(shopid)):
    count = 0
    for itr in range(len(itype)):
        if shopid[itr] == outer_itr :
            if pd.isna(iweight[itr]):
                count += 1

    print(outer_itr, ': Check nan :', count)
