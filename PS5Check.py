def ps5test():
	from GenerateEmail import send_email
	import requests
	from requests_html import HTMLSession
	import nest_asyncio

	nest_asyncio.apply()
	from bs4 import BeautifulSoup
	session = HTMLSession()

	try:
		results = session.get("Insert URL HERE - Do Not Use Without Website Permission")
		html_str = results.text

		if "out of stock" not in html_str.lower():
			message = "Subject (Typically Store Name)"
			send_email(message)
			session.close()
			return True
	except:
		send_email("ERROR OCCURRED AT <<STORE>> ... SYSTEM EXIT!")

	session.close()
	return False