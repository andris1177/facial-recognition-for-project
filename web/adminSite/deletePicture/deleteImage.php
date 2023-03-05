<?php

if (isset($_GET['imageName'])) {
    $imageName = $_GET['imageName'];

    $folderPath = '../takePicture/images/';

    if (file_exists($folderPath . $imageName . '.jpg')) {
        if (unlink($folderPath . $imageName . '.jpg')) {
            // sikeres törlés
            echo 'Image "' . $imageName . '" was deleted.';
            header('Location: listimage.php');
            exit;
        } else {
            // nem sikerült a képet törölni
            echo 'Error: Failed to delete image "' . $imageName . '".';
        }
    } else {
        echo 'Error: Image file "' . $imageName . '" does not exist.';
    }
} else {
    echo 'Error: Image name not provided.';
}

?>

