def get_supported_formats():
    return ['.mp3', '.wav', '.mp4', '.mkv', '.avi', '.flac']

def open_file_dialog():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()  # Prevents the root window from appearing
    filename = askopenfilename(filetypes=[("Media Files", get_supported_formats())])
    return filename if filename else None