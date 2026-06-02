import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PERFORMANCE ANALYTICS FOR STUDENT DATA

try:

    # Step 1: Load student performance data from CSV file
    df = pd.read_csv("student_performance.csv")

    print("\n--- RAW DATA ---")
    print(df.head())

    # Step 2: Statistical summary using Pandas
    print("\n--- STATISTICAL SUMMARY ---")
    print(df.describe())

    # Step 3: Convert to NumPy array for numerical operations
    scores = df[["Math", "Science", "English"]].to_numpy()

    # Step 4: Compute Mean, Median, and Standard Deviation
    mean_scores = np.mean(scores, axis=0)
    median_scores = np.median(scores, axis=0)
    std_dev_scores = np.std(scores, axis=0)

    print("\n--- NUMPY ANALYSIS ---")

    print(f"Mean Scores (Math, Science, English): {mean_scores}")

    print(f"Median Scores (Math, Science, English): {median_scores}")

    print(f"Standard Deviation (Math, Science, English): {std_dev_scores}")

    # Step 5: Find top performer in each subject
    top_math = df.loc[df["Math"].idxmax(), "Name"]

    top_science = df.loc[df["Science"].idxmax(), "Name"]

    top_english = df.loc[df["English"].idxmax(), "Name"]

    print("\n--- TOP PERFORMERS ---")

    print(f"Math Topper: {top_math}")

    print(f"Science Topper: {top_science}")

    print(f"English Topper: {top_english}")

    # Step 6: Visualization using Matplotlib
    subjects = ["Math", "Science", "English"]

    average_scores = [
        mean_scores[0],
        mean_scores[1],
        mean_scores[2]
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(subjects, average_scores)

    plt.title("Average Scores by Subject")

    plt.xlabel("Subjects")

    plt.ylabel("Average Marks")

    plt.grid(True)

    plt.show()

except FileNotFoundError:

    print("Error: student_performance.csv file not found.")

except Exception as e:

    print(f"Unexpected Error: {e}")