import os
import requests
from urllib.parse import urlparse


class Downloader:

    def __init__(self, download_folder="downloads"):

        self.download_folder = download_folder

        os.makedirs(
            self.download_folder,
            exist_ok=True
        )

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        }

    def download(self, url: str, filename=None):

        try:

            response = requests.get(
                url,
                headers=self.headers,
                stream=True,
                timeout=30
            )

            response.raise_for_status()

            # If filename is not provided, extract it from URL
            if not filename:

                parsed_url = urlparse(url)

                filename = os.path.basename(
                    parsed_url.path
                )

                if not filename:

                    filename = "downloaded_file"

            file_path = os.path.join(
                self.download_folder,
                filename
            )

            # Avoid overwriting an existing file
            file_path = self._get_unique_filename(
                file_path
            )

            with open(file_path, "wb") as file:

                for chunk in response.iter_content(
                    chunk_size=8192
                ):

                    if chunk:

                        file.write(chunk)

            return {
                "success": True,
                "url": url,
                "file_path": file_path,
                "filename": os.path.basename(file_path)
            }

        except requests.exceptions.RequestException as e:

            return {
                "success": False,
                "error": str(e)
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    def _get_unique_filename(self, file_path):

        if not os.path.exists(file_path):

            return file_path

        directory = os.path.dirname(file_path)

        filename = os.path.basename(file_path)

        name, extension = os.path.splitext(filename)

        counter = 1

        while True:

            new_filename = (
                f"{name}_{counter}{extension}"
            )

            new_path = os.path.join(
                directory,
                new_filename
            )

            if not os.path.exists(new_path):

                return new_path

            counter += 1