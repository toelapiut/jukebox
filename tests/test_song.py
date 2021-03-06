import unittest
# Import class to be tested
from app.models import Song, Playlist

class SongTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Song class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_song = Song(name='Happy Song Happy Song')

    def test_instance(self):
        '''
        Test case to check if new_song is an instance of Song
        '''
        self.assertTrue( isinstance( self.new_song, Song))

    def test_save_song(self):
        '''
        Test case to check if a song is saved to the databse
        '''

        self.new_song.save_song()

        self.assertTrue( len(Song.query.all()) > 0 )

    def test_get_songs(self):
        '''
        Test case to check if all songs are returned by the get_songs function
        '''

        self.new_song.save_song()

        test_song = Song(name="Wierd Song Awkward Song")

        test_song.save_song()

        gotten_songs = Song.get_songs(3456789098765431234567890098765432123456787654323456787654323456787654323456787654334)

        self.assertTrue( len(gotten_songs) != len(Song.query.all()) )

    def test_delete_song(self):
        '''
        Test case to check if test_song is deleted from the database
        '''

        self.new_song.save_song()

        test_song = Song(name="Stand Up Jump Up")

        test_song.save_song()

        test_song.delete_song(test_song.id)

        gotten_songs = Song.get_songs(4990826417581240726341234)

        self.assertFalse( len(gotten_songs) == len(Song.query.all()) )

    def test_search_songs(self):
        '''
        Test case to check if all songs matching the provided song name are returned by the search_songs function
        '''

        self.new_song.save_song()

        test_song = Song(name="Wierd Song Awkward Song")

        test_song.save_song()

        gotten_songs = Song.search_songs("Wierd")

        self.assertFalse( len(gotten_songs) == len(Song.query.all()) )



