import PyPDF2
from sentence_transformers import SentenceTransformer
import os
folder_path = r"C:\Users\Sudarshan\Desktop\files for project"
pdfpages = []
chunk_size = 200
chunk_overlap = 50 
text_chunks = []
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

#chunking.....
for page_data in pdfpages:
    text = page_data["text"]
    words = text.split()

    #here we run chunking loop inside the page loop because we dont want the words of two files mix with eachother 
    for i in range (0 , len(words),chunk_size-chunk_overlap):
        chunk_words= words [i:i+chunk_size]
        chunk_text = " ".join(chunk_words)
        text_chunks.append({
            "document_name": page_data["document_name"],
            "page_number": page_data["page_number"],
            "chunk_index":(i//(chunk_size-chunk_overlap))+1,
            "text":chunk_text  
        })

#GENERATING EMBEDDING 
batch_size = 20
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2') #384 dimensional encoding per chunk 
texts = [chunk["text"] for chunk in text_chunks ]
embeddings = model.encode(
    texts , 
    batch_size=20,
    show_progress_bar=True,
    normalize_embeddings=False
)
print(f" Sample embedding (first 5 values) for first chunk: {embeddings[0][:5]}")













        

