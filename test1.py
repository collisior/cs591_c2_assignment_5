import unittest
from urlSplitting import *

class TestURLSplitting(unittest.TestCase):

	def test_full_url(self):
		urlSplit = URLSplitting()
		url = "https://wwww.google.com/some-path"
		self.assertEqual(urlSplit.protocol(url), "https", "process_url should return \"https\" given")
		self.assertEqual(urlSplit.domain(url), "wwww.google.com")
		self.assertEqual(urlSplit.path(url), "some-path")
		url = "ftp://bu.edu/"
		self.assertEqual(urlSplit.protocol(url), "ftp")
		self.assertEqual(urlSplit.domain(url), "bu.edu")
		self.assertEqual(urlSplit.path(url), "")
		url = "yahoo.co.uk/"
		self.assertEqual(urlSplit.protocol(url), "")
		self.assertEqual(urlSplit.domain(url), "yahoo.co.uk")
		self.assertEqual(urlSplit.path(url), "")

	def test_protocol(self):
		urlSplit = URLSplitting()
		url = "https://wwww.google.com/some-path"
		self.assertEqual(urlSplit.protocol(url), "https")
		self.assertNotEqual(urlSplit.protocol(url), "wwww.google.com")
		self.assertNotEqual(urlSplit.protocol(url), "some-path")
		url = "ftp://bu.edu/"
		self.assertEqual(urlSplit.protocol(url), "ftp")
		self.assertNotEqual(urlSplit.protocol(url), "bu.edu")
		self.assertNotEqual(urlSplit.protocol(url), "")

	def test_domain(self):
		urlSplit = URLSplitting()
		url = "https://wwww.google.com/some-path"
		self.assertNotEqual(urlSplit.domain(url), "https")
		self.assertEqual(urlSplit.domain(url), "wwww.google.com")
		self.assertNotEqual(urlSplit.domain(url), "some-path")
		url = "ftp://bu.edu/"
		self.assertNotEqual(urlSplit.domain(url), "ftp")
		self.assertEqual(urlSplit.domain(url), "bu.edu")
		self.assertNotEqual(urlSplit.domain(url), "")


	def test_path(self):
		urlSplit = URLSplitting()
		url = "https://wwww.google.com/some-path"
		self.assertNotEqual(urlSplit.path(url), "https")
		self.assertNotEqual(urlSplit.path(url), "wwww.google.com")
		self.assertEqual(urlSplit.path(url), "some-path")
		url = "ftp://bu.edu/"
		self.assertNotEqual(urlSplit.path(url), "ftp")
		self.assertNotEqual(urlSplit.path(url), "bu.edu")
		self.assertEqual(urlSplit.path(url), "")


if __name__ == "__main__":
	unittest.main()
