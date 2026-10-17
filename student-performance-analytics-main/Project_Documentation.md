# Project Documentation
## Student Performance Analytics System

### 1. Project Title

**Student Performance Analytics System**

**Student:** Tanmay Santosh Sanap 
**Course:** Python with AI  
**Technology:** Python, NumPy, Pandas

---

### 2. Objective

The objective of the project is to build a Python-based system that reads student academic data and analyzes student performance.

The system calculates total and average marks, assigns grades, identifies pass/fail students, performs subject-wise analysis and identifies top-performing students.

---

### 3. Technologies Used

- **Python:** Main programming language
- **Pandas:** Used to read the CSV file, create and process the DataFrame, filter/sort records and generate analysis
- **NumPy:** Used for numerical calculations such as sum, mean, minimum and maximum
- **CSV:** Used as the student dataset format

---

### 4. Dataset Description

The project uses a CSV dataset containing **20 student records**.

Important fields include:

- Student ID
- Name
- Department
- Python marks
- Statistics marks
- Database marks
- Data Analysis marks
- Attendance percentage

Each subject is scored out of 100.

---

### 5. Implementation

#### Step 1 – Load the Dataset

The program reads `students.csv` using Pandas `read_csv()` and stores the records in a Pandas DataFrame.

#### Step 2 – Calculate Total and Average

The four subject marks are converted into a NumPy array.

NumPy functions are used to calculate:

- Total marks using `np.sum()`
- Average marks using `np.mean()`

The results are added to the DataFrame as new columns.

#### Step 3 – Assign Grades

A reusable `assign_grade()` function checks the student's average marks using conditional statements and returns the corresponding grade.

#### Step 4 – Determine Pass/Fail

A reusable function checks three conditions:

- Average marks >= 40
- Every subject mark >= 35
- Attendance >= 75%

The student receives `Pass` only when all three conditions are satisfied.

#### Step 5 – Class Performance Analysis

The project calculates:

- Number of students
- Number of passed students
- Number of failed students
- Overall class average
- Highest student average
- Lowest student average
- Average attendance

#### Step 6 – Subject-wise Analysis

A loop processes each subject and calculates its:

- Average
- Highest marks
- Lowest marks

The subject with the highest average is identified as the best-performing subject.

#### Step 7 – Top Performers

The DataFrame is sorted by average marks in descending order, and the top five students are displayed.

#### Step 8 – Result and Grade Breakdown

The project counts the number of students in each result category and each grade category.

#### Step 9 – Save Processed Data

After analysis, the completed DataFrame is saved as `student_analysis_output.csv`.

---

### 6. Key Features

1. CSV dataset loading
2. Pandas DataFrame processing
3. NumPy-based numerical calculations
4. Reusable calculation functions
5. Loops and conditions
6. Automatic total and average calculation
7. Grade assignment
8. Pass/fail classification
9. Class performance statistics
10. Subject-wise analysis
11. Top-five performer identification
12. Attendance analysis
13. Export of processed results

---

### 7. Output / Screenshots

Screenshots can be added here after running the project.

Suggested screenshots:

- Dataset loading and project start
- Student Performance Summary
- Class Performance Statistics
- Subject-wise Performance Analysis
- Top Performing Students
- Result & Grade Breakdown

---

### 8. Final Outcome

The final system successfully converts raw student records into a structured performance analysis.

It provides student-level results as well as class-level and subject-level insights. The output is displayed in a readable format so that the analysis can be understood without inspecting the source code.

---

### 9. Challenges & Learning

#### Challenges

- Organizing student marks into a structured dataset
- Applying multiple conditions for pass/fail classification
- Separating reusable processing logic into functions
- Combining NumPy calculations with Pandas DataFrame operations

#### Learning

Through this project, I practiced:

- Reading CSV files using Pandas
- Working with DataFrames
- Performing numerical calculations using NumPy
- Creating reusable Python functions
- Using loops and conditional statements
- Sorting and filtering data
- Presenting analytical results clearly

---

### 10. GitHub Repository

**Repository Link:**  
_To be added after the GitHub repository is created._

**Google Form Submission:**  
The final GitHub repository URL will be submitted through the EWB Courses Google Form as required.
