<?php
include "../../connect.php";

$img = $_POST['image'];
$imagename = $_POST['imagename'];

$image_data = str_replace('data:image/jpeg;base64,', '', $img);

$sql = "INSERT INTO képek (name, image) VALUES (?, ?)";
$stmt = $conn->prepare($sql);

$stmt->bind_param("ss", $imagename, $image_data);
$stmt->execute();

$stmt->close();

$conn->close();

header("Location: takePicture.html");
exit; 
