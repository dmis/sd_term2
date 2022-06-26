import random, math
from server import Account, Payment


def test_data(db):
    for i in range(20):
        balance = random.randint(0, 100)
        a = Account(username=f"User_{i}", balance=balance)
        db.session.add(a)
        b_b = balance
        for j in range(random.randint(1, 50)):
            amount = random.randint(-1 * b_b, b_b)
            p = Payment(account=a, amount=amount, balance_before=b_b, type=random.randint(1, 3))
            b_b += amount
            db.session.add(p)
    db.session.commit()


def accounts(id) -> Account:
    return Account.query.get(id)


def payments(db, account_id, page_id, per_page):
    result = []
    for record in db.engine.execute(f'SELECT * FROM payment where account_id= {account_id} order by id'):
        rec_dict = dict()
        rec_dict['id'] = record['id']
        rec_dict['date'] = record['date']
        rec_dict['amount'] = record['amount']
        rec_dict['balance'] = record['balance_before']
        rec_dict['type'] = record['type']
        rec_dict['comment'] = record['comment']
        result.append(rec_dict)
    pages = math.ceil(len(result) / per_page)
    page_id = pages if page_id > pages else page_id

    return result[(page_id - 1) * per_page: page_id * per_page], page_id, pages


def add_payment(db, p):
    # I take last transaction and calculate balance
    query = f"select max(id), balance_before + amount as balance from payment where account_id = {p.account_id}"
    for b in db.engine.execute(query):
        p.balance_before = b['balance']
    db.session.add(p)
    db.session.commit()
    # update the account independently from the main transaction
    b = db.engine.execute(
        f'update account set balance=(select balance_before+ amount from payment where account_id={p.account_id} '
        f'ORDER BY id DESC LIMIT 1), update_date=DATE() where id={p.account_id}')
    return p
