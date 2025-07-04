# Media Player Application

This project is a simple media player application that allows users to play video and audio files. It is designed to provide a user-friendly interface and supports various media formats.

## Project Structure

```
media-player-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── player
│   │   ├── __init__.py       # Player module initialization
│   │   ├── video_player.py    # Video playback functionalities
│   │   └── audio_player.py    # Audio playback functionalities
│   ├── ui
│   │   ├── __init__.py       # UI module initialization
│   │   └── main_window.py     # Main application window setup
│   └── utils
│       └── file_utils.py      # Utility functions for file handling
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd media-player-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the media player application, execute the following command:

```
python src/main.py
```

## Features

- Play and pause audio and video files
- Load media files from your system
- User-friendly interface for easy navigation

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.