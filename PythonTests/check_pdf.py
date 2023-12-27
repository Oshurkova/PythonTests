import os
import fitz

directory = 'files_check'

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):

        doc = fitz.open(file_path)
        incorrect = False
        for page_num in range(doc.page_count):
            page = doc[page_num]
            blocks = page.get_text("blocks")

            for block in blocks:
                table_rect = fitz.Rect(block[:4])
                
                for inner_block in blocks:
                    if inner_block != block:
                        inner_rect = fitz.Rect(inner_block[:4])
                        
                        if table_rect.intersects(inner_rect):
                            incorrect = True

        if incorrect:
            print(f"Наложения в документе {file_path}")