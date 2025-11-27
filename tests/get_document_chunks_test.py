from scripts.chuncking import get_document_chunks_from_docx

def get_document_chunks_from_docx_test():
    path = r'data/constitutionrf.docx'
    chunks = get_document_chunks_from_docx(path, chunk_size=300, chunk_overlap=50)
    print(chunks[99:105])


if __name__ == '__main__':
    get_document_chunks_from_docx_test()
