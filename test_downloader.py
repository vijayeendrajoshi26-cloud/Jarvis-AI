from browser.downloader import Downloader


downloader = Downloader()


url = "https://www.python.org/static/img/python-logo.png"


result = downloader.download(url)


if result["success"]:

    print("=" * 60)
    print("DOWNLOAD SUCCESSFUL")
    print("=" * 60)

    print("Filename:")
    print(result["filename"])

    print()

    print("File Path:")
    print(result["file_path"])

else:

    print("=" * 60)
    print("DOWNLOAD FAILED")
    print("=" * 60)

    print(result["error"])