from peewee import SqliteDatabase, AutoField, CharField, TextField, FloatField, IntegerField, DateField, Model
from datetime import date


def create():
    """connection and creating tables
    """
    db.connect()
    db.create_tables([Product])


def product_add(name, info="", price=0, stock=0, create=date.today(), update=date.today()):
    """add product to datebase whit some defauts variables

    Args:
        name (str): product name
        info (str): product description
        price (float): product price
        stock (int, optional)): product stock actualy. Defaults to 0.
        create (date, optional): create date. Defaults to date.today().
        update (date, optional): create date. Defaults to date.today().
    """
    product_new = Product(name=name,
                          info=info,
                          price=price,
                          stock=stock,
                          create_time=create,
                          update_time=update)
    product_new.save()


def product_list():
    """return products dicts

    Returns:
        dict: the product
    """
    return Product.select().dicts()


def product_update(id, name=None, info=None, price=None, stock=None):

    if name != None:
        Product.update(name=name).where(Product.product_id == id).execute()
    if info != None:
        Product.update(info=info).where(Product.product_id == id).execute()
    if price != None:
        Product.update(price=price).where(Product.product_id == id).execute()
    if stock != None:
        Product.update(stock=stock).where(Product.product_id == id).execute()

    Product.update(update_time=date.today()).where(
        Product.product_id == id).execute()


def product_delete(id):
    Product.delete().where(Product.product_id == id).execute()


def product_search(search):
    return Product.select().where(Product.name.contains(search))


def product_info(id):
    return Product.select().where(Product.product_id == id).dicts()


db = SqliteDatabase("database.db")


class Product(Model):

    product_id = AutoField()
    name = CharField(max_length=150)
    info = TextField()
    price = FloatField()
    stock = IntegerField()
    create_time = DateField()
    update_time = DateField()

    class Meta:
        database = db


if __name__ == "__main__":
    create()
