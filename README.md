# Research-paper-organizer
This Python program allows you to add, view, and search through a collection of research papers and notes. It stores entries in a CSV file for easy organization and retrieval.
Research Paper Organizer

A simple Python application to organize, store, and search through a collection of research papers. This tool helps you keep track of your research papers by allowing you to add details like title, author, year, topic, link, and notes, and it stores everything in a CSV file for easy retrieval.
Features

    Add a New Paper: Enter details such as title, author, year, topic, link, and notes.
    View All Papers: Displays all stored research papers in a formatted way.
    Search by Topic: Allows searching for papers based on a topic keyword.
    CSV Storage: Saves all entries to a research_papers.csv file for easy access and future use.

Requirements

    Python 3.x

No additional libraries are required as this program uses only standard Python libraries.
How to Run

    Download or clone the repository.
    Navigate to the project folder.
    Run the program by entering:

    python research_organizer.py

Usage
Menu Options

    Add a New Paper: Choose this option to enter details for a new research paper. You’ll be prompted to enter:
        Title
        Author
        Year
        Topic
        Link (DOI or URL)
        Notes

    The details will be stored in research_papers.csv.

    View All Papers: Displays all papers currently stored in research_papers.csv.

    Search Papers by Topic: Prompts you to enter a topic keyword. It will display all papers with matching topics.

    Exit: Exits the program.

Example
Adding a Paper

Enter Title: A Study on Artificial Intelligence
Enter Author: John Doe
Enter Year: 2022
Enter Topic: AI
Enter Link: https://doi.org/10.1000/xyz123
Enter Notes: Excellent paper on AI methodologies.

Viewing Papers

Title: Streamed Video Reconstruction for Firefox Browser Forensics
Author: Mahmoud Eltayeb
Year: 2022
Topic: AI
Link: https://doi.org/10.1000/xyz123
Notes: Excellent paper on AI methodologies.
--------------------------------------------------

Searching by Topic

If you search by "AI," all papers tagged with "AI" in the topic field will be displayed.
CSV File

All entries are stored in research_papers.csv in the following format:

Title,Author,Year,Topic,Link,Notes

Example CSV Entry

A Study on Artificial Intelligence,John Doe,2022,AI,https://doi.org/10.1000/xyz123,Excellent paper on AI methodologies.

Future Enhancements

Potential improvements include:

    Adding options to edit or delete entries.
    Sorting papers by different fields like year or author.
    Building a graphical user interface (GUI) using tkinter.
    Exporting notes or summaries for selected topics.
