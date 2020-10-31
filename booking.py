from urllib.request import urlopen
from openpyxl import Workbook 
from bs4 import BeautifulSoup
import time, re

class Booking:
	def name(self, soup):
		return soup.find('h2', class_='hp__hotel-name').text.strip()

	def no_of_reviews(self, soup):
		x = soup.find('span', class_='review-score-widget__subtext')
		if x: return ((x.text.strip()).split(' '))[0]

	def overall_score(self, soup):
		x = soup.find('span', class_='review-score-badge')
		if x: return x.text.strip()
		else: return None

	def last_review_score(self, soup):
		return None

	def last_review_date(self, soup):
		div = soup.find('div', id='review_list_page_container')
		ul = div.find('ul', class_='review_list')
		return None

	def get_reviews(self, soup):
		reviews = []
		revs = soup.find_all('div', class_='review-container')
		if revs: 
			for x in revs:
				for y in x.find('div', class_='prw_rup prw_reviews_text_summary_hsx'):
					reviews.append(y.text)
			return reviews[:5]
		else:
			return None

if __name__ == '__main__':
	total = 0
	scraped, not_scraped = 0, 0

	start_time = time.time()
	input_file = str(input('Input File (.txt): '))
	output_file = str(input('Output Filename: '))

	if not input_file.endswith('.txt'):
		input_file = ''.join([input_file, '.txt'])
	else:
		input_file = input_file

	if output_file == '':
		output_file = 'booking.xlsx'
	else:
		if not output_file.endswith('.xlsx'):
			output_file = ''.join([output_file, '.xlsx'])

	wb = Workbook()
	ws = wb.active

	f = open(input_file)
	links = f.readlines()
	links = [x.strip() for x in links]
	for x in links:
		if not '#tab-reviews' in x:
			x = x + '#tab-reviews'
	f.close()

	start = time.time()
	for x in links:
		total += 1
		soup = BeautifulSoup(urlopen(x).read(), 'lxml')
		x = soup.find('span', class_='review-score-badge')
		if (x):
			print('Link {}: {}'.format(total, x.text.strip()))
		else:
			print('Link {}: not available'.format(total))


	wb.save(output_file)
	print('Execution time: {}'.format(time.time() - start_time))
	print('Total Links: {}'.format(count))
	print('Links scraped: {}'.format(links_scraped))
	print('File {} saved'.format(output_file))