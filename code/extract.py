import pandas as pd
import xlrd
import entropy_weight
import numpy as np

for t in range(2010, 2017):
    print(t)
    dataframe = pd.read_excel("../data/Output/" + str(t) + ".xlsx")
    column_names_dup = list(dataframe.columns)
    column_names_tep = []
    column_names_pos = []
    for item in column_names_dup:
        item = item.split(".")[0]
        # print(item)
        column_names_tep.append(item)
    column_names = list(set(column_names_tep))
    column_names.sort(key=column_names_tep.index)

    left = 0
    for i in range(1, len(column_names_tep)):
        if(i == len(column_names_tep) - 1):
            column_names_pos.append((left, i))
            break
        if(column_names_tep[i] != column_names_tep[i-1]):
            column_names_pos.append((left, i-1))
            left = i

    # print(column_names_dup)
    # print(column_names_pos)

    item = column_names_pos[4]
    # print(item[0], item[1])
    dataset = dataframe.iloc[:, 63:90]
    # print(dataset)
    dataset = np.array(dataset)
    result = entropy_weight.entropy(dataset)
    # print(result.shape)

    dg = pd.DataFrame()
    dg['Id'] = dataframe['Id']
    dg['Id2'] = dataframe['Id2']
    dg['Geography'] = dataframe['Geography']
    for i in range(4, len(column_names_pos)):
        item = column_names_pos[i]
        dataset = np.array(dataframe.iloc[:, item[0]:item[1]])
        result = entropy_weight.entropy(dataset)
        dg[column_names[i]] = result

    dg.to_excel("../data/entropy/" + str(t) + "_entropy.xls")