# This is an interface for inheriting classes that
# defines the proccess for which a playlist should
# be generated by the groupify app.

from abc import ABC, abstractmethod

class PlaylistFactory(ABC):

    def __init__(self, users, length):
        self.users = users
        self.playlist_length = length
        self.common_songs = []
        self.union_songs = []
        self.playlist = None
        super().__init__()

    # Run from constructor add users
    def create(self): 
        __union_tracks()
        __squish_tracks()
        __filter_common_tracks(self)
        __filter_intersect_most_played(self)
        __filter_union_most_played(self)
        __filter_union_similarities(self)
        __filter_by_length(self)
        combine(self)
        create_playlist()
        return self.playlist

    # Lvl 1 filter
    def __union_tracks()
        for user in users:
            union_songs = union_songs + user.saved_tracks

    # Squish duplicate tracks into one 
    # TODO: Use hashing and buckets to locate duplicates for efficiency
    def __squish_tracks(self):
        for trackOne in union_songs:
            for trackTwo in union_songs:
                if ( trackOne.songId == trackTwo.songId ) and ( id(trackOne) != id(trackTwo) ):
                    trackOne.add_users(trackTwo.users)
                    union_songs.remove(trackTwo)

    # Lvl 1 filter
    def __filter_common_tracks():
        min_required = len(users)/2 
        for track in union_songs:
            if track.amt_saved >= min_required:
                common_songs.append(track)

    # Lvl 2 filter
    @abstractmethod
    def __filter_intersect_most_played(self): 
        pass

    # Lvl 2 filter
    @abstractmethod
    def __filter_union_most_played(self): 
        pass

    # Lvl 3 filter
    @abstractmethod
    def __filter_union_similarities(self): 
        pass

    # Lvl 4 filter
    @abstractmethod
    def __filter_by_length(self): 
        pass

    # Combine union list and intersect list
    def combine(self):
        # Convert both lists to sets
        union_set = set(union_songs)
        intersect_set = set(intersect_songs)

        # Merge the sets
        union_set.union(intersect_songs)

        # Finally convert to list
        songs = list(union_set)

    def create_playlist():

        # TODO:
        # playlist_name = Groupify-DATE
        # playlist_image = groupify album art by default (?)

        playlist = playlist( songs, playlist_name, playlist_image )
        return playlist
