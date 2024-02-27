# Інструкція до запуску веб-сайту для обробки файлів з числами
Цей веб-додаток дозволяє користувачам завантажувати файли з числами, автоматично обчислює основні статистичні показники для цих чисел (максимум, мінімум, медіана, середнє) та знаходить найбільші зростаючі та спадаючі послідовності серед цих чисел.

## Передумови
Перш ніж запускати сайт, вам потрібно встановити наступне програмне забезпечення:

- [Python](https://www.python.org/downloads/) (версія 3.6 або новіша)
- Flask
- Numpy

Це можна зробити через командний рядок або термінал використовуючи pip (після встановлення Python):

`pip install flask numpy`

## Запуск сервера
Для запуску сервера виконайте наступні кроки:

1. Клонуйте репозиторій або завантажте вихідний код на свій комп'ютер.
2. Відкрийте термінал або командний рядок і перейдіть до папки з проектом.
3. Виконайте команду `python app.py` для запуску Flask-сервера.
4. Після цього сервер має запуститися, і ви побачите повідомлення з адресою, за якою доступний веб-додаток (зазвичай http://127.0.0.1:5000/).

## Користування додатком
Для користування додатком виконайте наступні кроки:

1. Відкрийте веб-переглядач та перейдіть за адресою, яку вказав сервер під час запуску (зазвичай http://127.0.0.1:5000/).

![image](https://github.com/Friendly-Neighborhood/large_number_analysis/assets/68468538/2bc7ae16-4bad-4534-a3c2-9afa1ac8ef97)


2. На головній сторінці ви побачите форму для завантаження файлу. Клікніть на кнопку "Обрати файл" та виберіть файл з числами, який ви хочете обробити. Файл має містити одне число на рядок.
3. Після вибору файлу натисніть кнопку "Завантажити", щоб відправити файл на сервер для обробки.
4. Дочекайтеся, поки сервер обробить файл. Під час обробки на екрані з'явиться анімація завантаження ().

![image](https://github.com/Friendly-Neighborhood/large_number_analysis/assets/68468538/7cee9734-8b97-4e63-902c-22b1af2b3785)

5. Після завершення обробки на сторінці з'являться результати: максимум, мінімум, медіана, середнє значення, найбільша зростаюча послідовність та найбільша спадаюча послідовність чисел.

![image](https://github.com/Friendly-Neighborhood/large_number_analysis/assets/68468538/d0be369f-04c4-4b30-8870-37eb58fe6c6c)

