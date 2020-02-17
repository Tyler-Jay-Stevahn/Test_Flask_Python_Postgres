from app.catalog import main
from app import db
from app.catalog.models import Book, Publication


@main.route('/')
def display_books():
    return 'Your oof is showing'
