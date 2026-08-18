from browser.browser_manager import BrowserManager


browser = BrowserManager()


print("=" * 60)
print("TEST 1: SEARCH")
print("=" * 60)

search_results = browser.search("Python programming")

print(f"Found {len(search_results)} results")


print()


print("=" * 60)
print("TEST 2: SCRAPE")
print("=" * 60)

scrape_result = browser.scrape(
    "https://www.python.org"
)

if "error" in scrape_result:

    print("Scraping failed:")
    print(scrape_result["error"])

else:

    print("Title:")
    print(scrape_result["title"])

    print("Content preview:")
    print(
        scrape_result["content"][:300]
    )


print()


print("=" * 60)
print("TEST 3: DOWNLOAD")
print("=" * 60)

download_result = browser.download(
    "https://www.python.org/static/img/python-logo.png"
)

if download_result["success"]:

    print("Download successful:")
    print(download_result["file_path"])

else:

    print("Download failed:")
    print(download_result["error"])