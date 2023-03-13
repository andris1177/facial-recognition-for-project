<link rel="stylesheet" href="../../style.css">;
<?php
    $working_dir = getcwd();
    
    $img_dir = $working_dir . "/../takePicture/images/";

    chdir($img_dir);
    
    $files = glob("*.{jpg,jpeg,png,gif,JPG,JPEG,PNG,GIF}", GLOB_BRACE );
    
    chdir($working_dir);

    ?>

    <div id="deleteImage">

    <?php
    echo "<table>";
    echo "<tr><th>Image</th><th>Name</th><th>Delete</th></tr>";

    foreach ($files as $file) {
        $image_name = pathinfo($file, PATHINFO_FILENAME);
        $encoded_image_name = urlencode($image_name);
    
        echo "<tr>";
        echo "<td><img src='$img_dir" . urlencode($file) . "' style='height: 200px; width: 200px;'/></td>";
        echo "<td>$image_name</td>";
        echo "<td><button onclick='deleteImage(\"$encoded_image_name\")'>Delete</button></td>";
        echo "</tr>";
    }
    
    
    echo "</table>";

    ?>

    </div>

    <?php

?>

<script>
    function deleteImage(imageName) {
        var url = "deleteImage.php?imageName=" + imageName;
        window.location.href = url;
    }
</script>
