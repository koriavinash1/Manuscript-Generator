import arxivscraper
from tqdm import tqdm
import pandas as pd

parent_category = [{'type': 'cs', 
		'sub-type': ['cs.ai', 'cs.cl', 'cs.gt', 'cs.cv', 'cs.hc', 'cs.it', 'cs.si' ]}, 
	    	   {'type': 'q-bio',
		'sub-type': ['q-bio.gn', 'q-bio.nc', 'q-bio.ot', 'q-bio.qm']},
	 	   {'type': 'stat',
		'sub-type': ['stat.ap', 'stat.co', 'stat.ml', 'stat.me', 'stat.ot', 'stat.th']},
		   {'type': 'physics',
		'sub-type': ['gr-qc']}
	]
download_dates = ['201'+str(j)+'-'+str(i+1).zfill(2)+'-01' for j in [5, 6, 7, 8, 9] for i in range(12)]

titles = []
ids = []
authors = []
categories = []
abstracts = []
dates = []
urls = []
print (parent_category, download_dates)
for i in tqdm(range(len(download_dates) -1)):
	st_date = download_dates[i]
	end_date = download_dates[i+1]
	for cat in parent_category:
		try:
			scraper = arxivscraper.Scraper(category=cat['type'], 
						date_from=st_date, 
						date_until = end_date)
			outputs = scraper.scrape()
		
			ref_set = set(cat['sub-type'])
			for out in tqdm(outputs):
				_set = set(out['categories'].split(" "))
				if len(ref_set - _set) != len(ref_set):
					titles.append(out['title'])
					ids.append(out['id'])
					authors.append(out['authors'])
					categories.append(out['categories'])
					abstracts.append(out['abstract'])
					dates.append(out['created'])
					urls.append(out['url'])
		except: continue




df = pd.DataFrame()
df['id'] = ids
df['date'] = dates
df['authors'] = authors
df['url'] = urls
df['title'] = titles
df['categories'] = categories
df['abstract'] = abstracts

df.to_csv('./Arxiv_Text_Data_CS_QBIO_STAT_LARGE.csv')





