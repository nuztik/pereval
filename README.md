Выполнение стажировки от SkillFactory.

Задача совместное создание приложения студентами для Федерации Спортивного Туризма России (ФСТР).

  Запрос от ФСТР:
    На сайте ФСТР ведётся база горных перевалов, которая пополняется туристами. После преодоления очередного перевала,
    турист заполняет отчёт в формате PDF и отправляет его на электронную почту федерации. Экспертная группа ФСТР получает 
    эту информацию, верифицирует, а затем вносит её в базу, которая ведётся в Google-таблице. Весь процесс очень неудобный и 
    долгий и занимает в среднем от 3 до 6 месяцев.
    
  Как ФСТР видит решение:
    ФСТР заказала разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке 
    данных о перевале и сократило время обработки запроса до трёх дней. Пользоваться мобильным приложением будут туристы. 
    В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет. 
    Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в 
    свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

Структура работы приложения:

  Доступно для пользователя в приложении:
    -Внесение информации о новом объекте.
    -Редактирование нового объекта, если еще он не отправлен на сервер ФСТР.
    -Заполнение данных пользователя.

  Связь с сервером:
    -Информация о статусе отправки.
    -Согласие пользователя с политикой обработки персональных данных.

  Данные для передачи на сервер:
    -Имя пользователя.
    -Почта и телефон пользователя.
    -Название перевала.
    -Координаты и высота перевала.
    -Фото перевала.
    -Status. Состояние обработки информации сотрудниками ФСТР.

Методы API для работы с JSON файлами:

  POST/submitData/
    Принимает JSON в теле запроса с информацией о перевале.

  GET/submitData/
    Получает 1 запись по ее id с выведением всей информации об перевале

  PATCH/submitData/
  Позволяет редактировать запись, если status='new'. Кроме полей относящихся к users.

  
  
