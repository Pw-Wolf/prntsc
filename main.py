import os
import aiohttp
import asyncio

import string
import random

from bs4 import BeautifulSoup as bs

import sys

def img_dir():
	img = os.path.join(os.getcwd(), "images")
	if not os.path.exists(img):
		os.mkdir(img)        
	
def generate_random_string(length=6):
	characters = string.ascii_lowercase + string.digits
	unique_characters = random.sample(characters, k=min(length, len(characters)))
	while len(unique_characters) < length:
		random_char = random.choice(characters)
		if random_char not in unique_characters:
			unique_characters.append(random_char)
	return ''.join(unique_characters)

def generate_prntsc_link():
	random_string = generate_random_string()
	link = "https://prnt.sc/" + random_string
	print(link)
	return link

async def get_html(session, url, headers=None):
	async with session.get(url, headers=headers) as response:
		if response.status == 200:
			return await response.text()
		else:
			print(f"Failed to fetch {url}. Status code: {response.status}")
			return None

async def extract_image_url(session, url, headers=None):
	html = await get_html(session, url, headers=headers)
	if html:
		soup = bs(html, 'html.parser')
		image_element = soup.select_one("#screenshot-image")

		if image_element and "src" in image_element.attrs and image_element.get("id") != "p":
			return image_element["src"]
		
		else:
			print(f"No image found with the CSS selector '#screenshot-image' at {url}")
			return None

async def download_image(session, url, folder):
	filename = os.path.basename(url)
	filepath = os.path.join(folder, filename)
	if url[:5] != "https":
		print(f"Bad url {url}")
		return False

	async with session.get(url) as response:
		current_url = str(response.url)

		if current_url[-11:-4] == "removed":
			print(f"Bad url {url}")
			return False
		
		if response.status == 200:
			with open(filepath, 'wb') as f:

				while True:
					chunk = await response.content.read(1024)
					if not chunk:
						break
					f.write(chunk)

			print(f"Downloaded image: {url} -> {filepath}")
			return True

		return False


async def main(count = 10, folder = "images"):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Accept-Encoding': 'none',
			'Accept-Language': 'en-US,en;q=0.8',
			'Connection': 'keep-alive'}
	
	async with aiohttp.ClientSession() as session:
		count_urls = 0
		while count_urls < count:
			url = generate_prntsc_link()
			image_url = await extract_image_url(session, url, headers=headers)

			if image_url:
				await download_image(session, image_url, folder)
				count_urls += 1

if __name__ == "__main__":
	img_dir()
	if len(sys.argv) > 1:
		asyncio.run(main(int(sys.argv[1])))
		sys.exit()
	asyncio.run(main())