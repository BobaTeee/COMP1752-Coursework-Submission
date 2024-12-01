import tkinter as tk
import tkinter.scrolledtext as tkst


import track_library as lib
import font_manager as fonts


def set_text(text_area, content):    # inserts content into the text_area 
    text_area.delete("1.0", tk.END)  # first the existing content is deleted
    text_area.insert(1.0, content)   # then the new content is inserted



class TrackViewer():
    def __init__(self, window): # Creates a window
        window.geometry("750x350") # Set the size of the window
        window.title("View Tracks") # Title for the window

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked) # Creates a button that lists all track
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Track Number") # Creates a text "Enter track Number"
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3) # Creates an input field for track number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked) # Creates a view track button 
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none") # Scrolled text area to display the list of tracks
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")  # Text area to display individual tracks
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # Label to display messages
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
           
        self.list_tracks_clicked()  # Listing tracks when GUI is opened

    
     # Function for when "View tracks" is clicked
    def view_tracks_clicked(self):
        key = self.input_txt.get() # Gets the input track number
        name = lib.get_name(key)  # Retrieve the track with the name "key"
        if name is not None: # If the track exists then:
            artist = lib.get_artist(key)  # Gets the artist name
            rating = lib.get_rating(key) # Gets the track's rating
            play_count = lib.get_play_count(key) # Gets the play count
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}" # Format for when the details is displayed
            set_text(self.track_txt, track_details).curselection() # Display the details
        else: # If the track does not exist
            set_text(self.track_txt, f"Track {key} not found") # Display error
        self.status_lbl.configure(text="View Track button was clicked!")
    
    # Function for when the "list all tracks" is clicked.
    def list_tracks_clicked(self):
        track_list = lib.list_all() # retrieve the list of all tracks
        set_text(self.list_txt, track_list) # display the list in the text area
        self.status_lbl.configure(text="List Tracks button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc



