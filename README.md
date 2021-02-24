## Задание

### Основное

· Создать сервис с веб-апи для сохранения изображений и тегов к ним. Сервис должен позволять получать список изображений и их тегов, фильтрацию изображений по тегам и скачивание/просмотр изображений.

· Для хранения информации (возможно и самих изображений) использовать postgres.

### Дополнительное

· Создать Dockerfile и docker-compose.yml для запуска сервиса и БД.

· Описать методы api в readme.md проекта.

· Создать cli утилиту для работы с веб-апи.

## Методы API

### url: http://localhost:8000/api/images/

GET: get all images and their tags

![Image alt](https://github.com/ZharkovMihail/test_task_KT/blob/master/screenshots_for_readme/get_all_pictures.png)

POST: post image and tags
            
            body:
                upload:  image.jpg  
                tags:    tag1, tag2, tag3 ...

![Image alt](https://github.com/ZharkovMihail/test_task_KT/blob/master/screenshots_for_readme/post_new_picture.png)
