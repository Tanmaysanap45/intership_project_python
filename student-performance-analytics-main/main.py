"""
Student Performance Analytics System
Python with AI - EWB Courses Project

This project demonstrates Python fundamentals, NumPy and Pandas
through a practical student performance analysis system.
"""

from pathlib import Path

import pandas as pd

from functions import (
    add_grades,
    add_pass_fail,
    calculate_total_and_average,
    display_class_statistics,
    display_result_breakdown,
    display_student_summary,
    display_subject_analysis,
    display_top_performers,
    get_class_statistics,
    get_subject_analysis,
    get_top_performers,
)


def print_header(title: str) -> None:
    """Print a consistent section heading."""
    print("\n" + "=" * 88)
    print(title.center(88))
    print("=" * 88)


def main() -> None:
    """Run the complete student performance analysis."""

    data_file = Path(__file__).with_name("students.csv")
    output_file = Path(__file__).with_name("student_analysis_output.csv")

    subjects = ["Python", "Statistics", "Database", "Data_Analysis"]

    # 1. Read the dataset using Pandas.
    df = pd.read_csv(data_file)

    print_header("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("Python + NumPy + Pandas")
    print(f"\nDataset file       : {data_file.name}")
    print(f"Student records    : {len(df)}")
    print(f"Columns            : {len(df.columns)}")
    print(f"Subjects analyzed  : {len(subjects)}")

    # Basic dataset check.
    print("\nDataset loaded successfully.")
    print("Missing values by column:")
    print(df.isnull().sum().to_string())

    # 2. Process marks using NumPy.
    df = calculate_total_and_average(df, subjects)

    # 3. Assign grades using conditions and a reusable function.
    df = add_grades(df)

    # 4. Determine Pass/Fail.
    df = add_pass_fail(df, subjects)

    # 5. Student-level output.
    print_header("1. STUDENT PERFORMANCE SUMMARY")
    display_student_summary(df)

    # 6. Class-level analysis.
    stats = get_class_statistics(df, subjects)
    print_header("2. CLASS PERFORMANCE STATISTICS")
    display_class_statistics(stats)

    # 7. Subject-level analysis.
    subject_analysis = get_subject_analysis(df, subjects)
    print_header("3. SUBJECT-WISE PERFORMANCE ANALYSIS")
    display_subject_analysis(subject_analysis)

    # 8. Top five students.
    top_performers = get_top_performers(df, top_n=5)
    print_header("4. TOP 5 PERFORMING STUDENTS")
    display_top_performers(top_performers)

    # 9. Grade and result counts.
    print_header("5. RESULT & GRADE BREAKDOWN")
    display_result_breakdown(df)

    # 10. Save processed data.
    df.to_csv(output_file, index=False)

    print_header("ANALYSIS COMPLETED")
    print(f"Processed data saved as: {output_file.name}")
    print("The project is ready for GitHub submission.")


if __name__ == "__main__":
    main()
