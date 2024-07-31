## About <a name = "about"></a>

This project was implemented to be able to save crunchbase data without having access to their APIs. All that you need is a `Crunchbase Free Trial`.

It gathers data about companies like their website, their twitter and their founder's twitter. It can be modified to gather other types of data easily.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.



### Installing



```
pip install -r requirements.txt
```


## 🎈 Usage <a name="usage"></a>

The project is composed of 2 scripts `clipboard_fetcher.py` and `crunchbase_scraper.py`

In order to get a `list of comapanies`, saved in `list_of_company_names_raw` run `python clipboard_fetcher.py`. Then login into [Crunchbase](https://crunchbase.com), go to an advanced search and `cmd+a, cmd+c`. The program will automatically detect the copied content and will write the name of the company to the list csv.

In order to scrape data using the company names run `python crunchbase_scraper.py`. It will write the data in 3 files:

* `found.csv` - the companies that were found. Format `Company Name, Company Website, Company Twitter, CEO Twitter, CTO Twitter`
* `not_found.csv` - the companies that were not found based on the company name. Format `Company Name`
* `error.csv` - the companies that returned an error while scraping. Format `Company Name`

## ⛏️ Built Using <a name = "built_using"></a>

- [PyQt5](https://pypi.org/project/PyQt5/) - For loading website javascript
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Scraping library

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
