<?php
include "../../connect.php";

for ($i = 1; $i <= 50; $i++) {
    $img = $_POST['image'];
    $imagename = $_POST['imagename'] . $i;

    $image_data = str_replace('data:image/jpeg;base64,', '', $img);

    $sql = "INSERT INTO képek (name, image) VALUES (?, ?)";
    $stmt = $conn->prepare($sql);

    $stmt->bind_param("ss", $imagename, $image_data);
    $stmt->execute();
}

header("Location: takePicture.html");
exit; 
?>
