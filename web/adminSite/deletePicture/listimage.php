<?php
    $working_dir = getcwd();
    
    $img_dir = $working_dir . "/../takePicture/images/";

    chdir($img_dir);
    
    $files = glob("*.{jpg,jpeg,png,gif,JPG,JPEG,PNG,GIF}", GLOB_BRACE );
    
    chdir($working_dir);

    echo "<table>";
    echo "<tr><th>Image</th><th>Name</th><th>Delete</th></tr>";
    
    foreach ($files as $file) {
        $image_name = pathinfo($file, PATHINFO_FILENAME);
        
        echo "<tr>";
        echo "<td><img src='images/$file' style='height: 200px; width: 200px;'/></td>";
        echo "<td>$image_name</td>";
        echo "<td><button onclick='deleteImage(\"$image_name\")'>Delete</button></td>";
        echo "</tr>";
    }
    
    echo "</table>";
?>

<script>
    function deleteImage(imageName) {
        var url = "deleteImage.php?imageName=" + imageName;
        window.location.href = url;
    }
</script>
