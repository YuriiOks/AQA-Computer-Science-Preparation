import os

# List of week names with their topics
weeks = [
    "01 - Introduction to Computational Thinking",
    "02 - Representing Algorithms",
    "03 - High-level vs Low-level Languages",
    "04 - Searching Algorithms",
    "05 - Sorting Algorithms",
    "06 - Data Types and Data Structures in Python",
    "07 - Variables, Constants, and Operators",
    "08 - Random Number Generation in Python",
    "09 - Control Structures in Python (Part 1)",
    "10 - Control Structures in Python (Part 2)",
    "11 - Structured Programming and Subroutines (Part 1)",
    "12 - Structured Programming and Subroutines (Part 2)",
    "13 - String Handling in Python",
    "14 - Advanced Data Structures in Python",
    "15 - Testing and Debugging in Python",
    "16 - Robust and Secure Programming",
    "17 - Fundamentals of Data Representation (Part 1)",
    "18 - Fundamentals of Data Representation (Part 2)",
    "19 - Data Representation of Images and Sound",
    "20 - Data Compression Techniques",
    "21 - Relational Databases and SQL Basics (Part 1)",
    "22 - Relational Databases and SQL Basics (Part 2)",
    "23 - Structured Query Language (SQL)",
    "24 - Exam Practice – Algorithms and Pseudocode",
    "25 - Final Exam Preparation and Q&A"
]

# Subfolders to be created inside each week's folder
subfolders = ['Notes', 'Code Examples', 'Exercises', 'Presentations']

# Base directory where all the folders will be created
base_directory = "AQA-CompSci-Paper1-Prep"

# README content for each week's folder
week_readme_content = """
# Week {week_name}

This week focuses on **{week_topic}**. Below are the materials for this week:

- **Notes**: Key concepts and theory for this topic.
- **Code Examples**: Sample Python code demonstrating key ideas.
- **Exercises**: Problems and coding challenges for practice.
- **Presentations**: Slides and visual aids used in the lessons.

Please refer to the appropriate sections to explore this week's content.
"""

# README content for subfolders (optional)
subfolder_readme_content = """
# {subfolder} for Week {week_number}

This folder contains the **{subfolder}** related to **Week {week_number}**.
"""

# Create the base directory if it doesn't exist
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

# Generate folders for each week
for week_index, week in enumerate(weeks, start=1):
    week_directory = os.path.join(base_directory, week)
    
    # Create the week folder if it doesn't exist
    if not os.path.exists(week_directory):
        os.makedirs(week_directory)

    # Create a README.md for the week folder
    readme_path = os.path.join(week_directory, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(
            week_readme_content.format(
                week_number=f"{week_index:02}",
                week_name=week,
                week_topic=week.split(' - ')[1]
            )
        )
    
    # Create subfolders inside each week folder
    for subfolder in subfolders:
        subfolder_path = os.path.join(week_directory, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        
        # Create a README.md for each subfolder (optional)
        subfolder_readme_path = os.path.join(subfolder_path, "README.md")
        with open(subfolder_readme_path, "w") as subfolder_readme_file:
            subfolder_readme_file.write(
                subfolder_readme_content.format(
                    subfolder=subfolder,
                    week_number=f"{week_index:02}"
                )
            )

print("Folders and README.md files have been created successfully!")
