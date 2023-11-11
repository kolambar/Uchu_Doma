Установка Docker и Docker Compose:

    Убедитесь, что у вас установлен Docker и Docker Compose. Если нет, вы можете следовать инструкциям по установке 
    на официальном сайте Docker: Установка Docker и Установка Docker Compose.

Клонирование проекта:

    Склонируйте репозиторий с проектом на свой локальный компьютер.

Настройка окружения:

    В корневой папке проекта создайте файл с именем .env и укажите в нем переменные окружения. Например:
    DATABASES_NAME=uchu_doma
    DATABASES_USER=postgres
    DATABASES_PASSWORD=6002

Запуск приложения:

    Откройте терминал в корневой папке проекта и выполните следующие команду:
    docker-compose up --build

    Эта команда построит Docker образы и запустят все сервисы, включая Redis, PostgreSQL, Django приложение, 
    Celery worker и Celery beat.