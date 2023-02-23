#include <iostream>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/objdetect.hpp>

int main()
{
	cv::VideoCapture video(0);
	cv::CascadeClassifier facedetect;
	cv::Mat img;
	facedetect.load("C:/github local/facial-recognition-for-project/local/windows/FaceRec/src/cascades/haarcascades/haarcascade_frontalface_default.xml");
	while (true)
	{
		video.read(img);
		std::vector<cv::Rect> faces;
		facedetect.detectMultiScale(img, faces, 1.3, 5);
		for (int i = 0; i < faces.size(); i++)
		{
			cv::rectangle(img, faces[i].tl(), faces[i].br(), cv::Scalar(50, 50, 255), 3);
		}
		cv::imshow("Preview", img);
		cv::waitKey(1);
	}

	return 0;
}