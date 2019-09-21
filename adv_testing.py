
import numpy as np
import dataret as dr
import pandas as pd

frame = dr.get_data('clean_data.xls')

def divide(item):
    item_frame = frame[frame['Item_Id'] == item]
    return item_frame

def get_reference_items(frame_list):
    ref_list = []
    for fr in frame_list:
        src = list(fr['source'])
        flag = True
        for itr in src:
            if itr == 'test':
                flag = False
                break
        if flag:
            ref_list.append(fr)

    return ref_list



def show_frames(ref_frames, type, loc):
    #colus = ref_frames[0].columns
    item_mrp = []
    item_sales = []
    for itr in ref_frames:
        itr = itr[ (itr['Outlet_Type'] == type) & (itr['Outlet_Loc_Type'] == loc)]
        shape = itr.shape
        if shape[0] > 0:
            temp_item_mrp = list(itr['Item_MRP'])
            item_mrp = item_mrp +temp_item_mrp
            temp_item_sales = list(itr['Item_Outlet_Sales'])
            item_sales = item_sales + temp_item_sales
            #print(itr[['Item_Visibility', 'Item_MRP', 'Item_Outlet_Sales']])
            #print(itr[['Item_Id', 'Item_Visibility', 'Item_MRP', 'Item_Outlet_Sales']])
    #print(fr['Item_Id', 'Item_Visibility', 'Item_MRP', 'Item_Outlet_Sales'])
    return item_mrp, item_sales

if __name__ == '__main__':
    item_id_list = dr.get_unqiue_list(list(frame['Item_Id']))
    item_frame_list = list(map(divide, item_id_list))
    ref_frames = get_reference_items(item_frame_list)
    mrp, sales = show_frames(ref_frames, 'Supermarket Type1', 'Tier 2')
    result = []
    for itr in range(len(mrp)):
        result.append(sales[itr] / mrp[itr])
    #print(sum(result)/len(result))


