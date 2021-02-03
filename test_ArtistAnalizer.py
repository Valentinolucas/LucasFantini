import unittest
from ArtistAnalizer import ArtistAnalizer
import musicbrainzngs


class TestArtistAnalizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.artist = ArtistAnalizer("The Mars Volta")
        self.artist2 = ArtistAnalizer("The Beatles")
        self.artist3 = ArtistAnalizer("Radiohead")
        self.artist4 = ArtistAnalizer("")

    def tearDown(self):
        pass

    def test_artistId(self):
        self.assertEqual(self.artist.artistId(), "20883363-1ea4-4d72-ad72-c0e767038f3e")
        self.assertEqual(
            self.artist2.artistId(), "b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d"
        )
        self.assertEqual(
            self.artist3.artistId(), "a74b1b7f-71a5-4011-9441-d0b5e4122711"
        )
        self.assertEqual(self.artist4.artistId(), False)

    def test_artistRecords(self):
        self.assertEqual(
            self.artist.artistRecords("20883363-1ea4-4d72-ad72-c0e767038f3e"),
            [
                "De‐Loused in the Comatorium",
                "Frances the Mute",
                "Amputechture",
                "The Bedlam in Goliath",
                "Octahedron",
                "Noctourniquet",
                "A Missing Chromosome",
                "[demos]",
            ],
        )

    def test_analizeLyrics(self):
        self.assertEqual(self.artist3.analizeLyrics("radiohead", ["creep"]), 163)


if __name__ == "__main__":
    unittest.main()
