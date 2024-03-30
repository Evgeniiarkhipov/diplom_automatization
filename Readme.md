# Тестирование сайта https://runa-land.ru/
## Тестовый фреймворк:
```
Runa_land
  > pages
     > application_page.py   # Файл с классом для работы с заявкой на тур
     > feedback_page.py      # Файл с классами для работы со страницей обратной связи
     > locators.py           # Файл содержащий локаторы элементов страниц
     > testing_data.py       # Файл содержащий тестовые данные
  > config.py                # Файл с конфигурационными данными
  > test.py                  # Файл с тестами для автоматизированного тестирования
  > Readme.md                # Файл с описанием проекта и инструкциями
```

## Описание:
1. **`Runa_land`**: Главная папка проекта.
2. **`pages`**: Папка, содержащая файлы, связанные с веб-страницами.
    - **`application_page.py`**: Файл с классом для работы с заявкой на тур.
    - **`feedback_page.py`**: Файл с классами для работы со страницей обратной связи.
    - **`Locators.py`**: Файл, содержащий локаторы элементов страниц. Локаторы используются для поиска и взаимодействия с элементами на веб-страницах. 
    - **`testing_data.py`**: Файл содержащий тестовые данные для отправки заявки на тур, а также для заполнения обратной связи.
3. **`config.py`**: Файл с конфигурационными данными. Информация об URL-адресах, учетных данных, настройках тестирования и т.д.
4. **`test.py`**: Файл с автоматизированными тестами. Реализовация тест-кейсов, использующие классы и методы из файлов в папке `pages`.
5. **`Readme.md`**: Файл с описанием проекта и инструкциями.

Эта структура проекта помогает организовать код и ресурсы таким образом, чтобы проект был легко понятен и масштабируем.