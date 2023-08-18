# Скрипт для скачивания изображений с сайта riamediabank.ru

Этот скрипт позволяет скачивать изображения с сайта riamediabank.ru. Вы можете указать количество изображений для скачивания и скрипт загрузит их в указанную папку.

## Установка зависимостей

Перед использованием скрипта, убедитесь, что у вас установлены необходимые библиотеки. Если их нет, вы можете установить их, выполнив следующую команду:

`pip install requests beautifulsoup4`

## Как использовать
Скачайте репозиторий или скопируйте код из файла main.py.
Укажите свой пользовательский User-Agent в файле auth_temp.py, например:

`user_agent = "Мой_Пользовательский_Агент"`

Запустите main.py через командную строку:

`python main.py`

Введите количество изображений, которые вы хотите скачать.
Скрипт начнет скачивание изображений в папку downloaded_images.

## Примечание
Учтите, что использование скриптов для скачивания контента с веб-сайтов может нарушать правила сайта. Пожалуйста, убедитесь, что вы имеете право скачивать и использовать содержимое согласно правилам сайта.
