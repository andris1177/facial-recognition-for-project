<?php
include '../connect.php';
 $username = $_POST['username'];
 $password = $_POST['password'];

 $sql = "SELECT * FROM users WHERE username = '$username'";
 $result = mysqli_query($conn, $sql);
 
 if (mysqli_num_rows($result) > 0) {
     $row = mysqli_fetch_assoc($result);
     if (password_verify($password, $row["password"])) {
        header("Location: ../adminSite/mainSite.html");
        exit();
     } else {
         // Rossz jelszó
     }
 } else {
     // Rossz felhasználónév
 }
?>