# Aruco-Markers
Detecting aruco markers

1. We will use opencv to detect aruco markers with the help pf numpy.
2. At first we will take the list of aruco markers and detect it's parameters from DetectorParameters_create() function.
3. Then we will create a variable for capturiing the video.
4. In while loop we create variiable ret and frame which will read the video.
5. We will convert this into gray scale.
6. Then we will create variables for corners and IDs and in for loop using polylines we can make lines around the frame.
7. After this we will take the text input to show the id using putText().
8. At last we will show the image using imshow().
![image](https://user-images.githubusercontent.com/91333702/199022151-fe81fbc2-937b-4287-bd5b-e07256f63c15.png)
