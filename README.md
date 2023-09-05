# NimaxTestTask

Тестовое задания для компании "Nimax".

Запуск проекта через Docker:

1. Собираем проект
```
docker-compose build
```

2. Запускаем контейнеры
```
docker-compose up -d
```

3. Optional. Остановить контейнеры
```
docker-compose down
```

После этого проект будет запущен на 127.0.0.1:8000

Swagger для просмотра API: http://127.0.0.1:8000/api/v1/swagger/

API для категорий товаров: http://127.0.0.1:8000/api/v1/categories/

API для товаров: http://127.0.0.1:8000/api/v1/items/
