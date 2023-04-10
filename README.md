# UPTRADER TEST_TASK
___

# Установка
* Склонируй репозиторий используя команду
```
git clone git@github.com:31nkmu/Neobis_Python_Auth_Project.git
```
* Создай виртуальное окружение используя команду
```
python3 -m venv <name of your environment> 
```

* Активируй виртуальное окружение
``` 
source <name of your environment>/bin/activate 
```

* Установи зависимости
``` 
pip install -r requirements.txt 
```

* Сделай миграции
```
  ./manage.py migrate
```
* Запусти свой проект
``` 
./manage.py runserver 
или
 python3 manage.py runserver 
``` 
---
Добавление новых разделов в меню возможно через панель администратора

Ссылка на вложенное меню должна начинаться с ссылки на родителя.
Пример: меню "Контакты" вложенное в раздел "Информация" (site_name/info/) должно иметь ссылку site_name/info/contacts

Количество вложенных списков не ограничено