import os
import PyPDF2

def pdf_to_text(filename: str, outfile: str) -> None:
    """
    Converts a PDF file to text
    :param filename: The path to the PDF file
    :return: The text contained in the PDF file
    """
    pdfs = PyPDF2.PdfFileReader(filename)
    txts = ""
    for i in range(pdfs.getNumPages()):
        txts += pdfs.getPage(i).extractText()
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(txts)
    return 

def extract_all_pdfs(pdfs_dir: str, out_dir: str) -> None:
    """
    Extracts all PDFs from a directory
    :param pdfs_dir: The directory containing the PDFs
    :param out_dir: The directory to write the extracted text files to
    :return: None
    """
    for filename in os.listdir(pdfs_dir):
        if filename.endswith(".pdf"):
            pdf_to_text(pdfs_dir + filename, out_dir + filename.replace(".pdf", ".txt"))
    return
    
if __name__ == "__main__":
    extract_all_pdfs("pdfs/", "txts/")