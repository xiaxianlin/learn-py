from peewee import *
from settting import get_settings
from hashlib import md5

database = SqliteDatabase(get_settings().database)
print(get_settings())


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateField()

    def following(self):
        return (
            User.select()
            .join(Relationship, on=Relationship.to_user)
            .where(Relationship.from_user == self)
            .order_by(User.username)
        )

    def followers(self):
        return (
            User.select()
            .join(Relationship, on=Relationship.from_user)
            .where(Relationship.to_user == self)
            .order_by(User.username)
        )

    def is_following(self, user):
        return (
            Relationship.select()
            .where((Relationship.from_user == self) & (Relationship.to_user == user))
            .exists()
        )

    def gravatar_list(self, size=80):
        return "http://www.gravatar.com/avatar/%s?d=identicon&s=%d" % (
            md5(self.email.strip().lower().encode("utf-8")).hexdigest(),
            size,
        )


class Relationship(BaseModel):
    from_user = ForeignKeyField(User, backref="relationships")
    to_user = ForeignKeyField(User, backref="related_to")

    class Meta:
        indexes = ((("from_user", "to_user"), True),)


class Message(BaseModel):
    user = ForeignKeyField(User, backref="messages")
    content = TextField()
    pub_data = DateTimeField()


def create_tables():
    with database:
        database.create_tables([User, Relationship, Message])

