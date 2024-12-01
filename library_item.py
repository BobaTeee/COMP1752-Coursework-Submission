class LibraryItem:
    def __init__(self, name, artist, rating=0):
        if not name or not isinstance(name, str):
            raise ValueError("Name cannot be empty and must be a string")
        if not artist or not isinstance(artist, str):
            raise ValueError("Artist cannot be empty and must be a string")
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer")
        if not 0 <= rating <= 5:
            raise ValueError("Rating must be between 0 and 5")
        self.name = name
        self.artist = artist
        self.rating = rating
        self.play_count = 0

    def info(self):
        return f"{self.name} - {self.artist} {self.stars()}"

    def stars(self):
        return "*" * self.rating

    def play(self):
        self.play_count += 1
        return self.play_count