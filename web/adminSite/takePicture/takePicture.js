Webcam.set({
    width: 250,
    height: 250,
    image_format: "jpeg",
    jpeg_quality: 90,
  });
  
  Webcam.attach("#my_camera");
  
  function take_snapshot() {
    var i = 1;
    capturePhoto();
  
    function capturePhoto() {
      if (i <= 50) {
        Webcam.snap(function (data_uri) {
          $(".image-tag").val(data_uri);
          document.getElementById("results").innerHTML = ''; // Clear previous images
          document.getElementById("results").innerHTML += '<img src="' + data_uri + '"/>';
  
          $.ajax({
            type: "POST",
            url: "http://localhost/adminSite/takePicture/takePicture.php",
            data: { image: data_uri, imagename: $('#imagename').val() + i },
            success: function (response) {
              console.log(response);
            }
          });
  
          i++;
          setTimeout(capturePhoto, 200); // Delay of 0.2 seconds (200 milliseconds)
          console.log("ez egy kép!")
        });
      }
    }
  }
  