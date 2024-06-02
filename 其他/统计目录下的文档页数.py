import os
import comtypes.client


def get_word_page_count(docx_path):
    try:
        # Initialize the COM object
        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = False

        # Open the document
        doc = word.Documents.Open(docx_path)

        # Get the page count
        page_count = doc.ComputeStatistics(2)  # 2 = wdStatisticPages

        # Close the document and quit Word
        doc.Close()
        word.Quit()

        return page_count
    except Exception as e:
        print(f"Error opening {docx_path}: {e}")
        return None


def get_all_docx_page_counts(directory):
    page_counts = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.docx'):
                docx_path = os.path.join(root, file)
                page_count = get_word_page_count(docx_path)
                if page_count is not None:
                    page_counts[docx_path] = page_count
    return page_counts


if __name__ == "__main__":
    # 指定目录路径
    directory = "C:\\Users\\Administrator\\Desktop\\软著\\测试文档"

    page_counts = get_all_docx_page_counts(directory)

    if page_counts:
        for docx_path, page_count in page_counts.items():
            print(f"{docx_path}: {page_count} pages")
    else:
        print("No Word documents found or unable to read page counts.")
