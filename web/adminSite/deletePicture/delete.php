<?php
include "../../connect.php";

if (isset($_GET['person'])) {
    $personName = $_GET['person'];

    for ($i = 1; $i <= 50; $i++) {
        $imageName = $personName . $i;
        $sql = "DELETE FROM képek WHERE name = '$imageName'";
        if ($conn->query($sql) !== TRUE) {
            echo "Error deleting images for name: " . $conn->error;
            break;
        }
    }

    echo "Images deleted successfully.";
    header("Location: deleteImage.php");
    exit; 

    $conn->close();
} else {
    echo "Invalid request.";
}
?>
