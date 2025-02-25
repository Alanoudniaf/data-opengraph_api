# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""
import requests
def fetch_metadata(url):
    """
    Returns the "data" dictionary of OpenGraph metadata found in HTML of given url
    """
    if not url:
        return {}
    response = requests.get(f"https://opengraph.lewagon.com/?url={url}")
    if response.status_code == 200:
        return response.json().get("data", {})
    return {}
# # To manually test, uncomment the following lines and run `python opengraph.py`:
# if __name__ == "__main__":
#     import pprint
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(fetch_metadata("https://www.github.com"))
