import fitz  # PyMuPDF

def pdf_yukle_ve_bol(pdf_dosyasi):
    """
    PDF dosyasını alır, her sayfanın metnini ayrı bir liste elemanı olarak döndürür.
    """
    doc = fitz.open(stream=pdf_dosyasi.read(), filetype="pdf")
    sayfalar = [sayfa.get_text("text") for sayfa in doc]
    return sayfalar
