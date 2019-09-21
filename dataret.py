import pandas as pd

#data retrival area


def generate_excel(df, filename = 'temp.xls'):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer,'Sheet1',index=False)
    writer.save()


def check_same(frame, col_ind, tup_name, ind):
    for itr in range(len(tup_name)):
        if tup_name[itr] != frame[col_ind[itr]][ind]:
            return False
    return True


def get_all_att(df, col_name, tup_name ,excel = False, datatype = "list"):
    col_list = list(df.columns)
    result = []
    frame = list(map(lambda x : list(df[x]),col_list))
    #print(frame[1])
    if(datatype == "var"):
        index = col_list.index(col_name)
        for itr in range(len(frame[index])):
            if frame[index][itr] == tup_name :
                result.append(list(map(lambda x: frame[x][itr], range(len(col_list)))))

    else:
        index = col_list.index(col_name[0])
        col_ind = list(map(lambda x : col_list.index(x), col_name))
        for itr in range(len(frame[index])):
            if check_same(frame, col_ind, tup_name, itr):
                result.append(list(map(lambda x: frame[x][itr], range(len(col_list)))))

    result_frame = pd.DataFrame(result, columns=col_list)
    if(excel == True):
        generate_excel(result_frame)
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

