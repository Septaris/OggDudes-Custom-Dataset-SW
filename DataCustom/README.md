Please read the below if you are having a hard time with importing the data set.

The challenge is two fold.

1. How Gitlab names the zip files within the zip.
2. Oggdude's program being very specific on file names.

Currently Gitlab does not offer a way to change the naming convention on downloads. And Oggdude has not found/changed the program to accept different naming conventions.

Link to the detailed solution: https://gitlab.com/rikus01/SWDataSet-OggDudes/-/issues/3#related-issues

Solution Summary:

1. If you download using the \*.tar option instead of the \*.zip function it should fix the issue with the Windows 10 zip problem.
2. The file has to be named "SWDataSet-(NAME)" and first folder inside has to be "DataSet*(NAME)". Please note that (NAME) has to be the exact same for both folders (including case). In addition, the program is both naming and case specific. If you are encountering an error double check the naming convention and make sure it matches exactly how it is above. For example: the first folder inside the zip uses an underscore "*" ; not a dash "-".
