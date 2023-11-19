# pereval
Выполнение стажировки от SkillFactory.

Задача совместного создания приложения для студентов для Федерации Спортивного Туризма России (ФСТР).

Запрос от ФСТР: На сайте ФСТР проводится база горных перевалов, которая заполняется туристами. После завершения очередного перевала турист заполняет отчёт в формате PDF и отправляет его на электронную почту федерации. Экспертная группа ФСТР получает эту информацию, верифицирует, а затем вносит ее в базу, которая ведет в Google-таблице. Весь процесс очень неудобный и долгий и занимает в среднем от 3 до 6 месяцев.

Как ФСТР видит решение: ФСТР организовала создание мобильного приложения для Android и IOS, которое упростило задачу туристам по отправке данных о перевале и сократило время обработки запросов до трех дней. Пользуйтесь мобильными приложениями для туристов. В горах они будут переносить данные о перевале в приложении и отправлять их в ФСТР, как только будет обеспечен доступ в Интернет. Модератор из федерации будет проверять и вносить в сайты информацию о данных, полученную от пользователей, а те, в свою очередь, смогут увидеть в мобильном приложении статус модерации и найти ресурсы с внешёнными другими объектами.

Структура работы приложения:

Доступно для пользователя в приложении: - Внесение информации о новом объекте. -Редактирование нового объекта, если он еще не отправлен на сервер ФСТР. -Заполнение данных пользователя.

Связь с сервером: -Информация о статусе сообщения. -Согласие пользователя с политической обработкой медицинских данных.

Данные для передачи на сервер: -Имя пользователя. -Почта и телефон пользователя. -Название перевала. -Координаты и высота перевала. -Фото перевала. -Положение дел. Состояние обработки информации сотрудниками ФСТР.

Методы API для работы с JSON файлами:

POST/submitData/ Принимает JSON в теле запросе с информацией о перевале.

GET/submitData/ Получает 1 запись по ее идентификатору с выведением всей информации об перевале

PATCH/submitData/ устанавливает резервную запись, если status='new'. Кроме полей, относящихся к пользователям.
