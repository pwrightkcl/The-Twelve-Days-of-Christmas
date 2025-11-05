"""
Tests for The Twelve Days of Christmas
"""

import unittest
from twelve_days import get_gifts, get_day_ordinal, generate_verse, generate_song


class TestTwelveDays(unittest.TestCase):
    
    def test_get_gifts_returns_12_items(self):
        """Test that get_gifts returns exactly 12 gifts"""
        gifts = get_gifts()
        self.assertEqual(len(gifts), 12)
    
    def test_get_gifts_first_item(self):
        """Test that the first gift is correct"""
        gifts = get_gifts()
        self.assertEqual(gifts[0], "a partridge in a pear tree")
    
    def test_get_gifts_last_item(self):
        """Test that the twelfth gift is correct"""
        gifts = get_gifts()
        self.assertEqual(gifts[11], "twelve drummers drumming")
    
    def test_get_day_ordinal_first(self):
        """Test ordinal for first day"""
        self.assertEqual(get_day_ordinal(1), "first")
    
    def test_get_day_ordinal_twelfth(self):
        """Test ordinal for twelfth day"""
        self.assertEqual(get_day_ordinal(12), "twelfth")
    
    def test_generate_verse_first_day(self):
        """Test verse generation for the first day"""
        verse = generate_verse(1)
        self.assertIn("On the first day of Christmas", verse)
        self.assertIn("A partridge in a pear tree", verse)
        # Should not contain "And" on the first day
        self.assertNotIn("And a partridge", verse)
    
    def test_generate_verse_second_day(self):
        """Test verse generation for the second day"""
        verse = generate_verse(2)
        self.assertIn("On the second day of Christmas", verse)
        self.assertIn("Two turtle doves", verse)
        self.assertIn("And a partridge in a pear tree", verse)
    
    def test_generate_verse_twelfth_day(self):
        """Test verse generation for the twelfth day"""
        verse = generate_verse(12)
        self.assertIn("On the twelfth day of Christmas", verse)
        self.assertIn("Twelve drummers drumming", verse)
        self.assertIn("And a partridge in a pear tree", verse)
        # Should contain all 12 gifts
        self.assertIn("Five gold rings", verse)
    
    def test_generate_verse_preserves_capitalization(self):
        """Test that French is capitalized in the verse"""
        verse = generate_verse(3)
        self.assertIn("Three French hens", verse)
    
    def test_generate_song_has_12_verses(self):
        """Test that the complete song has all 12 verses"""
        song = generate_song()
        # Count occurrences of "day of Christmas"
        self.assertEqual(song.count("day of Christmas"), 12)
    
    def test_generate_song_contains_all_ordinals(self):
        """Test that the song contains all ordinal days"""
        song = generate_song()
        ordinals = [
            "first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
        ]
        for ordinal in ordinals:
            self.assertIn(f"On the {ordinal} day", song)
    
    def test_get_day_ordinal_invalid_day_zero(self):
        """Test that get_day_ordinal raises ValueError for day 0"""
        with self.assertRaises(ValueError):
            get_day_ordinal(0)
    
    def test_get_day_ordinal_invalid_day_negative(self):
        """Test that get_day_ordinal raises ValueError for negative day"""
        with self.assertRaises(ValueError):
            get_day_ordinal(-1)
    
    def test_get_day_ordinal_invalid_day_too_large(self):
        """Test that get_day_ordinal raises ValueError for day > 12"""
        with self.assertRaises(ValueError):
            get_day_ordinal(13)
    
    def test_generate_verse_invalid_day_zero(self):
        """Test that generate_verse raises ValueError for day 0"""
        with self.assertRaises(ValueError):
            generate_verse(0)
    
    def test_generate_verse_invalid_day_too_large(self):
        """Test that generate_verse raises ValueError for day > 12"""
        with self.assertRaises(ValueError):
            generate_verse(13)


if __name__ == "__main__":
    unittest.main()
