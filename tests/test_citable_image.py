import unittest
from citable_image import CitableImage
from urn_citation import Cite2Urn


class TestCitableImage(unittest.TestCase):
    """Test suite for CitableImage class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_urn = Cite2Urn.from_string("urn:cite2:example:images.v1:img001")
        self.test_caption = "A beautiful landscape photograph"
        self.test_rights = "CC BY-SA 4.0"
        
    def test_initialization(self):
        """Test CitableImage initialization with all parameters."""
        img = CitableImage(
            urn=self.test_urn,
            caption=self.test_caption,
            rights=self.test_rights
        )
        
        self.assertEqual(img.urn, self.test_urn)
        self.assertEqual(img.caption, self.test_caption)
        self.assertEqual(img.rights, self.test_rights)
    
    def test_delimited_default_delimiter(self):
        """Test delimited string with default pipe delimiter."""
        img = CitableImage(
            urn=self.test_urn,
            caption=self.test_caption,
            rights=self.test_rights
        )
        
        result = img.delimited()
        expected = f"{str(self.test_urn)}|{self.test_caption}|{self.test_rights}"
        
        self.assertEqual(result, expected)
    
    def test_delimited_custom_delimiter(self):
        """Test delimited string with custom delimiter."""
        img = CitableImage(
            urn=self.test_urn,
            caption=self.test_caption,
            rights=self.test_rights
        )
        
        result = img.delimited(delimiter="#")
        expected = f"{str(self.test_urn)}#{self.test_caption}#{self.test_rights}"
        
        self.assertEqual(result, expected)
    
    def test_from_delimited_default_delimiter(self):
        """Test creating CitableImage from delimited string with default delimiter."""
        delimited_str = f"{str(self.test_urn)}|{self.test_caption}|{self.test_rights}"
        
        img = CitableImage.from_delimited(delimited_str)
        
        self.assertEqual(str(img.urn), str(self.test_urn))
        self.assertEqual(img.caption, self.test_caption)
        self.assertEqual(img.rights, self.test_rights)
    
    def test_from_delimited_custom_delimiter(self):
        """Test creating CitableImage from delimited string with custom delimiter."""
        delimited_str = f"{str(self.test_urn)}#{self.test_caption}#{self.test_rights}"
        
        img = CitableImage.from_delimited(delimited_str, delimiter="#")
        
        self.assertEqual(str(img.urn), str(self.test_urn))
        self.assertEqual(img.caption, self.test_caption)
        self.assertEqual(img.rights, self.test_rights)
    
    def test_from_delimited_invalid_parts(self):
        """Test from_delimited raises ValueError with wrong number of parts."""
        invalid_str = f"{str(self.test_urn)}|{self.test_caption}"
        
        with self.assertRaises(ValueError) as context:
            CitableImage.from_delimited(invalid_str)
        
        self.assertIn("Expected 3 parts", str(context.exception))
    
    def test_from_delimited_too_many_parts(self):
        """Test from_delimited raises ValueError with too many parts."""
        invalid_str = f"{str(self.test_urn)}|{self.test_caption}|{self.test_rights}|extra"
        
        with self.assertRaises(ValueError) as context:
            CitableImage.from_delimited(invalid_str)
        
        self.assertIn("Expected 3 parts", str(context.exception))
    
    def test_roundtrip_delimited(self):
        """Test that delimited and from_delimited are inverse operations."""
        img1 = CitableImage(
            urn=self.test_urn,
            caption=self.test_caption,
            rights=self.test_rights
        )
        
        delimited_str = img1.delimited()
        img2 = CitableImage.from_delimited(delimited_str)
        
        self.assertEqual(str(img1.urn), str(img2.urn))
        self.assertEqual(img1.caption, img2.caption)
        self.assertEqual(img1.rights, img2.rights)
    
    def test_caption_with_special_characters(self):
        """Test handling captions with special characters."""
        special_caption = "Image with 'quotes' and \"double quotes\""
        img = CitableImage(
            urn=self.test_urn,
            caption=special_caption,
            rights=self.test_rights
        )
        
        self.assertEqual(img.caption, special_caption)
    
    def test_pydantic_validation(self):
        """Test that Pydantic validation works correctly."""
        # Should work with valid data
        img = CitableImage(
            urn=self.test_urn,
            caption=self.test_caption,
            rights=self.test_rights
        )
        self.assertIsInstance(img, CitableImage)


if __name__ == '__main__':
    unittest.main()
