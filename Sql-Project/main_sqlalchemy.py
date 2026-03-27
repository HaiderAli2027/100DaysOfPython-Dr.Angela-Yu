from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Float, String

app = Flask(__name__)

class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///new_books_collection.db"

db = SQLAlchemy(model_class=Base)

db.init_app(app)

# Create the Model
class Book(db.Model):
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author:Mapped[str] = mapped_column(String(250), nullable=False)
    rating:Mapped[float] = mapped_column(Float, nullable=False)

def __repr__(self):
    return f'<Book {self.title} >'

with app.app_context():
    db.create_all()
# Create the Object of the Model
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J.K.Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

# Read The Records:
with app.app_context():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()

book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_to_update.title = "Harry Potter and Goblet of Fire"
    db.session.commit()