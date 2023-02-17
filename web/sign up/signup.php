<?php
include '../connect.php';
 $username = $_POST['username'];
 $password = $_POST['password'];

 $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
 $sql = "INSERT INTO users (username, password) VALUES ('$username', '$hashedPassword')";

if ($conn->query($sql) === TRUE) {
    header("Location: ../login/login.html");
    exit;
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
