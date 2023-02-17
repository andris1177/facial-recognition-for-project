<?php
include '../connect.php';
 $username = $_POST['username'];
 $password = $_POST['password'];

 $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
 $result = mysqli_query($conn, $sql);

 if (mysqli_num_rows($result) == 1) {
    header("Location: ../adminSite/mainSite.html");
    exit;
 } else {
    echo "Bad usernaem or password";
 }
?>