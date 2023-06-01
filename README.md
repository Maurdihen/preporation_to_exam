# Preparation for Exam

Проект представляет собой приложение Flask, которое включает в себя операции CRUD (Create, Read, Update, Delete) для заметок. Он использует SQLAlchemy для работы с базой данных и Marshmallow для сериализации объектов.

Это приложение предназначено для управления записями в базе данных. Пользователи могут добавлять, удалять, изменять и просматривать все записи из БД.

## Запуск проекта локально

Для развертывания проекта локально выполните следующие шаги:

1. Клонируйте репозиторий на ваш локальный компьютер.
2. Перейдите в корневую директорию проекта.
3. Выполните команду `docker-compose up --build -d` для запуска проекта.

## Доступ к приложению

Приложение развернуто на сервере и доступно по следующему адресу: [http://84.201.136.137/](http://84.201.136.137/)

## Использование приложения

Для входа в систему вм используйте следующие учетные данные:
- Имя пользователя: exam
- Пароль: 1

Пользователи могут добавлять, удалять, изменять и просматривать все записи из базы данных.

## Содержание

- [Основные технологии](#основные-технологии)
- [Развертывание с помощью Docker](#развертывание-с-помощью-docker)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Структура проекта](#структура-проекта)

## Основные технологии

- Python 98.2%
- Dockerfile 1.8%

## Развертывание с помощью Docker

В репозитории представлен файл `docker-compose-ci.yml`, который можно использовать для развертывания приложения. Файл определяет две службы: "api" и "pg". "api" служба базируется на образе Docker, который создается из репозитория, прослушивает порт 80 и зависит от службы "pg". "pg" служба базируется на образе postgres:latest, использует переменные окружения для установки пользователя, пароля и имени базы данных PostgreSQL, а также хранит данные базы данных в каталоге ./pg_data.

## GitHub Actions Workflow

В репозитории имеется файл `.github/workflows/action.yml`, который определяет рабочий процесс GitHub Actions для автоматической сборки и развертывания приложения при каждом push. Этот рабочий процесс выполняет следующие действия: сборка Docker образа с приложением, вход в Docker с использованием секретов DOCKER_USERNAME и DOCKER_TOKEN, push Docker образа в Docker Hub, клонирование кода на сервер, рендеринг конфигурации Docker и копирование на сервер, запуск приложения на сервере с использованием Docker Compose.

## Структура проекта

Проект имеет следующую структуру:
- `dao/` содержит классы Data Access Object (DAO) для работы с базой данных.
- `models/` содержит модели SQLAlchemy и схемы Marshmallow для сериализации данных.
- `setup_db.py` устанавливает соединение с базой данных.
- `.github/workflows/action.yml` определяет рабочий процесс GitHub Actions для CI/CD.
- `docker-compose-ci.yml` определяет конфигурацию Docker Compose для развертывания приложения.


