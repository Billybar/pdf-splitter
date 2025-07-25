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

    # Example 1: Split pages 2 to 4 from 'example.pdf'
    print("--- Running Example 1 ---")
    split_pdf_by_range('C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\חוברת הקורס.pdf', 'C:\\Users\\Reception-IL\\Downloads\\billy\\computer_network\\mmh-1.pdf', 11, 14)
    print("\n")

    # Example 2: Try to split a non-existent file
    print("--- Running Example 2 (Non-existent file) ---")
    split_pdf_by_range('non_existent.pdf', 'output_non_existent.pdf', 1, 2)
    print("\n")

    # Example 3: Try with invalid page range (assuming 'example.pdf' exists and has enough pages)
    # You might need to create a 'example.pdf' for this to demonstrate correctly
    print("--- Running Example 3 (Invalid page range) ---")
    split_pdf_by_range('example.pdf', 'output_invalid_range.pdf', 1,
                       999)  # Assuming example.pdf has fewer than 999 pages
    print("\n")

    # Example 4: Start page greater than end page
    print("--- Running Example 4 (Start > End page) ---")
    split_pdf_by_range('example.pdf', 'output_start_gt_end.pdf', 5, 2)
    print("\n")

    # To run this script:
    # 1. Save the code as a .py file (e.g., pdf_splitter.py).
    # 2. Make sure you have a PDF file named 'example.pdf' in the same directory,
    #    or update the 'input_pdf_path' variable to your PDF's actual path.
    # 3. Open your terminal or command prompt.
    # 4. Navigate to the directory where you saved the file.
    # 5. Run the script using: python pdf_splitter.py
