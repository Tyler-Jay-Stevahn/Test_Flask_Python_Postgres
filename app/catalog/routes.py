from app.catalog import main


@main.route('/')
def hello_world():
    return 'hello world'
