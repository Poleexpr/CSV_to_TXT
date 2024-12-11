from csv import DictReader

# данные парсятся из csv-файла и преобразуются в список словарей
with open("web_clients_correct.csv", 'r') as csv_file:    
    dict_reader = DictReader(csv_file)
    clients = list(dict_reader)

# формируется текстовое описание по шаблону и данные записываются в txt-файл
with open("web_clients_correct.txt", 'w') as txt_file:  
    for client in clients:  
        txt_file.write(f"Пользователь {str(client['name'])} {'женского' if client['sex'] == 'female' else 'мужского'} пола, {str(client['age'])} лет совершил{'а' if client['sex'] == 'female' else ''} покупку на {str(client['bill'])} у.е. с {'мобильного' if client['device_type'] == 'mobile' or client['device_type'] == 'tablet' else ''} браузера {str(client['browser'])}. Регион, из которого совершалась покупка: {str(client['region'])}.\n")


