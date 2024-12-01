import pytest
from library_item import LibraryItem

class LibraryItem:
    def __init__(self, track, name, artist, rating=0):
        self.track = track
        self.name = name
        self.artist = artist
        self.rating = rating
        self.play_count = 0

    def info(self):
        return f"{self.track} - {self.name} - {self.artist} {self.stars()}"

    def stars(self):
        return "*" * self.rating

    def play(self):
        self.play_count += 1
        return self.play_count

def test_valid_library_item():
    item = LibraryItem("01", "EARFQUAKE", "Tyler, the Creator", 5)
    assert item.track == "01"
    assert item.name == "EARFQUAKE"
    assert item.artist == "Tyler, the Creator"
    assert item.rating == 5
    assert item.play_count == 0

def test_invalid_track_format():
    with pytest.raises(ValueError):
        LibraryItem("1", "EARFQUAKE", "Tyler, the Creator", 5)  
    with pytest.raises(ValueError):
        LibraryItem("abc", "EARFQUAKE", "Tyler, the Creator", 5)  
    with pytest.raises(ValueError):
        LibraryItem("123", "EARFQUAKE", "Tyler, the Creator", 5)  

def test_invalid_inputs():
    with pytest.raises(ValueError):
        LibraryItem("01", "", "Tyler, the Creator", 5)  
    with pytest.raises(ValueError):
        LibraryItem("01", "EARFQUAKE", "", 5)  
    with pytest.raises(ValueError):
        LibraryItem("01", "EARFQUAKE", "Tyler, the Creator", 6)  
    with pytest.raises(ValueError):
        LibraryItem("01", "EARFQUAKE", "Tyler, the Creator", "5")  

def test_stars_display():
    assert LibraryItem("01", "EARFQUAKE", "Tyler, the Creator", 0).stars() == ""
    assert LibraryItem("01", "EARFQUAKE", "Tyler, the Creator", 3).stars() == "***"
    assert LibraryItem("01", "EARFQUAKE", "Tyler, the Creator", 5).stars() == "*****"

def test_info_display():
    item = LibraryItem("01", "EARFQUAKE", "Tyler, the Creator", 5)
    assert item.info() == "01 - EARFQUAKE - Tyler, the Creator *****"

def test_play_functionality():
    item = LibraryItem("01", "EARFQUAKE", "Tyler, the Creator", 5)
    assert item.play_count == 0  
    assert item.play() == 1    
    assert item.play() == 2      
    assert item.play_count == 2  



