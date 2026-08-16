class AudioFileMain:

    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks

    def play_audio(self):
        for track in self.audio_tracks:
            print(f"Воспроизведение аудио для {self.__class__.__name__}:\n{track}")


class VideoFileMain:

    def __init__(self, video_files):
        self.video_files = video_files

    def play_video(self):
        for video in self.video_files:
            print(f"Воспроизведение видео для {self.__class__.__name__}:\n{video}")


class MediaPlayer(AudioFileMain):

    def __init__(self, audio_tracks):
        super().__init__(audio_tracks)


class Laptop(AudioFileMain, VideoFileMain):

    def __init__(self, audio_tracks, video_files):
        AudioFileMain.__init__(self, audio_tracks)
        VideoFileMain.__init__(self, video_files)


if __name__ == "__main__":
    tracks = ["track1.mp3", "track2.mp3"]
    movies = ["movie.mp4", "trailer.mov"]

    print("Воспроизведение аудио для MediaPlayer:")
    media_player = MediaPlayer(tracks)
    media_player.play_audio()

    print("\nВоспроизведение аудио для Laptop:")
    laptop = Laptop(tracks, movies)
    laptop.play_audio()

    print("\nВоспроизведение видео для Laptop:")
    laptop.play_video()
