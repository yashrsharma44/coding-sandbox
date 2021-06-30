"""A video playlist class."""


from typing import Iterable, Mapping, Sequence


class PlaylistException(Exception):
    """A class to represent a duplicate playlist exception"""
    pass


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self) -> None:
        self.all_playlist = {}
        self.name_map = {}

    def create_playlist(self, playlist_name) -> str:
        """Add a new playlist."""
        if playlist_name.lower() in self.all_playlist.keys():
            return "Cannot create playlist: A playlist with the same name already exists"

        self.all_playlist[playlist_name.lower()] = list()
        self.name_map[playlist_name.lower()] = playlist_name
        return "Successfully created new playlist: {0}".format(playlist_name)

    def add_to_playlist(self, playlist_name, video_id) -> str:
        """Adds a video id to a given playlist."""
        if playlist_name.lower() not in self.all_playlist.keys():
            return "Cannot add video to {0}: Playlist does not exist".format(playlist_name)

        if video_id in self.all_playlist[playlist_name.lower()]:
            return "Cannot add video to {0}: Video already added".format(playlist_name)

        self.all_playlist[playlist_name.lower()].append(video_id)
        return None

    def show_all_playlist(self):
        """Returns all the playlist and videos added."""
        return self.all_playlist, self.name_map

    def show_playlist(self, playlist_name) -> Sequence:
        """Returns all the videos for a given playlist."""
        if playlist_name.lower() not in self.all_playlist.keys():
            return None

        return self.all_playlist[playlist_name.lower()]

    def remove_video_playlist(self, playlist_name, video_id, video_details):
        """Remove a video from the playlist."""
        if playlist_name.lower() not in self.all_playlist.keys():
            return "Cannot remove video from {0}: Playlist does not exist".format(playlist_name)

        if not video_details:
            return "Cannot remove video from {0}: Video does not exist".format(playlist_name)

        if video_id not in self.all_playlist[playlist_name.lower()]:
            return "Cannot remove video from {0}: Video is not in playlist".format(playlist_name)

        # Playlist is present
        # Video is present

        self.all_playlist[playlist_name.lower()].remove(video_id)
        return "Removed video from {0}: {1}".format(playlist_name, video_details.title)

    def clear_playlist(self, playlist_name):
        """Remove all videos from playlist."""
        if playlist_name.lower() not in self.all_playlist.keys():
            return "Cannot clear playlist {0}: Playlist does not exist".format(playlist_name)

        self.all_playlist[playlist_name.lower()] = list()
        return "Successfully removed all videos from {0}".format(playlist_name)

    def delete_playlist(self, playlist_name):
        """Delete the playlist, if present"""
        if playlist_name.lower() not in self.all_playlist.keys():
            return "Cannot delete playlist {0}: Playlist does not exist".format(playlist_name)

        self.all_playlist.pop(playlist_name.lower())
        return "Deleted playlist: {0}".format(playlist_name)
