class VideoPlayer:
    def __init__(self):
        self.video_file = None
        self.is_playing = False

    def load_video(self, file_path):
        self.video_file = file_path
        print(f"Loaded video: {self.video_file}")

    def play_video(self):
        if self.video_file:
            self.is_playing = True
            print(f"Playing video: {self.video_file}")
        else:
            print("No video file loaded.")

    def pause_video(self):
        if self.is_playing:
            self.is_playing = False
            print("Video paused.")
        else:
            print("Video is not playing.")

    def stop_video(self):
        if self.is_playing:
            self.is_playing = False
            print("Video stopped.")
        else:
            print("Video is not playing.")