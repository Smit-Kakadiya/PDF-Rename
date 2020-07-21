from pyPdf import PdfFileReader
import os
import re

# Retrive all the files from the current directory
for fileName in os.listdir('.'):
    try:
        # Process nly the pdf files.
        if fileName.lower()[-3:] != "pdf":
            continue

        # Print the file name.
        print("Processing " + fileName)

        # Retrive the Title of the pdf.
        pdfReader = PdfFileReader(file(fileName, "rb"))
        title = pdfReader.getDocumentInfo().title
        # close the pdf
        pdfReader.stream.close()
        
        # Not all the PDFs contain the Title meta-info.
        # If the Title info is not available print the "Title: None" message.
        if title is None:
            print("Title: None")
        else:
            # Print the Title.
            print("Title: " + title)

            # Format the Title by removing any special characters.
            newName = re.sub('[^-a-zA-Z0-9_.() ]+', '', title) + ".pdf"

            # Ask the user for confirmation because sometimes the Title information can be wrong.
            option = raw_input("Do you want to rename '" + fileName + "'' to '" + newName + "'? [y][n]: ")
            option = option.lower()

            # If user really wants to rename the file, rename it.
            if(option.startswith('y')):
                os.rename(fileName, newName)

        # Print an empty line.
        print("")
    except:
        print("Error in processing: " + fileName)