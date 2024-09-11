import unittest
from urllib.parse import urlparse

# Define the revised function to be tested
def extract_webpage_name(urls):
    domains = []
    for url in urls:
        try:
            netloc = urlparse(url).netloc
            # Extract the last two segments from the domain, handling cases where there are fewer segments
            domain_parts = netloc.split('.')
            if len(domain_parts) >= 2:
                domain = domain_parts[-2]
            else:
                domain = ''
        except Exception:
            domain = ''
        domains.append(domain)
    return domains

class TestExtractWebpageName(unittest.TestCase):
    def test_extract_webpage_name(self):
        # Define test cases
        urls = [
            'http://www.example.com/page',
            'https://subdomain.example.uk/page',
            'http://example.org',
            'ftp://ftp.example.com/resource',
            'https://www.another-example.com/page'
        ]
        
        # Expected output
        expected_domains = [
            'example',
            'example',
            'example',
            'example',
            'another-example'
        ]
        
        # Call the function
        result = extract_webpage_name(urls)
        
        # Assert that the result matches the expected output
        self.assertEqual(result, expected_domains)

    def test_empty_list(self):
        # Test with an empty list
        urls = []
        expected_domains = []
        result = extract_webpage_name(urls)
        self.assertEqual(result, expected_domains)

    def test_malformed_urls(self):
        # Test with malformed URLs
        urls = [
            'http://',
            'https://.com',
            'ftp://ftp'
        ]
        # The domain extraction should handle these gracefully
        expected_domains = [
            '',
            '',
            ''
        ]
        result = extract_webpage_name(urls)
        self.assertEqual(result, expected_domains)

if __name__ == '__main__':
    unittest.main()
