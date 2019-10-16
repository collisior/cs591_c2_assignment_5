class URLSplitting():

	def __init__(self): pass

	def protocol(self, url):
		if "://" in url:
			return url.split(":")[0]
		return ""

	def domain(self, url):
		if self.protocol(url) == "":
			return url.split("/")[0]
		return url.split("/")[2]

	def path(self, url):
		l0 = url.split("/")[3:]
		return ''.join(l0)
