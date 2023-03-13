#include <iostream>
#include <fstream>
#include <opencv2/opencv.hpp>
#include <opencv2/face.hpp>

using namespace cv;
using namespace cv::face;

int main()
{
    std::string imagePath = "../../../../web/adminSite/takePicture/images/";
    CascadeClassifier face_cascade;
    face_cascade.load("cascades/haarcascades/haarcascade_frontalface_alt.xml");
    Ptr<LBPHFaceRecognizer> recognizer = LBPHFaceRecognizer::create();
    return 0;
}
