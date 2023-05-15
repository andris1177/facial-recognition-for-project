<?php
    include "../../connect.php"
    $img = $_POST['image'];
    $imagename = $_POST['imagename'];
  
    $image_parts = explode(";base64,", $img);
    $image_type_aux = explode("image/", $image_parts[0]);
    $image_type = $image_type_aux[1];
  
    $image_base64 = base64_decode($image_parts[1]);
    $fileName = $imagename . '.jpg';

    // Save the image to a database table
    $sql = "INSERT INTO projekt_feladatok (name, kepke) VALUES (?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $fileName, $image_base64);
    $stmt->execute();
    $stmt->close();

    // Close the database connection
    $conn->close();

    header("Location: takePicture.html");
    exit;
?>