from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from time import sleep
from datetime import date, datetime
import models as m

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api.sqlite"
db = SQLAlchemy(app)
RECORDS_PER_PAGE = 3


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    account = db.relationship('Account',
                              backref=db.backref('payments', lazy=True))
    date = db.Column(db.DATETIME, default=datetime.now())
    amount = db.Column(db.Float, nullable=False, default=0.0)
    balance_before = db.Column(db.Float, nullable=False, default=0.0)
    type = db.Column(db.String, nullable=True)
    comment = db.Column(db.String, nullable=True)

    def serialize(self):
        return {
            'date': self.date,
            'amount': self.amount,
            'balance_before': self.balance_before,
            'type': self.type,
            'comment': self.comment
        }


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    creation_date = db.Column(db.Date, nullable=False, default=date.today())
    update_date = db.Column(db.Date, nullable=False, default=date.today())
    balance = db.Column(db.Float, nullable=False, default=0.0)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'creation_date': self.creation_date,
            'update_date': self.update_date,
            'balance': self.balance
        }


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/account/<id>", methods=['GET'])
def accounts(id):
    try:
        a = m.accounts(id)
        return jsonify(a.serialize)
    except:
        return {'result': 'error'}


@app.route("/account/<id>/payments", methods=['GET'])
def payments(id):
    try:
        result = dict()
        page = request.args.get('page', 1, type=int)
        a, page, pages = m.payments(db, id, page, RECORDS_PER_PAGE)
        result['current_page'] = page
        result['per_page'] = RECORDS_PER_PAGE
        result['pages'] = pages
        result['payments'] = a
        return jsonify(result)
    except:
        return {'result': 'error'}


@app.route("/account/<id>/payments", methods=['POST'])
def payments_post(id):
    try:
        data = request.json
        p = Payment(account_id=id, amount=data['amount'], type=data['type'], comment=data['comment'])
        p = m.add_payment(db, p)
        return jsonify(p.serialize())
    except:
        return {'result': 'error'}


if __name__ == '__main__':
    db.init_app(app)
    create_tables()
    m.test_data(db)
    app.run(threaded=True, port=8889)  # threaded variant
