# api_final
api final
API для моего проекта YaTube 

Описание проекта
----------
API для проекта социальной сети. 
Реализована возможность добавления, удаления и изменения 
постов и комментариев. Настроена пагинация и права доступа
для авторизированных и неавторизированных пользователей.

# Как запустить проект:
### Клонировать репозиторий c сайта GitHub.com:
`git clone git@github.com:Japrojah/api_final_yatube.git`\

### Перейти в репозиторий проекта на рабочем месте:
`cd api_final_yatube`

### Cоздать и активировать виртуальное окружение:
`python -m venv venv`\

### Для Windows:
`source venv/Scripts/activate`

### Для Linux & macOS
`source venv/bin/activate`

### Установить зависимости из файла requirements.txt:
`python -m pip install --upgrade pip`\
`pip install -r requirements.txt`

### Выполнить миграции:
`python manage.py migrate`

### Запустить проект:
`python manage.py runserver`