import mysql.connector
import base64
import os
import shutil

def delete_old_images():
    for folder_name in os.listdir("positive/"):
        folder_path = os.path.join("positive/", folder_name)
        
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
    print("All folders deleted!")
    

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

        directory = name_without_number.replace(" ", "_")  #
        if not os.path.exists(os.path.join("anchor", directory)):
            os.makedirs(os.path.join("anchor", directory))

        with open(os.path.join("anchor", directory, name + ".jpg"), "wb") as file:
            file.write(image_bytes)

        print(f"Image '{name}' saved successfully.")

    cursor.close()
    db.close()

def run():
    delete_old_images() 
    save_image_from_database()
