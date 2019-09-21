
#predict data

import matplotlib.pyplot as plt
import pandas as pd
import dataret as dr

#global
t3_st1 = 15.28
t3_st2 = 11.63
t3_st3 = 23.11
t3_st0 = 8.60

t1_st0 = 5.99
t1_st1 = 24.83

t2_st1 = 16.03

frame = dr.get_data('clean_data.xls')

def divide(item):
    item_frame = frame[frame['Item_Id'] == item]
    return item_frame

if __name__ == '__main__':
    '''
    item_id_list = dr.get_unqiue_list(list(frame['Item_Id']))
    item_frame_list = list(map(divide, item_id_list))
    test_frame = frame[frame['source'] == 'test']
    '''
    for itr in range(len(frame['Item_Id'])):
        if frame.loc[itr, 'source'] == 'test':
            if frame.loc[itr, 'Outlet_Loc_Type'] == 'Tier 1':
                if frame.loc[itr, 'Outlet_Type'] == 'Grocery Store':
                    frame.loc[itr, 'Item_Outlet_Sales'] = t1_st0 * frame.loc[itr, 'Item_MRP']
                else: #if frame.loc[itr, 'Outlet_Type'] == 'Grocery Store':
                    frame.loc[itr, 'Item_Outlet_Sales'] = t1_st1 * frame.loc[itr, 'Item_MRP']

            elif frame.loc[itr, 'Outlet_Loc_Type'] == 'Tier 2':
                frame.loc[itr, 'Item_Outlet_Sales'] = t2_st1 * frame.loc[itr, 'Item_MRP']


            else:#if frame.loc[itr, 'Outlet_Loc_Type'] == 'Tier 1':
                if frame.loc[itr, 'Outlet_Type'] == 'Grocery Store':
                    frame.loc[itr, 'Item_Outlet_Sales'] = t3_st0 * frame.loc[itr, 'Item_MRP']
                elif frame.loc[itr, 'Outlet_Type'] == 'Supermarket Type1':
                    frame.loc[itr, 'Item_Outlet_Sales'] = t3_st1 * frame.loc[itr, 'Item_MRP']
                elif frame.loc[itr, 'Outlet_Type'] == 'Supermarket Type2':
                    frame.loc[itr, 'Item_Outlet_Sales'] = t3_st2 * frame.loc[itr, 'Item_MRP']
                else: #if frame.loc[itr, 'Outlet_Type'] == 'Supermarket Type1':
                    frame.loc[itr, 'Item_Outlet_Sales'] = t3_st3 * frame.loc[itr, 'Item_MRP']


    frame.to_excel('result.xlsx',index=False)
