from agents.base_agent import BaseAgent
from browser.browser_manager import BrowserManager


class BrowserAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Browser Agent",
            description="Handles web browsing, searching, scraping, and downloading.",
            priority=3
        )

        self.browser = BrowserManager()

    def can_handle(self, user_input: str) -> bool:

        text = user_input.lower().strip()

        keywords = [
            "search",
            "google",
            "browser",
            "website",
            "internet",
            "web",
            "scrape",
            "read",
            "download"
        ]

        return any(
            keyword in text
            for keyword in keywords
        )

    def execute(self, user_input: str):

        text = user_input.strip()

        lower_text = text.lower()

        # ==========================================================
        # SEARCH
        # ==========================================================

        if lower_text.startswith("search"):

            query = text[6:].strip()

            if not query:

                return "Please tell me what you want me to search for."

            results = self.browser.search(query)

            if not results:

                return "No search results found."

            output = []

            for index, result in enumerate(
                results,
                start=1
            ):

                output.append(
                    f"\nResult {index}\n"
                    f"Title: {result.get('title', 'No title')}\n"
                    f"URL: {result.get('url', 'No URL')}\n"
                    f"Snippet: {result.get('snippet', 'No description')}"
                )

            return "\n".join(output)

        # ==========================================================
        # SCRAPE / READ WEBSITE
        # ==========================================================

        elif (
            lower_text.startswith("scrape")
            or lower_text.startswith("read")
            or lower_text.startswith("open website")
        ):

            if lower_text.startswith("scrape"):

                url = text[6:].strip()

            elif lower_text.startswith("read"):

                url = text[4:].strip()

            else:

                url = text[13:].strip()

            if not url:

                return "Please provide a website URL."

            result = self.browser.scrape(url)

            if "error" in result:

                return f"Scraping failed: {result['error']}"

            return (
                f"Title: {result['title']}\n\n"
                f"URL: {result['url']}\n\n"
                f"Content:\n"
                f"{result['content'][:3000]}"
            )

        # ==========================================================
        # DOWNLOAD
        # ==========================================================

        elif lower_text.startswith("download"):

            url = text[8:].strip()

            if not url:

                return "Please provide a download URL."

            result = self.browser.download(url)

            if result["success"]:

                return (
                    "Download successful.\n\n"
                    f"Filename: {result['filename']}\n"
                    f"Path: {result['file_path']}"
                )

            return (
                "Download failed.\n\n"
                f"Error: {result['error']}"
            )

        return "Browser Agent couldn't understand the request."