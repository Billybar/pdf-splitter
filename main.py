import PyPDF2
import os


def split_pdf_by_range(input_pdf_path, output_pdf_path, start_page, end_page):
    """
    Splits a PDF file by a specified range of pages.

    Args:
        input_pdf_path (str): The path to the input PDF file.
        output_pdf_path (str): The path where the new split PDF will be saved.
        start_page (int): The starting page number (1-indexed).
        end_page (int): The ending page number (1-indexed).
    """
    try:
        # Check if the input PDF file exists
        if not os.path.exists(input_pdf_path):
            print(f"Error: Input PDF file not found at '{input_pdf_path}'")
            return

        # Open the input PDF file in binary read mode
        with open(input_pdf_path, 'rb') as infile:
            reader = PyPDF2.PdfReader(infile)
            writer = PyPDF2.PdfWriter()

            num_pages = len(reader.pages)

            # Validate page numbers
            if not (1 <= start_page <= num_pages and 1 <= end_page <= num_pages):
                print(f"Error: Invalid page range. The PDF has {num_pages} pages.")
                print(
                    f"Please ensure start_page ({start_page}) and end_page ({end_page}) are within 1 and {num_pages}.")
                return

            if start_page > end_page:
                print("Error: Start page cannot be greater than end page.")
                return

            # PyPDF2 uses 0-based indexing for pages, so adjust accordingly
            for page_num in range(start_page - 1, end_page):
                writer.add_page(reader.pages[page_num])

            # Open the output PDF file in binary write mode
            with open(output_pdf_path, 'wb') as outfile:
                writer.write(outfile)

        print(f"Successfully split '{input_pdf_path}' from page {start_page} to {end_page}.")
        print(f"Output saved to '{output_pdf_path}'")

    except PyPDF2.errors.PdfReadError:
        print(f"Error: Could not read PDF file '{input_pdf_path}'. It might be corrupted or encrypted.")
    except FileNotFoundError:
        print(f"Error: File not found. Please check the paths.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Example Usage ---
if __name__ == "__main__":
    # IMPORTANT: Replace 'input.pdf' with the actual path to your PDF file
    # and 'output_split.pdf' with your desired output file name.

    # -- book
    # split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\book.pdf', 'chapter 1.pdf', 24, 88+24)
    # split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\book.pdf', 'chapter 2.pdf', 89+24,192 + 24)
    # split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\book.pdf', 'chapter 3.pdf', 193+24,255 + 24)
    # split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\book.pdf', 'chapter 4.pdf', 257 +24,354 + 24)
    # split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\book.pdf', 'chapter 5.pdf', 355+24,494 + 24)
    # split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\book.pdf', 'chapter 6.pdf', 495+24,610 + 24)
    # split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\book.pdf', 'chapter 7.pdf', 611+24,762 + 24)

    # -- course_notebook
    #split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\course_notebook.pdf', 'mmh1.pdf', 24,88 + 24)
    #split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\course_notebook.pdf', 'mmn11.pdf',15, 17)
    #split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\course_notebook.pdf', 'mmh2.pdf',19, 23)
    #split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\course_notebook.pdf', 'mmh3.pdf',25, 28)

    # -- study_notebook
    split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\course_notebook.pdff','SN_chapter 2.pdf', 17, 29)
    #split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\study_notebook.pdf', 'SN_chapter 2.pdf',17, 29)
    #split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\study_notebook.pdf', 'SN_chapter 3.pdf',31, 49)
    #split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\study_notebook.pdf', 'SN_chapter 4.pdf',51, 65)
    #split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\study_notebook.pdf','SN_chapter 5.pdf', 67, 96)
    #split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\study_notebook.pdf','SN_chapter 6.pdf', 97, 113)


    # To run this script:
    # 1. Save the code as a .py file (e.g., pdf_splitter.py).
    # 2. Make sure you have a PDF file named 'example.pdf' in the same directory,
    #    or update the 'input_pdf_path' variable to your PDF's actual path.
    # 3. Open your terminal or command prompt.
    # 4. Navigate to the directory where you saved the file.
    # 5. Run the script using: python pdf_splitter.py
