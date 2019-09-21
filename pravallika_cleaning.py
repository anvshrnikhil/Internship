import pandas as pd
import numpy as np
from scipy.stats import mode

#Read files:
train = pd.read_csv("D:\Pravallika\Internship\Project\Train.csv")
test = pd.read_csv("D:\Pravallika\Internship\Project\Test.csv")

#...Combining the datasets.......
train['source']='train'
test['source']='test'
data = pd.concat([train, test],ignore_index=True,sort=False)


#.........................................Data Cleaning........................................................

item_id = list(data['Item_Id'])
udata = list(set(data['Item_Id']))
w = list(data['Item_Weight'])
fat_cont = list(data['Item_Fat_Content'])
item_v =list(data['Item_Visibility'])
u_fat = list(set(data['Item_Weight']))
w_miss = data['Item_Weight'].isnull()

def clean_Item_fat_content(df):

    item_fat_content = list(df['Item_Fat_Content'])

    for itr in range(len(item_fat_content)):

        if item_fat_content[itr] == "Low Fat" or item_fat_content[itr] == "low fat" or item_fat_content[itr] == "LF" :
            df.loc[itr,'Item_Fat_Content'] = "Low Fat"
        else:
            df.loc[itr,'Item_Fat_Content'] = "Regular"

    return df

clean_Item_fat_content(data)


#................................................................Item_Id...........................................................

item_avg_weight = pd.pivot_table(data,values='Item_Weight', columns='Item_Id')
#print(item_avg_weight)
#print("value",item_avg_weight.loc['Item_Weight','DRA24'])

count = 0
for itr in list(data['Item_Weight']):
    if pd.isna(itr):
        count += 1

print(count)

std_item_id = list(item_avg_weight.columns)

for itr in std_item_id:
    for inner_itr in range(len(item_id)):
        if itr == item_id[inner_itr] :
            data.loc[inner_itr, 'Item_Weight'] = item_avg_weight.loc['Item_Weight',itr];

count = 0
for itr in list(data['Item_Weight']):
    if pd.isna(itr):
        count += 1

print(count)



#........................................................Outlet_Id...............................................................



shop_id = list(data['Outlet_Id'])
u_sid = list(set(data['Outlet_Id']))

#for i in range(len(u_sid))


o_size = pd.pivot_table(data,values='Outlet_Size', columns='Outlet_Type',aggfunc=(lambda x:mode(x).mode[0]))
print(o_size)
o_miss = data['Outlet_Size'].isnull()
print(o_miss)

count = 0
for itr in list(data['Outlet_Size']):
    if pd.isna(itr):
        count += 1

print(count)
std_o_size = list(o_size.columns)


for itr in  std_o_size:
    data.loc[o_miss,'Outlet_Size'] = data.loc[o_miss,'Outlet_Type'].apply(lambda x: o_size[x])


count = 0
for itr in list(data['Outlet_Size']):
    if pd.isna(itr):
        count += 1
print(count)

writer = pd.ExcelWriter('clean_data1.xls')
data.to_excel(writer, 'Sheet1', index = False)
writer.save()
