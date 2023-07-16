import pandas as pd

sovpad_vkusi = pd.read_excel('data\TABAKI2.xlsx')
black_bern = pd.read_excel('data\BlackBern.xlsx')

def result(msg):
    msg.strip().split()
    extracted_words = []
    for i in msg:
        # Удаляем возможную пунктуацию в начале и конце слова
        msg.strip(",.?!-\"\'")
        extracted_words.append(i)
    # Возвращаем список извлеченных слов
    #print(extracted_words)
    result = []
    for i in range(len(extracted_words)):
        exec(f'var_{i} = extracted_words[i]')
        extracted_words[i] = black_bern.columns[black_bern.isin([extracted_words[i]]).any()][0] # [0] используется, чтобы выбрать первый элемент списка (если он есть)
        extracted_words[i+1] = black_bern.columns[black_bern.isin([extracted_words[i+1]]).any()][0] 
           
        idx = sovpad_vkusi[sovpad_vkusi.iloc[:, 0] == extracted_words[i]].index[0]
        # найти название первого столбца, содержащего name_of_col2
        col_name = sovpad_vkusi.columns[sovpad_vkusi.columns.str.contains(extracted_words[i+1])][0]
        result.append(sovpad_vkusi.loc[idx, col_name])
    return result    
           
if __name__ == "test":
    print(result("Сладкий, Кислый, Терпкий"))