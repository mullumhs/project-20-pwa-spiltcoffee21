from flask import render_template, request, redirect, url_for, flash
from models import db ,Song

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        # This route should retrieve all items from the database and display them on the page.
        songs = Song.query.all() 
        return render_template('index.html', songs=songs)



    @app.route('/add', methods=['GET','POST'])
    def add():
        if request.method == 'POST':
            song = Song (
            title = request.form.get("title"),
            artist  = request.form.get("artist"),
            image = request.form.get("image"),
            duration  = request.form.get("duration"),
            album  = request.form.get("album"),
            )
            db.session.add(song)
            db.session.commit()
            return redirect(url_for('get_items'))
        else:
            # Display the add item form (GET request)
            return render_template('add.html')



    @app.route('/update', methods=['POST','GET'])
    def update():
        if request.method == 'POST':
            id = request.args.get('id')
            song = Song.query.get(id)
            song.title = request.form.get("title")
            song.artist  = request.form.get("artist")
            song.image = request.form.get("image")
            song.duration  = request.form.get("duration")
            song.album  = request.form.get("album")
            db.session.commit()
            return redirect(url_for('get_items'))
        else:
            id = request.args.get('id')
            song = Song.query.get(id)
            return render_template('edit.html',song = song)
       



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')