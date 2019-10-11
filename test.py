from unittest import TestCase, main as unittest_main
from app import app

class PlaylistsTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True


    def test_index(self):
        """Test the playlists homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Playlist', result.data)

    def test_new(self):
        """Test the new playlist creation page."""
        result = self.client.get('/playlists/new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'New Playlist', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_playlist(self, mock_find):
        """Test showing a single playlist."""
        mock_find.return_value = sample_playlist

        result = self.client.get(f'/playlists/{sample_playlist_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Cat Videos', result.data)

   @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_playlist(self, mock_find):
        """Test editing a single playlist."""
        mock_find.return_value = sample_playlist

        result = self.client.get(f'/playlists/{sample_playlist_id}/edit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Cat Videos', result.data)

if __name__ == '__main__':
    unittest_main()