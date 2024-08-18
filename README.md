🎵 Music Player 🎵

A sleek, modern, and easy-to-use music player built with Python and Tkinter, featuring drag-and-drop functionality, volume control, and a live progress bar. This music player is designed to provide a seamless experience with a minimalist aesthetic.
🌟 Features

Minimalist UI: A clean and modern interface that’s easy on the eyes.
Album Art Display: Showcases the album art of the currently playing song.
Drag & Drop: Easily add music to the playlist by dragging and dropping files (or use the "Add Music" button).
Playback Controls: Play, pause, skip forward, and skip backward through your playlist.
Volume Control: Adjust the volume using the slider.
Progress Bar: Displays the current position in the song along with the total duration.
Time Display: See the current time elapsed and total time of the song.
🚀 Getting Started

Prerequisites
Make sure you have the following installed:
Python 3.12+: Download Python
Pygame: Install it via pip
bash
Copy code
pip install pygame
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/music-player.git
cd music-player
Create a virtual environment (optional but recommended):
bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
python musicPlayer.py
🛠️ How It Works

Tkinter is used for the graphical user interface, providing a simple and effective way to create windows, labels, buttons, and more.
Pygame handles the music playback, allowing the application to load and play various audio file formats.
The progress bar and time labels are updated every second to provide real-time feedback on the music playing status.
📂 Project Structure

bash
Copy code
.
├── .venv/                  # Virtual environment (optional)
├── assets/                 # Directory for images and other assets
│   ├── login.png           # Placeholder image for album art
│   └── screenshot.png      # Screenshot of the app
├── musicPlayer.py          # Main application code
├── README.md               # This file
├── requirements.txt        # List of dependencies
└── LICENSE                 # License file
📸 Screenshots

📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
📬 Contact

Feel free to reach out if you have any questions or suggestions!
Email: your-email@example.com
GitHub: your-username
🌟 Acknowledgements

Special thanks to the Pygame community for providing excellent tools for game and multimedia development.
The Tkinter documentation was incredibly helpful in creating the GUI.
To-Do:
 Add playlist functionality.
 Improve album art detection.
 Add support for more audio formats.
