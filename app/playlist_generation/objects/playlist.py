class Playlist:

    def __init__(self, playlist_id, songs=None, name=None, image=None, time_length=None):
        self.playlist_id = playlist_id
        self.songs = songs
        self.name = name
        self.image = image
        self.time_length = time_length
        if songs is None:
            __retrieve_info(self)

    def __retrieve_info(self):
        # Retrive info from api 
        # Add each song_id to self.songs 
        # set self.name
        # set self.image
        # set self.time_length

    def toJson():
        # TODO: Generate json data for the playlist?
