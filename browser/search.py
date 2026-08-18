from ddgs import DDGS


class SearchEngine:

    def __init__(self):
        self.engine = DDGS()

    def search(self, query: str, max_results: int = 5):

        results = []

        try:

            response = self.engine.text(
                query=query,
                max_results=max_results
            )

            for item in response:

                results.append({
                    "title": item.get("title", ""),
                    "url": item.get("href", ""),
                    "snippet": item.get("body", "")
                })

            return results

        except Exception as e:

            return {
                "error": str(e)
            }