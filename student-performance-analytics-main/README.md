# Student Performance Analytics System

A Python-based data-analysis project created for the **EWB Courses – Python with AI** project assignment.

## Project Overview

The Student Performance Analytics System reads student academic data from a CSV file, processes the data with Pandas and NumPy, and produces useful performance insights.

The project covers Python fundamentals such as **variables, data types, loops, functions, conditions and data handling**, along with NumPy and Pandas operations.

## Objectives

The system is designed to:

1. Calculate total and average marks for every student.
2. Assign grades using a clearly defined grading rule.
3. Identify Pass/Fail students.
4. Find highest, lowest and overall class performance.
5. Perform subject-wise analysis.
6. Identify the top-performing students.
7. Present results in a readable final report.

## Technologies

- Python
- NumPy
- Pandas
- CSV

## Dataset

The project contains **20 student records** with the following fields:

| Field | Description |
|---|---|
| Student_ID | Unique student identifier |
| Name | Student name |
| Department | Academic department |
| Python | Marks out of 100 |
| Statistics | Marks out of 100 |
| Database | Marks out of 100 |
| Data_Analysis | Marks out of 100 |
| Attendance | Attendance percentage |

## Grading Rule

| Average | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

## Pass/Fail Rule

A student is marked **Pass** when all three conditions are satisfied:

- Average marks are at least 40.
- Marks in every subject are at least 35.
- Attendance is at least 75%.

Otherwise, the result is **Fail**.

## Project Structure

```text
student-performance-analytics/
│
├── main.py
├── functions.py
├── students.csv
├── README.md
├── Project_Documentation.md
├── GITHUB_SUBMISSION_GUIDE.md
├── requirements.txt
├── .gitignore
└── student_analysis_output.csv
```

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

## Main Analysis Sections

The program displays:

**1. Student Performance Summary**  
Shows each student's total marks, average, grade, attendance and result.

**2. Class Performance Statistics**  
Shows class average, highest/lowest student average, pass/fail count and attendance.

**3. Subject-wise Performance Analysis**  
Shows subject averages and highest/lowest marks, then identifies the best-performing subject.

**4. Top 5 Performing Students**  
Ranks the five students with the highest average marks.

**5. Result & Grade Breakdown**  
Shows Pass/Fail counts and the number of students in each grade.

## Output

After execution, the processed DataFrame is also saved as:

`student_analysis_output.csv`

## Concepts Demonstrated

- Variables and data types
- Conditional statements
- Loops
- Functions
- NumPy arrays and numerical calculations
- Pandas DataFrames
- CSV data loading
- Sorting and filtering
- Basic data analysis

## Learning Outcome

This project demonstrates how Python can be used to convert raw student records into structured and understandable analytical results.

## Author

**Aryan Bendre**  
B.Sc. Data Science

## Assignment Note

The project intentionally stays within the assignment scope and does not use advanced machine-learning models.
