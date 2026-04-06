import pandas as pd
import numpy as np

# Load cleaned CSV file from Task 2
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

# Print basic info
print(f"Loaded data: {df.shape}")

# Show first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Calculate averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score   : {avg_score}")
print(f"Average comments: {avg_comments}")

# --- NumPy Analysis ---
print("\n--- NumPy Stats ---")

scores = df["score"].to_numpy()

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

print(f"Mean score   : {mean_score}")
print(f"Median score : {median_score}")
print(f"Std deviation: {std_score}")

print(f"Max score    : {np.max(scores)}")
print(f"Min score    : {np.min(scores)}")

# Category with most stories
category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# Story with most comments
max_comments_row = df.loc[df["num_comments"].idxmax()]

print(f"\nMost commented story: \"{max_comments_row['title']}\" — {max_comments_row['num_comments']} comments")

# Add new columns

# Engagement = comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular = True if score > average score
df["is_popular"] = df["score"] > avg_score

# Save updated file
output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")