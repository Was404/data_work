import pandas as pd

sovpad_vkusi = pd.read_excel('TABAKI2.xlsx')
black_bern = pd.read_excel('6ea62e8d25dba044.xlsx')

sovpad_vkusi

#col_shugar = sovpad_vkusi['Сладкий']
col_sour = sovpad_vkusi['Кислый']
col_fresh = sovpad_vkusi['Свежий']
col_grassy = sovpad_vkusi['Травянистый']
col_tart = sovpad_vkusi['Терпкий']
col_spicy = sovpad_vkusi['Пряный']
col_coffee = sovpad_vkusi['Кофейный']
col_gastronomy = sovpad_vkusi['Гастрономия']
col_alcoholic = sovpad_vkusi['Алкогольный']
col_chocolate = sovpad_vkusi['Шоколадный']
col_pastries = sovpad_vkusi['Выпечка']
col_nutty = sovpad_vkusi['Ореховый']
col_bitter = sovpad_vkusi['Горький']
col_ice = sovpad_vkusi['Лёд']
col_mint = sovpad_vkusi['Мята']
col_coniferous = sovpad_vkusi['Хвойный']
col_sugary = sovpad_vkusi['Приторный']

# Будем искать вкусы, у который "да"
#result = sovpad_vkusi.columns[sovpad_vkusi.isin(['Да']).any()]
#print(result)
has_yes = sovpad_vkusi.isin(['Да']).any()
col = has_yes.any().idxmax()
row = has_yes[col].idxmax()
result = sovpad_vkusi.loc[row, col]

print(result)
