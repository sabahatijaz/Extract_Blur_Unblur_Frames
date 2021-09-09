import PySimpleGUI as sg
sg.theme('Light Blue 2')

layout = [[sg.Text('Folder for 12 Uniqure frames ')],
          [sg.Text('Path for Video ', size=(8, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Text('File to store Blurr ', size=(8, 1)), sg.Input(key='-USERFOLDER1-'), sg.FolderBrowse(target='-USERFOLDER1-')],
         [sg.Text('File to NonBlurr', size=(8, 1)), sg.Input(key='-USERFOLDER2-'), sg.FolderBrowse(target='-USERFOLDER2-')],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('folder ', layout)

event, values = window.read()
window.close()
#print(f'You clicked {event}')
#print(f'You chose filenames {values[0]}')

text_input = values['-USERFOLDER-']
text_input1=values['-USERFOLDER1-']
text_input3=values['-USERFOLDER2-']
import cv2 
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
from skimage import io 
def is_valid(image):

        # Convert image to HSV color space
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Calculate histogram of saturation channel
        s = cv2.calcHist([image], [1], None, [256], [0, 256])

        # Calculate percentage of pixels with saturation >= p
        p = 0.5
        s_perc = np.sum(s[int(p * 255):-1]) / np.prod(image.shape[0:2])

        ##### Just for visualization and debug; remove in final
        '''
        plt.plot(s)
        plt.plot([p * 255, p * 255], [0, np.max(s)], 'r')
        plt.text(p * 255 + 5, 0.9 * np.max(s), str(s_perc))
        plt.show()
        '''
        ##### Just for visualization and debug; remove in final

        # Percentage threshold; above: valid image, below: noise
        s_thr = 0.000035
        #print(s_perc)
        return s_perc > s_thr    
    

# Function to extract frames 
def FrameCapture(path):
    # Program To Read video 
        # and Extract Frames
        #print("cdsdkjhc")
        import cv2 
        #import cv2
        from matplotlib import pyplot as plt
        import numpy as np
        import os
        #from skimage import io  
        
        # Path to video file 
        vidObj = cv2.VideoCapture(path)
        #print("sdjkckdsj")
    
        # Used as counter variable 
        count = 0
        #print("vhbdjfhgvjhdfg")
    
        # checks whether frames were extracted 
        success = 1
        #i=1
    
        while success: 
    
            # vidObj object calls read 
            # function extract frames 
            #print("fdgh")
            success, image = vidObj.read()
            #if(imag.)
            #cv2.imshow("image",image)
            if(success==1):
                noise1 = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                #print(count)
                res=is_valid(noise1)
                if(res==True):
                    #blurr
                    Path = text_input1
                    cv2.imwrite(os.path.join(Path , "frame%d.jpg" % count), image)
                    #cv2.imwrite("Tframe%d.jpg" % count, image)
                else:
                    #nonBlurr
                    #cv2.imwrite("Fframe%d.jpg" % count, image)
                    Path = text_input3
                    cv2.imwrite(os.path.join(Path , "frame%d.jpg" % count), image)
            
            
    
            # Saves the frames with frame-count 
            #if(success==1):
                #cv2.imwrite("frame.jpg", image)
            #   laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
            #  if laplacian_var < 70:
            #     print("Image blurry")
                #    cv2.imwrite("Blurrframe%d.jpg" % count, image)
                #else:
                #   cv2.imwrite("frame%d.jpg" % count, image)
            
    
            count += 1
        
# Driver Code 
if __name__ == '__main__': 
  # Calling the function 
    FrameCapture(text_input) 