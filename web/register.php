<?php

include(__DIR__ . '/connect.php');
$code = 123456789;
$username = $_POST['user'];  
$password = $_POST['pass'];
$specialCode = $_POST['spec'];

//to prevent from mysqli injection  
$username = stripcslashes($username);  
$password = stripcslashes($password);  
$username = mysqli_real_escape_string($con, $username);  
$password = mysqli_real_escape_string($con, $password);

if ($specialCode == $code){
    $query = "INSERT INTO users (username, password) VALUES ('$username', '$password')";
    mysqli_query($con, $query);
}
      

?>