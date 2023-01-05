#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

int main()
{
	std::string image_path = "./images/image.jpg";

	cv::Mat image = cv::imread(image_path, cv::IMREAD_COLOR);

	cv::imshow("Image", image);
	cv::waitKey();

	return 0;

}