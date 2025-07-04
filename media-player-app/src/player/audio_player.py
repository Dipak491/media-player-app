class AudioPlayer:
    def __init__(self):
        self.current_audio = None

    def load_audio(self, file_path):
        # Logic to load audio file
        self.current_audio = file_path
        print(f"Loaded audio: {file_path}")

    def play_audio(self):
        if self.current_audio:
            # Logic to play audio
            print(f"Playing audio: {self.current_audio}")
        else:
            print("No audio loaded.")

    def pause_audio(self):
        # Logic to pause audio
        print("Audio paused.")

    def stop_audio(self):
        # Logic to stop audio
        print("Audio stopped.")