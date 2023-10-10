import PyPDF2
import re

def extract_pdf(pdf_file: str) -> [str]:
    try:
        with open(pdf_file, 'rb') as pdf:
            reader = PyPDF2.PdfReader(pdf, strict=False)
            pdf_text = []

            for page in reader.pages:
                content = page.extract_text()
                pdf_text.append(content)

            return pdf_text
    except FileNotFoundError:
        print(f"Error: The file '{pdf_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def print_words_starting_with_specific_words(text):
    pattern = r'(\d{3})\s+(SE111\w*|SE112\w*|AOL\w*|MAT\w*)'
    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    if matches:
        for match in matches:
            number, word = match
            print(f"Class:{number}, Sub:{word}")

if __name__ == '__main__':
    extracted = extract_pdf('target.pdf')
    if extracted:
        for text in extracted:
            print_words_starting_with_specific_words(text)
