#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

int main()
{
	
	//d::string img = "../../../../../../../Users/Andris-PC/Pictures/Camera Roll/img.jpg";
	
	//d::string src = "../../../../../../../Users/Andris-PC/Pictures/Camera Roll/video.mp4";
	

	//webkamera
	cv::VideoCapture cap(0);
	cv::Mat img;

	while (true)
	{
		cap.read(img);
		cv::imshow("Image", img);
		cv::waitKey(1);
	}


	return 0;
}

