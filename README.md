## Snapcraft.yaml changes
gnome-extension for core20 has been used so lot of libraries were not needed. 
##changes in facetracker app
facetracker is based on opencv tracking APIs. It looks like the tracking abstraction in OpenCV has changed a lot so original  sample code 
from Alfonso's repo 

https://github.com/alfonsosanchezbeato/Single_Face_Tracking_using_5_inbuilt_OpenCV_trackers.git

doesn't work. So here I have added facetracker.cpp file. Please replace original repo file with this one so that facetracker will compile.


