from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def russian_kitchen():
    context = {
        "link": 'Рецепт'
    }
    return render_template('index.html', **context)


@app.route('/blog/')
def blog():
    context = {
        "link": 'Рецепт'
    }
    return render_template('blog.html', **context)

@app.route('/contacts/')
def contacts():
    context = {
        "link": 'Рецепт'
    }
    return render_template('contacts.html', **context)

if __name__ == '__main__':
    app.run()