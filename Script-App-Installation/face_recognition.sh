sudo apt-get update
sudo apt-get install build-essential cmake
git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build
cmake ..
cmake --build .
sudo apt-get install python3-setuptools
python3 setup.py install
sudo apt-get -y install python3-pip
pip3 install face_recognition

