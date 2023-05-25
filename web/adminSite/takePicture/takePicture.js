Webcam.set({
  width: 250,
  height: 250,
  image_format: "jpeg",
  jpeg_quality: 90,
});

Webcam.attach("#my_camera");

function take_snapshot() {
  var imagename = $('#imagename').val(); // Get the imagename from the input field
  capturePhoto(1);

  function capturePhoto(i) {
    if (i <= 50) {
      Webcam.snap(function (data_uri) {
        $(".image-tag").val(data_uri);
        document.getElementById("results").innerHTML = '<img src="' + data_uri + '"/>'; // Update the image element

        $.ajax({
          type: "POST",
          url: "http://localhost/adminSite/takePicture/takePicture.php",
          data: { image: data_uri, imagename: imagename + i },
          success: function (response) {
            console.log(response);
            setTimeout(function () {
              capturePhoto(i + 1); // Capture the next photo after a delay
            }, 300);
          }
        });
      });
    }
  }
}
