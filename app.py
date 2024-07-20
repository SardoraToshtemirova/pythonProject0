from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Одежда'
    img = '/static/images/5ead0aaaa2069Modulkassa-956.jpg'
    href = '/GLAMOUR'
    model = 'Одежда GLAMOUR'
    return render_template("index.html", title = title, img = img, href = href, model = model)



@app.route('/shoes')
def shoes():
    shoes_list = [
        {'model': 'Кеды BASCONE', 'size':42, 'price':50},
        {'model': 'Туфли GUCCI', 'size':40, 'price':99},
        {'model': 'Туфли VITACI', 'size':41, 'price':70}]
    return render_template("shoes.html", shoes_list = shoes_list, title = 'Обувь' )


@app.route('/jackets')
def jackets():
    jackets_list = [
        {'model': 'Куртка TERRA PRO', 'size':48, 'price':70},
        {'model': 'Куртка джинсовая YUE YUE', 'size':42, 'price':55},
        {'model': 'Куртка джинсовая LING GA', 'size':44, 'price':85}]
    return render_template("jackets.html", jackets_list = jackets_list, title = 'Куртки')


@app.route('/picture')
def picture():
    title = 'Одежда GLAMOUR'
    product =  {'description': 'Одежда играет огромную роль в жизни каждого человека.С ее помощью можно создавать стильные образы,которые будут бросаться в глаза прохожим на улицах,  коллегам в компании и другим людям. ',
'img' : '/static/images/124.jpg',
 'price': 40}
    return render_template("picture.html", title = title, product = product)


@app.errorhandler(404)
def page_not_found(e):
    title = 'Страница не найдена'
    text = 'Такой страницы не существует'
    return render_template('404.html', title = title, text = text), 404


if __name__ == '__main__':
    app.run(debug=True)