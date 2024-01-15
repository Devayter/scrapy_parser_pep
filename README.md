# Парсер документации Python

## Обзор

Этот парсер документации Python разработан для извлечения информации с официального веб-сайта [Python](https://docs.python.org).

### Возможности

* Парсинг информации о существующих (PEP), включая статусы и количество.

### Использование

1. Клонирование репозитория:
`git clone git@github.com:Devayter/scrapy_parser_pep.git`
`cd scrapy_parser_pep`
2. Установка зависимостей:
`pip install -r requirements.txt`
3. Запуск парсера:
`cd pep_parse`
`scrapy crawl pep`

### Вывод данных

Данные сохраняются csv формате в базовой директории в папке `results`

## Стек технологий

* Язык программирования: Python
* Веб-скрапинг и парсинг Scrapy

## Авторы

* [Павел Рябов](https://github.com/Devayter/)
