<!DOCTYPE html>
<html>
<head>
  <title>Person Images</title>
  <style>
    .person {
      display: inline-block;
      margin: 10px;
      text-align: center;
    }
    .person img {
      width: 100px;
      height: 100px;
      object-fit: cover;
    }
  </style>
</head>
<body>
  <h1>Person Images</h1>

  <?php
  include "../../connect.php";

$sql = "SELECT * FROM képek";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $counter = 1; 

    while ($row = $result->fetch_assoc()) {
        $personName = preg_replace('/\d/', '', $row['name']); 
        $imageData = $row['image'];

        if ($counter % 50 == 1) {
            echo '<div class="person">';
            echo '<img src="data:image/jpeg;base64,' . $imageData . '" alt="' . $personName . '">';
            echo '<br>';
            echo '<span>' . $personName . '</span>'; // 
            echo '<br>';
            echo '<a href="delete.php?person=' . $personName . '">Delete</a>';
            echo '</div>';
        }

        $counter++; 
    }
} else {
    echo "No images found.";
}

$conn->close();
?>



</body>
</html>
