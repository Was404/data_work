# data_work
Задача: В первой таблице перечислены вкусы по названиям столбцов и по строкам первой таблицы. Далее содержание таблиц обременяется в пересечении вкусов, содержащий в себе "Да", "Нет" "Возможно". Во второй таблице перечислены названия табаков по столбцам со вкусами. Вывести ответ "Да" "Нет" "Возможно" исходя из выбора двух вкусов табака. 
__Как работает?__
В этой задаче мы смешиваем по вкусу два разных(или не разных) табака. Получаем на вход названия табаков. Далее в таблице производителя табака ищем полученные названия и берём названия столбцов в которых они находятся. Далее, когда получили уже два вкуса, будем работать со второй таблицей с "да, нет" и т.д. . Ищем первый вкус по названиям столбцов начиная со второго, а второй вкус по строкам в первом столбце так как нам дана таблица у которой вкусы "разбиты по осям XY" . Находим первые попавшиеся и по пересечению получаем ответ. Всё. 
