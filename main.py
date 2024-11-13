import csv
import os

# File to store research papers
FILE_NAME = "research_papers.csv"

# Initialize CSV file if it does not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "Year", "Topic", "Link", "Notes"])


def add_paper():
    print("\n--- Add a New Research Paper ---")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    year = input("Enter Year: ")
    topic = input("Enter Topic: ")
    link = input("Enter Link/DOI: ")
    notes = input("Enter Notes: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year, topic, link, notes])

    print("\nPaper added successfully!")


def view_papers():
    print("\n--- All Research Papers ---")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Title: {row[0]}")
            print(f"Author: {row[1]}")
            print(f"Year: {row[2]}")
            print(f"Topic: {row[3]}")
            print(f"Link: {row[4]}")
            print(f"Notes: {row[5]}")
            print("--------------------------------------------------")


def search_papers():
    print("\n--- Search Papers by Topic ---")
    topic = input("Enter Topic to Search: ").lower()
    found = False

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if topic in row[3].lower():
                print(f"\nTitle: {row[0]}")
                print(f"Author: {row[1]}")
                print(f"Year: {row[2]}")
                print(f"Topic: {row[3]}")
                print(f"Link: {row[4]}")
                print(f"Notes: {row[5]}")
                found = True
        if not found:
            print("No papers found with that topic.")


def main():
    while True:
        print("\nResearch Paper Organizer")
        print("1. Add a New Paper")
        print("2. View All Papers")
        print("3. Search Papers by Topic")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_paper()
        elif choice == "2":
            view_papers()
        elif choice == "3":
            search_papers()

        elif choice == "4":
            print("Exiting the organizer. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Run the program
if __name__ == "__main__":
    main()
