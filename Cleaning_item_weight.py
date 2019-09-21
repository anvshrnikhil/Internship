
import dretrive as dr
import pandas as pd

def clean_nan(itemid, item, item_weight, df):

    count_not_nan = 0
    count_nan = 0
    weight = 0

    for itr in range(len(item)):
        if pd.isna(item_weight[item[itr]]):
            count_nan += 1
        else:
            count_not_nan += 1
            weight = item_weight[item[itr]]

    if count_nan > 0 and count_not_nan > 0 :
        for itr in range(len(item)):
            df.loc[item[itr], 'Item_Weight'] = weight

    return df


def generate_excel(df):
    writer = pd.ExcelWriter('ctrain.xls')
    df.to_excel(writer,'Sheet1',index=False)
    writer.save()


def clean_Item_fat_content(df):

    item_fat_content = list(df['Item_Fat_Content'])

    for itr in range(len(item_fat_content)):

        if item_fat_content[itr] == "Low Fat" or item_fat_content[itr] == "low fat" or item_fat_content[itr] == "LF" :
            df.loc[itr,'Item_Fat_Content'] = "Low Fat"
        else:
            df.loc[itr,'Item_Fat_Content'] = "Regular"

    return df

#stub
if __name__ == '__main__':

    df  = dr.get_data('train.xls')
    item_id = dr.get_unqiue_list(list(df['Item_Id']))
    item_id_list = list(dr.get_req_att(df, 'Item_Id'))
    item_weight = list(dr.get_req_att(df, 'Item_Weight'))
    print(dr.count_nan(item_weight))
    item_fat_content = list(dr.get_req_att(df, 'Item_Fat_Content'))
    item_type = list(dr.get_req_att(df, 'Item_Type'))
    for outer_itr in item_id:
        temp_list = []
        for itr in range(len(item_id_list)):
            if item_id_list[itr] == outer_itr:
                #print(item_id_list[itr], item_weight[itr], item_fat_content[itr], item_type[itr])
                temp_list.append(itr)

        df = clean_nan(outer_itr, temp_list, item_weight, df)
    item_weight = list(df['Item_Weight'])
    print(dr.count_nan(item_weight))

    for itr in range(len(item_weight)):
        if pd.isna(item_weight[itr]):
            print(itr, item_id_list[itr], item_type[itr], item_fat_content[itr])

    df = clean_Item_fat_content(df)

    #generate_excel(df) # pls uncoment to generate new excel file
