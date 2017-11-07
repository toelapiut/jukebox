from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Playlist,Group
from .forms import PlaylistForm
from flask_login import login_required,current_user

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    playlists = Playlist.get_playlists() 
    title = 'Home'

    return render_template('index.html', title = title, playlists = playlists)

@main.route('/group/<int:id>')
@login_required
def group(id):
    '''
    View group page function for the logged in group
    '''
    group = Group.query.get(id)
    playlists = Playlist.query.filter_by(group_id=id).all()

    if group is None:
        abort(404)
    
    if group.id != current_user.id:
        abort(403)

    title = f'{group.name} page'

    return render_template('group.html', title = title, group = group, playlists=playlists)

@main.route('/group/playlist/new/<int:id>', methods=['GET','POST'])
@login_required
def create_playlist(id):
    '''
    View create playsist function to display a form for creating a playlist
    '''

    group = Group.query.get(id)

    if group is None:
        abort(404)
    
    if group.id != current_user.id:
        abort(403)

    form = PlaylistForm()

    if form.validate_on_submit():
        name = form.name.data

        new_playlist = Playlist(name = name, group=group)
        new_playlist.save_playlist()
        return redirect(url_for('.group', id=group.id))

    title = f'New Playlist'

    return render_template('new_playlist.html', new_playlist_form=form)

@main.route('/group/playlist/<int:id>')
@login_required
def group_playlist(id):
    '''
    View function to display a specific playlist belonging to a specific group
    '''

    playlist = Playlist.query.get(id)

    if playlist is None:
        abort(404)

    if playlist.group.id != current_user.id:
        abort(403)

    title = f'{playlist.name} page'

    return render_template('group_playlist.html', title=title, playlist=playlist)
   

