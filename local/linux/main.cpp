#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

int main()
{
	std::cout << "esc to quit" << std::endl;

	std::string image_path = "../../../web/images/";

	cv::Mat webcam;
	cv::namedWindow("Webcam preview");
	cv::VideoCapture cap(0);
	if (!cap.isOpened())
	{
		std::cout << "No webcam detected!" << std::endl;
		return -1;
	}

	while (true)
	{
		cap >> webcam;
		if (webcam.empty())
		{
			break;
		}

		cv::imshow("Webcam preview", webcam);
		char c = (char)cv::waitKey(25);
		if (c == 27)
		{
			break;
		}
	}

	return 0;

}