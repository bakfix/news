# news
В данной версии Django-приложения релизовано следующее 

1. CRUD Новостей с данными:
• Заголовок новости
• Главное изображение
• Превью-изображение (автоматически генерировать из главного изображения путём
уменьшения до 200px по наименьшей стороне)
• Текст новости
• Дата публикации
• Автор новости

2. Просмотр и редактирование Новостей с rich-текстом (подсказка: summernote) в админке.

3. Импорт Примечательных мест из xlsx-файла с данными:
• Название места
• Гео-координаты места (точка)
• Рейтинг (от 0 до 25)
4. Просмотр и редактирование Примечательных мест в админке, координаты получать с
помощью виджета карты.

Итак, кратко по важным моментам

models.py - в моделях добавлено представление News и Place. Класс News отвечает за создание новости, функция def create_thumbnail берет из главного изображения и уменьшает до 200px.
Класс Place ответственен за добавление примечательных мест, а также визуальное отображение с помощью geomap (никогда не пользуйтесь GDAL, мучительная библиотека, которая не могла у меня поставиться). 

import_places - файл,отвечающий за передачу файла xlsx в модель Place

admin.py - файл, который отображает админскую панель, также в него добавлены классы для редактора, и отображения. Проще говоря для визуализации

serialazers - сериализатор с подключенной библиотекой DRF

views.py - классы для обработки запросов в API
Это все было про приложение 

В проекте кроме путей и дефолтных изменений в настройках были добавлены библиотеки + обработки медиафайлов и по мелочи

Также добавлен файл newspage.html - это не постоянный файл, он для того, чтобы посмотреть как отображаются новости из API на предполагаемом сайте.
Также по требованию добавлен метод удаления картинок, который остаются после удаления новости
