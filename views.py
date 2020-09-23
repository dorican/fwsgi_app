
# Запуск
# uwsgi --http :8000 --wsgi-file main.py

from wavy import render
from models import TrainingSite

site = TrainingSite()


def main_view(request):
    secret = request.get('secret_key', None)
    # Используем шаблонизатор
    courses = site.courses
    categories = site.categories
    print(categories)
    return '200 OK', render('index.html', categories=categories)


def create_category(request):
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        category_id = data.get('category_id')
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))
        new_category = site.create_category(name, category)
        site.categories.append(new_category)
        return '200 OK', render('create_category.html')
    else:
        categories = site.categories
        return '200 OK', render('create_category.html', categories=categories)


# def about_view(request):
#     # Просто возвращаем текст
#     return '200 OK', "About"


def contact_view(request):
    # Проверка метода запроса
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
        return '200 OK', render('contact.html')
    else:
        return '200 OK', render('contact.html')
