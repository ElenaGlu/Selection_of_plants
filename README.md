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
DJANGO_KEY_USER = 'django-insecure-#x=(=j7e8kcz6h@x^yolqcky526ngg1=-zh&n9#5j2232t77#p'
KEY_NAME = 'vff'
KEY_USER = 'lena'
KEY_PASSWORD = '1'
```
### Установите требуемые зависимости

Выполните команду в терминале 
```
pip install -r requirements.txt
```

### Запустите проект

```
python manage.py runserver
```

- После запуска проект будут доступен по адресу: [http://localhost/](http://localhost/)
  
