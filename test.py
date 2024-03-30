date_str = '2024-03-29'
date_list = list(date_str)
last_digit = int(date_list[-1])  # преобразуем последний символ в число
last_digit -= 1  # уменьшаем на 1
date_list[-1] = str(last_digit)  # преобразуем обратно в строку и заменяем в списке
updated_date_str = ''.join(date_list)
print(updated_date_str)