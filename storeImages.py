import sqlite3
from urllib.request import  urlopen, HTTPError, URLError

# test image
src = "https://i.ebayimg.com/00/s/MTYwMFgxMjAw/z/iYYAAOxydgZTJwYc/$_1.JPG?set_id=880000500F"

try:
    img = urlopen(src).read()
    open("target.jpg", "wb").write(img)

except HTTPError:
    print("HTTP Error,Image not available")

except URLError:
    print("URL Error, Image cannot be downloaded")

#Creating a localDB
conn = sqlite3.connect('SQLite_Python.db')

c = conn.cursor()

c.execute("""CREATE TABLE images ( id INTEGER PRIMARY KEY,  photo BLOB NOT NULL)
        """)
conn.commit()
conn.close()


def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(imgId, photo):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_blob_query = """ INSERT INTO images
                                  (id,photo) VALUES (?, ?)"""

        imgPhoto = convertToBinaryData(photo)
        data_tuple = (imgId, imgPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")


insertBLOB(1, "/Users/kapildarsi/Desktop/eBay Competition/2021/target.jpg")

