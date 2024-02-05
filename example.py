from pprint import pprint

from python1c.core import ServerConnection
from python1c.apiodata import APIOdata

# Конектимся к 1С
server_info: str = 'ip'  # ip сервера
info_base: str = 'erp_dev'  # имя базы
base_name: str = 'Document'  # Набор сущностей
catalog_name: str = 'ЭтапыПроизводства'  # Имя каталога
user_name: str = 'login'  # Имя пользователя
password: str = 'password'  # Пароль

connection: ServerConnection = ServerConnection(server_info,
                                                info_base,
                                                base_name,
                                                catalog_name,
                                                user_name,
                                                password
                                                )

# Создаем экземпляр класса отвечающего за работу с ODATA
cpl = APIOdata(connection)

# Получаем конкретный объект из 1С
# get_query = cpl.get('dc1e12ec-a6bd-11ec-aa3b-ac1f6bd30991')

# Получаем список объектов из 1С
queryset = cpl.list(top=10, orderby='Description desc', select='Description')

# Редактируем объект в 1С
data = {
    'ЗанимаемаяМощность': 150,
}
# update_request = cpl.edit(guid='dc1e12ec-a6bd-11ec-aa3b-ac1f6bd30991', data=data)

# Выводим в консоль
pprint(queryset)
