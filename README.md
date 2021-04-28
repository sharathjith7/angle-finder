# Angle Finder
Angle Finder is a python program developed to find the angle between any two lines converging at a point on the screen. 
It uses the pygame library to render the images and take user input such as mouse clicks and key presses.

## Usage
This program works in collaboration with snipping tool available in windows or any other software that can be used to copy a part of the screen to the clipboard.

1. Use the snipping tool to select the part of the screen where the angle is displayed.

2. Copy the image to the clipboard by clicking on the copy button present at the top of the snipping tool window.
    ![image](https://user-images.githubusercontent.com/82765715/116001976-fe3e8900-a614-11eb-9a9d-a8dc30d5981e.png)
    
3. Once copied, run the program and it will automatically display the selected image by accessing the clipboard contents.

4. In case the image was not copied to the clipboard or if the contents of the clipboard were in text format, no image would be displayed in the window. 
   Instead the window will ask you to copy an image to the clipboard and then press the ‘v’ key to paste it.
   
5. Now select the three points that make up the two lines(as shown in the figure below), one of the points being the same for both the lines.
  ![Media1(1)](https://user-images.githubusercontent.com/82765715/116003735-d2bf9c80-a61c-11eb-9922-6fc58670c646.gif)
  
6. The angle formed between the two lines will be displayed repeatedly in the python console.

## Use Case
As the exams are being conducted online, to measure and validate the angles drawn in the geometry/drawing exams, this software turns out to be quite useful.
