import pandas as pd

sovpad_vkusi = pd.read_excel('data\TABAKI2.xlsx')
black_bern = pd.read_excel('data\BlackBern.xlsx')

def result(msg):

    words_list = msg.split(", ")
    print(words_list)
    result = []

    for i in range(len(words_list[:-1:])):

        first = words_list[i]
        second = words_list[i+1]
        print("INPUT:", first, second)

        name_of_col1 = black_bern.columns[black_bern.isin([first]).any()][0]
        name_of_col2 = black_bern.columns[black_bern.isin([second]).any()][0]
        print("OUTPUT:", name_of_col1, name_of_col2)

        idx = sovpad_vkusi[sovpad_vkusi.iloc[:, 0] == name_of_col1].index[0]
        print("IDX:", idx)   
        col_name = sovpad_vkusi.columns[sovpad_vkusi.columns.str.contains(name_of_col2)][0] 
        print("COLNAME", col_name)

        result.append(sovpad_vkusi.loc[idx, col_name])
    return result    
           
if __name__ == "test":
    result("Irish cream, Basillic, Haribon, Pistachio ice snow")