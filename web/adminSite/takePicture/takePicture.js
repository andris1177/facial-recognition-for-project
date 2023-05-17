Webcam.set({
    width: 490,
    height: 390,
    image_format: "jpeg",
    jpeg_quality: 90,});

Webcam.attach("#my_camera");

function take_snapshot() {
  for (let i = 1; i <= 50; i++) {
      Webcam.snap(function (data_uri) {
          $(".image-tag").val(data_uri);
          document.getElementById("results").innerHTML +=
              '<img src="' + data_uri + '"/>';
          
          // Add AJAX request to save the image
          $.ajax({
              type: "POST",
              url: "saveImage.php",
              data: { image: data_uri, imagename: 'usergivenname' + i },
              success: function (response) {
                  console.log(response);
              }
          });
      });
  }
}