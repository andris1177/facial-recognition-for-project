<?php
include '../connect.php';

$username = $_POST['username'];
$password = $_POST['password'];

$sql = "SELECT password FROM users WHERE username = '$username'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  $row = $result->fetch_assoc();
  $hashedPassword = $row['password'];

  if (password_verify($password, $hashedPassword)) {
    session_start();
    $_SESSION['username'] = $username;
    header("Location: ../adminSite/mainSite.html");
    exit;
  } else {
    echo "Bad username or password";
  }
} else {
  echo "Bad username or password";
}

$conn->close();
?>
