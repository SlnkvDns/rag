from docx import Document

def parse_docx_to_dict(file_path):
    doc = Document(file_path)
    
    data = []
    
    current_section = ""
    current_chapter = ""
    current_article = ""
    current_text = [] 
    
    for para in doc.paragraphs:
        text = para.text.strip()
        
        if not text:
            continue
        
        level = None
        pPr = para._element.pPr
        
        if pPr is not None:
            outlineLvl = pPr.find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}outlineLvl')
            if outlineLvl is not None:
                level = int(outlineLvl.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val'))
        
        if level in [0, 1, 2]:
            if current_text:
                entry = {
                    "text": "\n".join(current_text),  
                    "section": current_section,
                    "chapter": current_chapter,
                    "article": current_article,
                }
                data.append(entry)
                current_text = []  
            
            if level == 0:  
                current_section = text
                current_chapter = ""
                current_article = ""
                
            elif level == 1:  
                current_chapter = text
                current_article = ""
                
            elif level == 2:  
                current_article = text
        else:
            if current_chapter and not current_article:
                current_chapter += " " + text
            else:
                current_text.append(text)
    
    if current_text:
        entry = {
            "text": "\n".join(current_text),
            "section": current_section,
            "chapter": current_chapter,
            "article": current_article,
        }
        data.append(entry)
    
    return data
