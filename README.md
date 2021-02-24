## Задание

### Основное

· Создать сервис с веб-апи для сохранения изображений и тегов к ним. Сервис должен позволять получать список изображений и их тегов, фильтрацию изображений по тегам и скачивание/просмотр изображений.

· Для хранения информации (возможно и самих изображений) использовать postgres.

### Дополнительное

· Создать Dockerfile и docker-compose.yml для запуска сервиса и БД.

· Описать методы api в readme.md проекта.

· Создать cli утилиту для работы с веб-апи.

## Методы API

#### url: http://localhost:8000/api/images/

GET: get all images and their tags

![Image alt](https://github.com/ZharkovMihail/test_task_KT/blob/master/screenshots_for_readme/get_all_pictures.png)

POST: post image and tags


            body:
                upload:  image.jpg  
                tags:    tag1, tag2, tag3 ...


![Image alt](https://github.com/ZharkovMihail/test_task_KT/blob/master/screenshots_for_readme/post_new_picture.png)

#### url: http://localhost:8000/media/uploads/[str:file_name]

GET: get picture

![Image alt](https://github.com/ZharkovMihail/test_task_KT/blob/master/screenshots_for_readme/get_picture.png)

DELETE: delete picture from database and from dir media

![Image alt](https://github.com/ZharkovMihail/test_task_KT/blob/master/screenshots_for_readme/delete.png)

PATCH: change picture\`s tags to new

            body:
                tags:   new_tag1, new_tag2, new_tag3 ...

![Image alt](https://github.com/ZharkovMihail/test_task_KT/blob/master/screenshots_for_readme/patch.png)

#### url: http://localhost:8000/api/images_by_tags

GET: get images by tags

            body:
                tags:  tag1, tag2, tag3 ...

![Image alt](https://github.com/ZharkovMihail/test_task_KT/blob/master/screenshots_for_readme/get_picture_by_tags1.png)

![Image alt](https://github.com/ZharkovMihail/test_task_KT/blob/master/screenshots_for_readme/get_picyure_by_tags2.png)

## Запуск docker
            
            шаг0: docker-compose run web python3 manage.py midrate
            
            шаг1: docker-compose up

### TODO

* настроить работу не только с jpeg файлами
* переписать некоторые методы с использованием serialisers
* переписать на классы
* добавить обработку корректности входных данных
