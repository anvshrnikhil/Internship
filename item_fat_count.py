import dretrive as dr

df = dr.get_data('train.xls')
df = dr.get_req_att(df, ['Item_Type', 'Item_Fat_Content'])

item_list = dr.get_unqiue_list(df['Item_Type'])
print(item_list)
print("Length : ",len(item_list))

item_fat_list = dr.get_unqiue_list(df['Item_Fat_Content'])

print(item_fat_list)
print("Fat types : ", len(item_fat_list))
