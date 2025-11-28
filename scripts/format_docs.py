from langchain.schema import Document

def format_docs(docs):
    formated_docs = []
    for doc in docs:
        formatted_content = f"""
[SECTION]: {doc.metadata['section']}
[CHAPTER]: {doc.metadata['chapter']}
[ARTICLE]: {doc.metadata['article']}

[CONTENT]:
{doc.page_content}
"""

        formated_docs.append(
            Document(
                page_content=formatted_content,
                metadata={
                    'section': doc.metadata['section'],
                    'chapter': doc.metadata['chapter'],
                    'article': doc.metadata['article']
                }
            )
        )
    return formated_docs
