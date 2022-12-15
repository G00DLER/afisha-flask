from app import app, db, admin
from flask import render_template
from app.models import Ticket
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(Ticket, db.session, name='Билеты'))


@app.route('/')
def index():
    tickets = Ticket.query.all()
    return render_template('index.html', title='Главная', tickets=tickets)


@app.route('/success')
def success():
    return render_template('success.html', title='Успешная покупка')
