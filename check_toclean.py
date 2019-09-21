
import dretrive as dr

def using_item_id():

    df = dr.get_data('train.xls')
    item_id = dr.get_unqiue_list(list(df['Item_Id']))
    item_id_list = list(dr.get_req_att(df, 'Item_Id'))
    item_weight = list(dr.get_req_att(df, 'Item_Weight'))
    item_fat_content = list(dr.get_req_att(df, 'Item_Fat_Content'))
    item_type = list(dr.get_req_att(df, 'Item_Type'))

    for outer_itr in item_id:
        for itr in range(len(item_id_list)):
            if item_id_list[itr] == outer_itr:
                print(item_id_list[itr], item_weight[itr], item_fat_content[itr], item_type[itr])
        input()

using_item_id()
print('Checking for nan values')
print('-----------------------')
df = dr.get_data('train.xls')
lis = list(df.columns)

for itr in lis:
    print(itr, " : ", dr.count_nan(list(df[itr])))
#print(list(map(dr.count_nan, lis)))
