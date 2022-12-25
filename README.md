# MIPT: Dataton 2022. "Data Detectives"
____
### Тема: Маркетплейсы
### Задача: Сбор и анализ данных из маркетплейсов для создания предсказательной модели на примере категории электроники (ноутбуки)

["Data Detectives" - информация о работе на Miro](https://miro.com/app/board/uXjVP4dIqYE=/?moveToWidget=3458764541734187484&cot=14)
### Члены команды:
- Козырева Алина
- Переверзев Петр
- Ли Диана
- Иванов Кирилл
- Остапенко Мария
- Виноградов Дмитрий
____
### Cтруктура репозитория: 
* main.py - реализует вызов необходимых функций
* browser.py - имитирует действия реального пользователя при работе с браузером
* config.py - файл с url для скраппинга
* data - сырые собранные данные
* marketplaces/base.py - содержит реализацию класса BaseFunctions - основа для скраппинга
* marketplaces/mvideo_base.py - содержит реализацию класса Mvideo(BaseFunctions) для скраппинга данных с [М.Видео](https://www.mvideo.ru/product-list-page/f/tolko-v-nalichii=da?q=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA&category=noutbuki-118 "Данные по ноутбукам")
* locators/mvideo.py - содержит фитчи для парсинга [М.Видео](https://www.mvideo.ru/product-list-page/f/tolko-v-nalichii=da?q=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA&category=noutbuki-118 "Данные по ноутбукам")
* scraper.ipynb - альтернативный web-scraper
_____
### Описание задачи для анализаа:
Сформировать для поставщика, желающего разместить на маркетплейсе ноутбуки, рекомендации по выбору моделей ноутбуков и их стоимости, чтобы получить максимальную выгоду.
_____
### Источники данных:
- [М.Видео](https://www.mvideo.ru/product-list-page/f/tolko-v-nalichii=da?q=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA&category=noutbuki-118 "Данные по ноутбукам")
- [Amazon](https://www.amazon.com/s?k=laptop&crid=2JUKYBAPLWFUW&page={} "Данные по ноутбукам")
- [Wildberries](https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=ноутбук "Данные по ноутбукам")
- [DNS](https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/?stock=now-today-tomorrow-later-out_of_stock&order=6 "Данные по ноутбукам") (в плане)

____
### Преварительный результат: 
1. Разработан инструмент web-scraper 
2. Разработан альтернативный web-scraper 
3. Выбраны фитчи ноутбуков для скраппинга
4. Применен web-scraper на сайте [М.Видео](https://www.mvideo.ru/product-list-page/f/tolko-v-nalichii=da?q=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA&category=noutbuki-118 "Данные по ноутбукам")
5. Применен альтернативный web-scraper на сайтах [Amazon](https://www.amazon.com/s?k=laptop&crid=2JUKYBAPLWFUW&page={} "Данные по ноутбукам"), [Wildberries](https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=ноутбук "Данные по ноутбукам")
6. Собрана часть данных и записана в файл

#### В плане
1. Очистка данных и формирование финального датасета
2. Анализ данных, создание предсказательной модели
3. Визуальное представление результатов анализа