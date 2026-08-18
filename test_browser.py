from browser.search import SearchEngine

browser = SearchEngine()

results = browser.search("Python programming")

if isinstance(results, dict) and "error" in results:
    print("ERROR:")
    print(results["error"])
else:
    for i, result in enumerate(results, start=1):
        print("=" * 60)
        print(f"Result {i}")
        print("=" * 60)
        print("Title :", result["title"])
        print("URL   :", result["url"])
        print("Snippet:", result["snippet"])
        print()