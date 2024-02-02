from core import ServerConnection

# Конектимся к 1С
server_info: str = 'http://192.168.0.18/'  # ip сервера
info_base: str = 'erp_dev'  # имя базы
base_name: str = 'Catalog'  # Набор сущностей
catalog_name: str = 'ЭтапыПроизводства'  # Имя каталога
user_name: str = 'a_galkin'  # Имя пользователя
password: str = 'Vhcrdoft123'  # Пароль

connection: ServerConnection = ServerConnection(server_info,
                                                info_base,
                                                base_name,
                                                catalog_name,
                                                user_name,
                                                password
                                                )

