import mysql.connector
import base64
import os
import shutil

def check_create_folder(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
            print(f"{folder_path} folder created.")
        except OSError as e:
            print(f"Error creating {folder_path} folder: {e}")
    else:
        print(f"{folder_path} folder already exists.")

def delete_old_images():
    file_list = os.listdir("dataset/")

    # Iterate over the files and delete them one by one
    for file_name in file_list:
        file_path = os.path.join("dataset/", file_name)  # Get the full file path
        if os.path.isfile(file_path):  # Check if it's a file
            os.remove(file_path)  # Delete the file
    print("Az összes régi képet tartalmazó mappa törlve.")

def save_image_from_database():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="")

    cursor = db.cursor()

    cursor.execute("SELECT image, name FROM projekt_feladat.képek")
    counter = 0
    for row in cursor:
        if counter == 0 or counter % 50 == 0:
            image_data = row[0]
            name = row[1]
            image_bytes = base64.b64decode(image_data)
            name_without_number = name.rstrip('0123456789')

            destination_folder = "dataset"

            with open(os.path.join(destination_folder +"/" +name_without_number + ".jpg"), "wb") as file:
                file.write(image_bytes)

            print(f"{name} successfully saved.")
        counter += 1

    cursor.close()
    db.close()

def run():
    check_create_folder("dataset/")
    delete_old_images() 
    save_image_from_database()

run()
