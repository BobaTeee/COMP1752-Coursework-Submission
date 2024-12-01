import tkinter as tk
import track_library as lib
import font_manager as fonts
import tkinter.scrolledtext as tkst

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateTrack:
    def __init__(self, window):
        self.window = window
        window.geometry("750x350")
        window.title("Update Track List")

        update_track_btn = tk.Button(window, text="Update Tracks", command=self.update_tracks_clicked)
        update_track_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.track_number_entry = tk.Entry(window, width=3)
        self.track_number_entry.grid(row=0, column=2, padx=10, pady=10)

        rating_lbl = tk.Label(window, text="Enter New Rating")
        rating_lbl.grid(row=0, column=3, padx=10, pady=10)

        self.track_rating_entry = tk.Entry(window, width=3)
        self.track_rating_entry.grid(row=0, column=4, padx=10, pady=10)
        
        self.playlist_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)
      
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
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

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateTrack(window)
    window.mainloop()

