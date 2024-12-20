import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class ViewTracksFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.Main_Win()
    

    def Main_Win(self):
        list_tracks_btn = tk.Button(self, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(self, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(self, width=3, highlightthickness=0)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(self, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)


        self.list_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none", highlightthickness=0)
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(self, width=24, height=4, wrap="none", highlightthickness=0)
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(self, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        filter_lbl = tk.Label(self, text="Filter by Artist:")
        filter_lbl.grid(row=0, column=4, padx=10, pady=10)

        self.filter_txt = tk.Entry(self, width=20, highlightthickness=0)
        self.filter_txt.grid(row=0, column=5, padx=10, pady=10)

        filter_btn = tk.Button(self, text="Filter", command=self.filter_tracks_clicked)
        filter_btn.grid(row=0, column=6, padx=10, pady=10)

        self.list_tracks_clicked()
    
    def filter_tracks_clicked(self):
        artist_name = self.filter_txt.get().strip().lower()
        if not artist_name:
            self.list_tracks_clicked()
            return

        filtered_tracks = []
        all_tracks = lib.list_all().split('\n')
        for track_line in all_tracks:
            if track_line: 
                track_num = track_line.split()[0]  
                track_artist = lib.get_artist(track_num)
                if track_artist and artist_name in track_artist.lower():
                    name = lib.get_name(track_num)
                    rating = lib.get_rating(track_num)
                    play_count = lib.get_play_count(track_num)
                    filtered_tracks.append(f"{track_num}: {name} by {track_artist} "
                                        f"(rating: {rating}, plays: {play_count})")

        if filtered_tracks:
            filtered_content = "\n".join(filtered_tracks)
            set_text(self.list_txt, filtered_content)
            self.status_lbl.configure(text=f"Showing tracks filtered by artist: {artist_name}")
        else:
            set_text(self.list_txt, "No tracks found for this artist")
            self.status_lbl.configure(text=f"No tracks found for artist: {artist_name}")


    
    def view_tracks_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
        else:
            set_text(self.track_txt, f"Track {key} not found")
        self.status_lbl.configure(text="View Track button was clicked!")
    

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

class CreateTrackListFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.Main_Win()
        self.create_track_list = []

    def Main_Win(self):
        add_track_btn = tk.Button(self, text="Add Track", command=self.add_track_clicked)
        add_track_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(self, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(self, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        playbtn = tk.Button(self, text="Play Playlist", command=self.play_playlist_clicked)
        playbtn.grid(row=0, column=3, padx=10, pady=10)

        resetbtn = tk.Button(self, text="Reset Playlist", command=self.reset_playlist_clicked)
        resetbtn.grid(row=0, column=4, padx=10, pady=10)

        self.playlist_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none", highlightthickness=0)
        self.playlist_txt.grid(row=1, column=0, columnspan=6, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(self, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=6, sticky="W", padx=10, pady=10)

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

    def play_playlist_clicked(self):    
        if not self.create_track_list:
           self.status_lbl.configure(text="The playlist is empty. Add tracks before playing.")
        else:
           for track in self.create_track_list:
              lib.increment_play_count(track['number'])
           self.status_lbl.configure(text="Playlist has been played.")


    def reset_playlist_clicked(self):
        self.create_track_list = []
        self.update_playlist_display()
        self.status_lbl.configure(text="Playlist has been reset.")

    def update_playlist_display(self):
        playlist_content = "\n".join([f"{track['name']} - {track['artist']}" for track in self.create_track_list])
        set_text(self.playlist_txt, playlist_content)

class UpdateTrackFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.Main_Win()

    def Main_Win(self):
        update_track_btn = tk.Button(self, text="Update Tracks", command=self.update_tracks_clicked)
        update_track_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(self, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.track_number_entry = tk.Entry(self, width=3, highlightthickness=0)
        self.track_number_entry.grid(row=0, column=2, padx=10, pady=10)

        rating_lbl = tk.Label(self, text="Enter New Rating")
        rating_lbl.grid(row=0, column=3, padx=10, pady=10)

        self.track_rating_entry = tk.Entry(self, width=3, highlightthickness=0)
        self.track_rating_entry.grid(row=0, column=4, padx=10, pady=10)
        
        self.playlist_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none", highlightthickness=0)
        self.playlist_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)
      
        self.status_lbl = tk.Label(self, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=5, sticky="W", padx=10, pady=10)

    def update_tracks_clicked(self):
        track_number = self.track_number_entry.get()
        new_rating = self.track_rating_entry.get()
        
        try:
            new_rating = int(new_rating)
            if new_rating < 1 or new_rating > 5:
                raise ValueError("Rating must be between 1 and 5")
        except ValueError:
            self.status_lbl.config(text="Invalid rating. Please enter a number between 1 and 5.")
            return
        
        name = lib.get_name(track_number)
        if name is None:
            self.status_lbl.config(text="Invalid track number. Please try again.")
            return
        
        lib.set_rating(track_number, new_rating)
        play_count = lib.get_play_count(track_number)
        message = f"Track: {name}\nNew Rating: {new_rating}\nPlay Count: {play_count}"
        set_text(self.playlist_txt, message)
        self.status_lbl.config(text="Track updated successfully.")
        
        self.track_number_entry.delete(0, tk.END)
        self.track_rating_entry.delete(0, tk.END)

class JukeBoxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("JukeBox")
        self.geometry("750x400")
        fonts.configure()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.view_tracks_frame = ViewTracksFrame(self.notebook)
        self.create_track_list_frame = CreateTrackListFrame(self.notebook)
        self.update_track_frame = UpdateTrackFrame(self.notebook)

        self.notebook.add(self.view_tracks_frame, text="View Tracks")
        self.notebook.add(self.create_track_list_frame, text="Create Track List")
        self.notebook.add(self.update_track_frame, text="Update Tracks")
        
    
if __name__ == "__main__":
    app = JukeBoxApp()
    app.mainloop()

