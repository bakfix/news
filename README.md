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

Также добавлен файл newspage.html - это не постоянный файл, он для того, чтобы посмотреть как отображаются новости из API.