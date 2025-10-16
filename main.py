from gemini_utils import reconstruct_text
from search_utils import search_content
from report_utils import generate_report
import sys

def main():
    if len(sys.argv) < 2:
        print("usage: python main.py \"fragmented text here\"")
        return 

    fragment = sys.argv[1]
    print("\n--- Processing --- \n")

    reconstructed = reconstruct_text(fragment)
    links = search_content(reconstructed)
    report = generate_report(fragment, reconstructed, links)

    print(report)

if __name__ == "__main__":
    main()
