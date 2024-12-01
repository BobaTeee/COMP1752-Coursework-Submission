import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class TrackCreator:
    def __init__(self, window):
        self.window = window
        self.window.geometry("750x350")
        self.window.title("Create Track List")
        
        add_track_btn = tk.Button(window, text="Add Track", command=self.add_track_clicked). grid(row=0, column=0, padx=10, pady = 10)

        enter_lbl = tk.Label(window, text="Enter Track Number") 
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(self.window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        playbtn = tk.Button(window, text="Play Playlist", command=self.play_playlist_clicked).grid(row=0, column=3, padx=10, pady=10)
        resetbtn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist_clicked).grid(row=0, column=4, padx=10, pady=10)
       

        self.playlist_txt = tkst.ScrolledText(self.window, width=48, height=12, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        self.create_track_list = []

    
    def Reset_playlist(self):
        self.playlist_txt.delete("1.0", tk.END)
        self.status_lbl.configure(text="Playlist cleared.")

    def add_track_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            self.create_track_list.append({"number": key, "name": name, "artist": artist})
            self.update_playlist_display()
            self.status_lbl.configure(text=f"Track {key} added to playlist.")
        else:
            self.status_lbl.configure(text=f"Track {key} not found.")   
        self.input_txt.delete(0, tk.END)
    
    def reset_playlist_clicked(self):
        self.create_track_list = []
        self.update_playlist_display()
        self.status_lbl.configure(text="Playlist has been reset.")

    def update_playlist_display(self):
        playlist_content = "\n".join([f"{track['name']} - {track['artist']}" for track in self.create_track_list])
        set_text(self.playlist_txt, playlist_content)

    def play_playlist_clicked(self):
        if not self.create_track_list:
            self.status_lbl.configure(text="The playlist is empty. Add tracks before playing.")
        else:
            for track in self.create_track_list:
                lib.increment_play_count(track["number"])
            self.status_lbl.configure(text="Playlist has been played.")


if __name__ == "__main__":
   window = tk.Tk()
   fonts.configure()
   TrackCreator(window)
   window.mainloop()
