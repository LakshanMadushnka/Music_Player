import tkinter as tk
from tkinter import filedialog, PhotoImage
from pygame import mixer
import time

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Music Player")
        self.geometry("400x650")
        self.configure(bg="#f2f2f2")

        mixer.init()

        self.create_widgets()

    def create_widgets(self):
        # Frame for album art and song details
        self.album_art_frame = tk.Frame(self, bg="#f2f2f2")
        self.album_art_frame.pack(pady=20)

        # Placeholder for album art
        self.album_art = PhotoImage(file='photo.png')
        self.album_art_label = tk.Label(self.album_art_frame, image=self.album_art, bg="#f2f2f2")
        self.album_art_label.pack()

        # Now Playing Label
        self.now_playing = tk.Label(self, text="Now Playing", font=("Arial", 16), bg="#f2f2f2", fg="#4b2b18")
        self.now_playing.pack(pady=10)

        # Song name Label
        self.song_name = tk.Label(self, text="No song playing", font=("Arial", 12), bg="#f2f2f2", fg="#4b2b18")
        self.song_name.pack(pady=10)

        # Timeline (Progress Bar)
        self.timeline = tk.Scale(self, from_=0, to=100, orient="horizontal", length=250, showvalue=0, bg="#f2f2f2", fg="#4b2b18")
        self.timeline.pack(pady=10)

        # Time Labels
        self.current_time_label = tk.Label(self, text="00:00", font=("Arial", 10), bg="#f2f2f2", fg="#4b2b18")
        self.current_time_label.pack(side="left", padx=(20, 0))
        
        self.total_time_label = tk.Label(self, text="00:00", font=("Arial", 10), bg="#f2f2f2", fg="#4b2b18")
        self.total_time_label.pack(side="right", padx=(0, 20))

        # Control Buttons
        self.controls_frame = tk.Frame(self, bg="#f2f2f2")
        self.controls_frame.pack(pady=20)

        self.prev_button = tk.Button(self.controls_frame, text="<<", command=self.play_prev, bg="#f2f2f2", fg="#4b2b18")
        self.prev_button.grid(row=0, column=0, padx=10)

        self.play_button = tk.Button(self.controls_frame, text="Play", command=self.play_pause, bg="#f2f2f2", fg="#4b2b18")
        self.play_button.grid(row=0, column=1, padx=10)

        self.next_button = tk.Button(self.controls_frame, text=">>", command=self.play_next, bg="#f2f2f2", fg="#4b2b18")
        self.next_button.grid(row=0, column=2, padx=10)

        # Volume Control
        self.volume_slider = tk.Scale(self, from_=0, to=100, orient="horizontal", command=self.set_volume, bg="#f2f2f2", fg="#4b2b18")
        self.volume_slider.set(50)
        self.volume_slider.pack(pady=20)

        # Add Music Button (Replacement for Drag & Drop)
        self.add_music_button = tk.Button(self, text="Add Music", command=self.add_music, bg="#e2e2e2", fg="#4b2b18", relief="sunken")
        self.add_music_button.pack(pady=20)

        self.music_list = []
        self.current_song_index = -1
        self.is_playing = False

    def add_music(self):
        files = filedialog.askopenfilenames(filetypes=(("Audio Files", "*.mp3 *.wav"),))
        self.music_list.extend(files)

    def play_prev(self):
        if self.current_song_index > 0:
            self.current_song_index -= 1
            self.play_music(self.music_list[self.current_song_index])

    def play_next(self):
        if self.current_song_index < len(self.music_list) - 1:
            self.current_song_index += 1
            self.play_music(self.music_list[self.current_song_index])

    def play_pause(self):
        if self.is_playing:
            mixer.music.pause()
            self.play_button.config(text="Play")
            self.is_playing = False
        else:
            if self.current_song_index == -1 and self.music_list:
                self.current_song_index = 0
            if self.music_list:
                self.play_music(self.music_list[self.current_song_index])

    def play_music(self, music_file):
        mixer.music.load(music_file)
        mixer.music.play()
        self.song_name.config(text=music_file.split("/")[-1])
        self.play_button.config(text="Pause")
        self.is_playing = True

        # Set total time label
        total_length = mixer.Sound(music_file).get_length()
        self.total_time_label.config(text=time.strftime('%M:%S', time.gmtime(total_length)))

        # Update the timeline
        self.update_timeline()

    def update_timeline(self):
        if self.is_playing:
            current_time = mixer.music.get_pos() / 1000  # Get current time in seconds
            total_length = mixer.Sound(self.music_list[self.current_song_index]).get_length()
            self.timeline.config(to=int(total_length))
            self.timeline.set(current_time)

            # Update current time label
            self.current_time_label.config(text=time.strftime('%M:%S', time.gmtime(current_time)))

            # Update every second
            self.after(1000, self.update_timeline)

    def set_volume(self, value):
        volume = int(value) / 100
        mixer.music.set_volume(volume)

if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()
