"""
Reusable functions for the Student Performance Analytics System.
"""

import numpy as np
import pandas as pd


def calculate_total_and_average(df: pd.DataFrame, subjects: list[str]) -> pd.DataFrame:
    """Calculate total and average marks for each student using NumPy."""
    result = df.copy()
    marks_array = result[subjects].to_numpy(dtype=float)

    result["Total_Marks"] = np.sum(marks_array, axis=1)
    result["Average_Marks"] = np.round(np.mean(marks_array, axis=1), 2)

    return result


def assign_grade(average: float) -> str:
    """Assign a grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def add_grades(df: pd.DataFrame) -> pd.DataFrame:
    """Add a Grade column using a loop and the reusable grade function."""
    result = df.copy()
    grades = []

    for average in result["Average_Marks"]:
        grades.append(assign_grade(average))

    result["Grade"] = grades
    return result


def determine_result(row: pd.Series, subjects: list[str]) -> str:
    """
    Pass rule:
    - Average >= 40
    - Every subject mark >= 35
    - Attendance >= 75%
    """
    average_ok = row["Average_Marks"] >= 40
    subjects_ok = all(row[subject] >= 35 for subject in subjects)
    attendance_ok = row["Attendance"] >= 75

    return "Pass" if average_ok and subjects_ok and attendance_ok else "Fail"


def add_pass_fail(df: pd.DataFrame, subjects: list[str]) -> pd.DataFrame:
    """Add the Pass/Fail result using row-wise iteration."""
    result = df.copy()
    results = []

    for _, row in result.iterrows():
        results.append(determine_result(row, subjects))

    result["Result"] = results
    return result


def get_class_statistics(df: pd.DataFrame, subjects: list[str]) -> dict:
    """Calculate class-level performance statistics with NumPy."""
    all_marks = df[subjects].to_numpy(dtype=float)

    return {
        "highest_average": float(df["Average_Marks"].max()),
        "lowest_average": float(df["Average_Marks"].min()),
        "class_average": float(np.mean(all_marks)),
        "total_students": int(len(df)),
        "passed_students": int((df["Result"] == "Pass").sum()),
        "failed_students": int((df["Result"] == "Fail").sum()),
        "average_attendance": float(np.mean(df["Attendance"])),
    }


def get_subject_analysis(df: pd.DataFrame, subjects: list[str]) -> pd.DataFrame:
    """Create subject-wise average, highest and lowest marks."""
    rows = []

    for subject in subjects:
        marks = df[subject].to_numpy(dtype=float)
        rows.append(
            {
                "Subject": subject,
                "Average": round(float(np.mean(marks)), 2),
                "Highest": round(float(np.max(marks)), 2),
                "Lowest": round(float(np.min(marks)), 2),
            }
        )

    return pd.DataFrame(rows)


def get_top_performers(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    """Return the top-performing students by average marks."""
    columns = [
        "Student_ID",
        "Name",
        "Department",
        "Average_Marks",
        "Grade",
        "Result",
    ]

    return (
        df.sort_values("Average_Marks", ascending=False)
        .head(top_n)[columns]
        .reset_index(drop=True)
    )


def display_student_summary(df: pd.DataFrame) -> None:
    """Display student-level performance."""
    columns = [
        "Student_ID",
        "Name",
        "Department",
        "Total_Marks",
        "Average_Marks",
        "Grade",
        "Attendance",
        "Result",
    ]
    print(df[columns].to_string(index=False))


def display_class_statistics(stats: dict) -> None:
    """Display class-level metrics."""
    metrics = [
        ("Total Students", stats["total_students"]),
        ("Passed Students", stats["passed_students"]),
        ("Failed Students", stats["failed_students"]),
        ("Class Average Marks", f"{stats['class_average']:.2f}"),
        ("Highest Student Average", f"{stats['highest_average']:.2f}"),
        ("Lowest Student Average", f"{stats['lowest_average']:.2f}"),
        ("Average Attendance", f"{stats['average_attendance']:.2f}%"),
    ]

    for label, value in metrics:
        print(f"{label:<26}: {value}")


def display_subject_analysis(subject_df: pd.DataFrame) -> None:
    """Display subject-wise analysis and identify the best subject."""
    print(subject_df.to_string(index=False))

    best_row = subject_df.loc[subject_df["Average"].idxmax()]
    print(
        f"\nBest-performing subject : {best_row['Subject']}"
        f" ({best_row['Average']:.2f} average)"
    )


def display_top_performers(top_df: pd.DataFrame) -> None:
    """Display the top-performing students."""
    for rank, (_, row) in enumerate(top_df.iterrows(), start=1):
        print(
            f"{rank}. {row['Name']:<18} "
            f"| Average: {row['Average_Marks']:.2f} "
            f"| Grade: {row['Grade']} "
            f"| Result: {row['Result']}"
        )


def display_result_breakdown(df: pd.DataFrame) -> None:
    """Display Pass/Fail counts and grade counts."""
    result_counts = df["Result"].value_counts()
    grade_counts = df["Grade"].value_counts()

    print("Result:")
    for result in ["Pass", "Fail"]:
        print(f"  {result:<6}: {int(result_counts.get(result, 0))}")

    print("\nGrades:")
    for grade in ["A+", "A", "B", "C", "D", "F"]:
        print(f"  {grade:<6}: {int(grade_counts.get(grade, 0))}")
