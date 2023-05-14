Webcam.set({
    width: 1920,
    height: 1080,
    image_format: "jpeg",
    jpeg_quality: 90,});

Webcam.attach("#my_camera");

function take_snapshot() {
Webcam.snap(function (data_uri) {
 $(".image-tag").val(data_uri);
 document.getElementById("results").innerHTML =
   '<img src="' + data_uri + '"/>';
});
}