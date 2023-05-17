import mysql.connector
import base64
import os

folder_path = "images/"

def check_createfolder():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")

def delete_old_images():
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("Old image deleted!")

def save_image_from_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = db.cursor()

    cursor.execute("SELECT image, name FROM projekt_feladat.képek")

    for row in cursor:
        image_data = row[0]
        name = row[1]
        image_bytes = base64.b64decode(image_data)

        with open('images/' + name + ".jpg", "wb") as file:
            file.write(image_bytes)

        print(f"Image '{name}' saved successfully.")

    cursor.close()
    db.close()

check_createfolder()
delete_old_images()
save_image_from_database()
