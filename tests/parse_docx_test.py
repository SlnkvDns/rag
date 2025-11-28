from scripts.docx_extract import parse_docx_to_dict

def parse_docx_test():
    path = r'data/constitutionrf.docx'
    dct = parse_docx_to_dict(path)
    print(dct[73])

if __name__ == '__main__':
    parse_docx_test()
