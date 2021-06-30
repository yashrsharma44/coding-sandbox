import random

"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist

random.seed(23)


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._map_id_video = dict()
        self._play_vid_tag = None
        self._paused_vid_tag = None
        self._playlist = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title)
        for video in videos:
            print("{0} ({1}) [{2}]".format(
                video.title, video.video_id, ' '.join(video.tags)))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        new_video = self._video_library.get_video(video_id)
        if new_video is None:
            print("Cannot play video: Video does not exist")
            return

        if self._play_vid_tag is not None:
            print("Stopping video: {0}".format(
                self._video_library.get_video(self._play_vid_tag).title))

        if self._paused_vid_tag is not None:
            print("Stopping video: {0}".format(
                self._video_library.get_video(self._paused_vid_tag).title))

        self._play_vid_tag = video_id
        self._paused_vid_tag = None
        msg = "Playing video: {0}".format(new_video.title)
        print(msg)

    def stop_video(self):
        """Stops the current video."""

        if self._play_vid_tag is None:
            print("Cannot stop video: No video is currently playing")
            return

        self._paused_vid_tag = None
        print("Stopping video: {0}".format(
            self._video_library.get_video(self._play_vid_tag).title))
        self._play_vid_tag = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        if len(self._video_library.get_all_videos()) == 0:
            print("No videos available")
            return

        self._paused_vid_tag = None
        if self._play_vid_tag is not None:
            print("Stopping video: {0}".format(
                self._video_library.get_video(self._play_vid_tag).title))

        curr_playing_video = self._video_library.get_all_videos()
        total_len = len(curr_playing_video)
        new_video = curr_playing_video[int(random.random()) % total_len]

        self._play_vid_tag = new_video.video_id
        print("Playing video: {0}".format(new_video.title))

    def pause_video(self):
        """Pauses the current video."""

        if self._paused_vid_tag is not None:
            print("Video already paused: {0}".format(
                self._video_library.get_video(self._paused_vid_tag).title))
            return

        if self._play_vid_tag is None:
            print("Cannot pause video: No video is currently playing")
            return

        self._paused_vid_tag = self._play_vid_tag
        self._play_vid_tag = None

        print("Pausing video: {0}".format(
            self._video_library.get_video(self._paused_vid_tag).title))

    def continue_video(self):
        """Resumes playing the current video."""

        if self._play_vid_tag is None and self._paused_vid_tag is None:
            print("Cannot continue video: No video is currently playing")
            return

        if self._paused_vid_tag is None:
            print("Cannot continue video: Video is not paused")
            return

        # Paused is not None
        # Play is None
        self._play_vid_tag = self._paused_vid_tag
        self._paused_vid_tag = None
        print("Continuing video: {0}".format(
            self._video_library.get_video(self._play_vid_tag).title))

    def show_playing(self):
        """Displays video currently playing."""

        if self._play_vid_tag is None and self._paused_vid_tag is None:
            print("No video is currently playing")
            return

        if self._play_vid_tag is not None:
            cur_video = self._video_library.get_video(self._play_vid_tag)
            print("Currently playing: {0} ({1}) [{2}]".format(
                cur_video.title, cur_video.video_id, ' '.join(cur_video.tags)))
            return

        paused_video = self._video_library.get_video(self._paused_vid_tag)
        print("Currently playing: {0} ({1}) [{2}] - PAUSED".format(
            paused_video.title, paused_video.video_id, ' '.join(paused_video.tags)))

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        msg = self._playlist.create_playlist(playlist_name)
        print(msg)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        # Check if playlist is valid
        err = self._playlist.add_to_playlist(playlist_name, video_id)
        if err is not None:
            print(err)
            return

        # Check if the video is valid
        if self._video_library.get_video(video_id) is None:
            print("Cannot add video to {0}: Video does not exist".format(
                playlist_name))
            return

        print("Added video to {0}: {1}".format(
            playlist_name,
            self._video_library.get_video(video_id).title))

    def show_all_playlists(self):
        """Display all playlists."""

        all_playlist, name_map = self._playlist.show_all_playlist()
        if len(name_map.keys()) == 0:
            print("No playlists exist yet")
            return

        names = list(name_map.keys())
        names.sort()
        print("Showing all playlists:")
        for name in names:
            print(name_map[name])

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        all_videos = self._playlist.show_playlist(playlist_name)
        if all_videos is None:
            print("Cannot show playlist {0}: Playlist does not exist".format(
                playlist_name))
            return

        print("Showing playlist: {0}".format(playlist_name))
        if len(all_videos) == 0:
            print("No videos here yet")
            return

        for video_id in all_videos:
            video = self._video_library.get_video(video_id)
            print("{0} ({1}) [{2}]".format(
                video.title, video.video_id, ' '.join(video.tags)))

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        video_details = self._video_library.get_video(video_id)
        msg = self._playlist.remove_video_playlist(
            playlist_name, video_id, video_details)
        print(msg)

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        msg = self._playlist.clear_playlist(playlist_name)
        print(msg)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        msg = self._playlist.delete_playlist(playlist_name)
        print(msg)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
