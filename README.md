Please read the below if you are having a hard time with importing the data set. 

The challenge is two fold.

How Gitlab names the zip files within the zip.
Oggdude's program being very specific on file names.

Currently Gitlab does not offer a way to change the naming convention on downloads. And Oggdude has not found/changed the program to accept different naming conventions.
Link to the detailed solution: #3 (closed)
Solution Summary:

If you download using the *.tar option instead of the *.zip function it should fix the issue with the Windows 10 zip problem.
The file has to be named "SWDataSet-(NAME)" and first folder inside has to be "Dataset_(NAME)"

Recommend shortening the folder name to just "SWDataSet-(NAME)" and verifying the first folder inside is labled "Dataset_(NAME)".
