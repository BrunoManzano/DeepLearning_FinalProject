# Project Structure

## Folders:

**"7" Folder:** This folder contains the character dataset. It includes images of individual characters used to train the CNN model for recognizing individual characters.\
**"9" Folder:** This folder contains the names dataset. It includes images of whole names that will be processed by the trained CNN model to recognize and extract individual characters.

## Files:

**CNN_New.py:** This file contains the complete code for training the CNN model and using it to recognize characters from images. It also contains the code for the RNN.\
**compare.py:** This file computes the real accuracy of the CNN predictions by comparing the recognized characters with the actual characters in the names dataset.