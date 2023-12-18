from pyzotero import zotero
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ZOTERO_API_KEY = os.getenv("ZOTERO_API_KEY")
ZOTERO_USER_ID = os.getenv("ZOTERO_USER_ID")

zot = zotero.Zotero(ZOTERO_USER_ID, "user", ZOTERO_API_KEY)

# function to retrieve all items from a collection in zotero
def get_collection_items(collection_id):
    items = zot.collection_items_top(collection_id)
    return items

# function to retrieve all items in a user's library
def get_all_items():
    items = zot.everything(zot.top())
    return items

# items = zot.top(limit=5)
items =  get_collection_items('FTNIZNKN')
for item in items:
    print(items)