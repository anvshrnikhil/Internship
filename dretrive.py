
import pandas as pd

#data retrival area

def generate_excel(df):
    writer = pd.ExcelWriter('temp.xls')
    df.to_excel(writer,'Sheet1',index=False)
    writer.save()


def get_all_att(df, col_name, tup_name ,excel = False):
    #print(datetime.datetime.now())
    col_list = list(df.columns)
    result = []
    index = col_list.index(col_name)
    count = 0
    frame = list(map(lambda x : list(df[x]),col_list))
    for itr in range(len(frame[index])):
        if frame[index][itr] == tup_name :
            result.append(list(map(lambda x: frame[x][itr], range(len(col_list)))))
            count += 1

    result_frame = pd.DataFrame(result, columns=col_list)
    if(excel == True):
        generate_excel(result_frame)
    #print(datetime.datetime.now())
    return result_frame

def get_data(file_name):

	df = pd.read_excel(file_name)
	return df

def get_req_att(data_frame, att_list):

	return data_frame[att_list]


def get_unqiue_list(data)->list:

	return list(set(data))

def count_nan(list_):
	count = 0
	for itr in list_:
		if pd.isna(itr):
			count += 1
	return count

