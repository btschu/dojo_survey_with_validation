from flask_app import app
from flask import redirect, render_template,request
from ..models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        return redirect('/results')
    return redirect('/')

@app.route('/results')
def results():
    return render_template('results.html', dojo = Dojo.get_last())

# @app.route('/books/create',methods=['POST'])
# def create_book():
#     Book.save(request.form)
#     return redirect('/books')

# @app.route('/books/<int:id>')
# def show_book(id):
#     data ={
#         "id":id
#     }
#     return render_template("show_book.html", book=Book.get_by_id(data),unfavorited_authors=Author.unfavorited_authors(data))

# @app.route('/join/author',methods=['POST'])
# def join_author():
#     data = {
#         'author_id': request.form['author_id'],
#         'book_id': request.form['book_id']
#     }
#     Author.add_favorite(data)
#     return redirect(f"/books/{request.form['book_id']}")

# @app.route('/users/new')
# def new():
#     return render_template("create.html")


# @app.route('/user/edit/<int:id>')
# def edit(id):
#     data ={
#         "id":id
#     }
#     return render_template("edit.html", user = User.get_one(data))


# @app.route('/user/update',methods=['POST'])
# def update():
#     User.update(request.form)
#     return redirect('/users')

# @app.route('/user/delete/<int:id>')
# def delete(id):
#     data = {
#         'id': id
#     }
#     User.delete(data)
#     return redirect('/users')