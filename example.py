from pprint import pprint

from python1c.core import ServerConnection
from python1c.apiodata import APIOdata

SERVER_INFO='http://192.168.0.18/'  # ip сервера
INFO_BASE='erp_dev'  # имя базы
DOCUMENT='Document'  # Набор сущностей
CATALOG='Catalog'
CATALOG_NAME='ЭтапПроизводства2_2'  # Имя каталога
CATALOG_WORK_STATION='ВидыРабочихЦентров'
USER_NAME='a_galkin'  # Имя пользователя
PASSWORD='Vhcrdoft123'  # Пароль

# Конектимся к 1С
server_info: str = SERVER_INFO  # ip сервера
info_base: str = INFO_BASE  # имя базы
base_name: str = CATALOG  # Набор сущностей
catalog_name: str = CATALOG_WORK_STATION  # Имя каталога
user_name: str = USER_NAME  # Имя пользователя
password: str = PASSWORD  # Пароль

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
