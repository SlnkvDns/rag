from typing import List
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from scripts.docx_extract import parse_docx_to_dict


def get_document_chunks_from_docx(path, chunk_size=300, chunk_overlap=50):
    splitted_text = parse_docx_to_dict(path)
    chunks = get_chunks_from_extracted_docx(splitted_text, chunk_size, chunk_overlap)
    return chunks

def get_chunks_from_extracted_docx(splitted_text: List, chunk_size, chunk_overlap):
    documents = []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=['\n\n', '\n', ' ', '']
    )

    for item in splitted_text:
        text = item['text']
        chunked_text = text_splitter.split_text(text)
        for chunk in chunked_text:
            documents.append(
                Document(
                    page_content=chunk,
                    metadata={
                        'section': item['section'],
                        'chapter': item['chapter'],
                        'article': item['article']
                    }
                )
            )
    return documents
