from browser.scraper import WebScraper


scraper = WebScraper()

result = scraper.scrape("https://www.python.org")


if "error" in result:

    print("ERROR:")
    print(result["error"])

else:

    print("=" * 60)
    print("TITLE:")
    print(result["title"])

    print()

    print("URL:")
    print(result["url"])

    print()

    print("CONTENT PREVIEW:")
    print(result["content"][:1000])