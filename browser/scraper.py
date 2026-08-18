import requests
from bs4 import BeautifulSoup


class WebScraper:

    def __init__(self):

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        }

    def scrape(self, url: str):

        try:

            response = requests.get(
                url,
                headers=self.headers,
                timeout=15
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            # Remove elements that don't contain useful readable content
            for element in soup(
                ["script", "style", "noscript", "header", "footer", "nav"]
            ):
                element.decompose()

            title = soup.title.string.strip() if soup.title else ""

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            return {
                "url": url,
                "title": title,
                "content": text
            }

        except requests.exceptions.RequestException as e:

            return {
                "error": str(e)
            }

        except Exception as e:

            return {
                "error": str(e)
            }