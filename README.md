## _Веб-Приложение для подбора домашних растений_
«Viva Flower Finder»: приложение, в котором пользователи могут подобрать себе растение, по критериям - сложность ухода/температурные содержания/полив и т.п.
Есть возможность открыть каждое растение и изучить подробную информацию о нем.
 
### Технологии:
Python, Django, PostgreSQL

### Запуск проекта на локальной машине:

- Клонировать репозиторий:
```
https://github.com/ElenaGlu/site.git
cd project
```
### Создайте и активируйте виртуальное окружение:
```
    python -m venv venv
    source venv/bin/activate     #для Linux
```
### В директории project создайте файл `.env` и заполните данными:
```
DJANGO_KEY_USER = 'key'
KEY_NAME = 'name'
KEY_USER = 'user'
KEY_PASSWORD = 'key'
```
### Установите требуемые зависимости:

Выполните команду в терминале 
```
pip install -r requirements.txt
```
### Наполните базу данных содержимым файла dump.sql из директории dump:

```
sudo -u postgres -i psql databasename < dump.sql

python manage.py migrate      #проверить миграции
```
### Запустите проект:

```
python manage.py runserver
```

- После запуска проект будут доступен по адресу: [http://localhost/](http://localhost/)
  
