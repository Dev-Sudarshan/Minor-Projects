import PyPDF2
import os
folder_path = r"C:\Users\Sudarshan\Desktop\files for project"
pdfpages = []
for file in os.listdir(folder_path):
    file_path = os.path.join (folder_path , file)
    with open(file_path, 'rb') as f :
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text= page.extract_text()
            cleaned_text = text.replace('\n', ' ').strip()
            page_data = {
                "document_name":file,
                "page_number":page_number+1,
                "text": cleaned_text
            }
            pdfpages.append(page_data)




        

