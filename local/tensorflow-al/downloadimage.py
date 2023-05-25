import mysql.connector
import base64
import os
import shutil

def delete_old_images():
    for folder_name in os.listdir("dataset/positive/"):
        folder_path = os.path.join("dataset/positive/", folder_name)
        
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
    print("Az összes régi képet tartalmazó mappa törlve.")

def save_image_from_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="")

    cursor = db.cursor()

    cursor.execute("SELECT image, name FROM projekt_feladat.képek")

    for row in cursor:
        image_data = row[0]
        name = row[1]
        image_bytes = base64.b64decode(image_data)
        name_without_number = name.rstrip('0123456789')

        directory = name_without_number.replace(" ", "_")
        destination_folder = "dataset/positive"

        if not os.path.exists(os.path.join(destination_folder, directory)):
            os.makedirs(os.path.join(destination_folder, directory))

        with open(os.path.join(destination_folder, directory, name + ".jpg"), "wb") as file:
            file.write(image_bytes)

        print(f"{name} successfully saved.")

    cursor.close()
    db.close()

def run():
    delete_old_images() 
    save_image_from_database()

run()

