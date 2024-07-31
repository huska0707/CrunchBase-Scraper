import sys
import re
from bs4 import BeautifulSoup

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage

BASE_URL = "https://www.crunchbase.com"

companies = []
page = []


class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ""
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


def get_page(route):
    if not route:
        return None

    try:
        url = f"{BASE_URL}{route}"
        pages.append(Page(url))
        soup = BeautifulSoup(pages[-1].html, "lxml")
        pages[-1].deleteLater()
    except:
        return None
    else:
        return soup


def format_name(name):
    return (
        name.lower()
        .replace("\n", "")
        .strip()
        .replace(".", "-")
        .replace(" ", "-")
        .replace(":", "-")
    )

def extract_link(element):
    return re.search(
        r"(https?:\/\/)(www\.)?([a-zA-Z0-9]+(-?[a-zA-Z0-9])*\.)+([a-z]{2,})(\/\S*)?",
        element,
    ).group(0)


def print_green(s):
    print(f"\033[92m{s}\033[0m")
