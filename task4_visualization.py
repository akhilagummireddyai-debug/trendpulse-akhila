import os
import pandas as pd
import matplotlib.pyplot as plt

# Load analysed CSV from Task 3
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

# Create outputs folder if it does not exist
os.makedirs("outputs", exist_ok=True)

# Shorten long titles for chart labels
def shorten_title(title, max_length=50):
    title = str(title)
    if len(title) > max_length:
        return title[:max_length] + "..."
    return title

# ----------------------------
# Chart 1: Top 10 Stories by Score
# ----------------------------
top_10 = df.sort_values(by="score", ascending=False).head(10).copy()
top_10["short_title"] = top_10["title"].apply(shorten_title)

plt.figure(figsize=(10, 6))
plt.barh(top_10["short_title"], top_10["score"])
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# ----------------------------
# Chart 2: Stories per Category
# ----------------------------
category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 6))
plt.bar(category_counts.index, category_counts.values, color=["red", "blue", "green", "orange", "purple"])
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# ----------------------------
# Chart 3: Score vs Comments
# ----------------------------
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure(figsize=(8, 6))
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# ----------------------------
# Bonus Dashboard
# ----------------------------
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("TrendPulse Dashboard", fontsize=16)

# Dashboard Chart 1
axes[0].barh(top_10["short_title"], top_10["score"])
axes[0].set_title("Top 10 Stories by Score")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Story Title")
axes[0].invert_yaxis()

# Dashboard Chart 2
axes[1].bar(category_counts.index, category_counts.values, color=["red", "blue", "green", "orange", "purple"])
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Number of Stories")
axes[1].tick_params(axis="x", rotation=20)

# Dashboard Chart 3
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Number of Comments")
axes[2].legend()

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("Charts saved successfully in outputs/ folder")
print("Saved files:")
print("outputs/chart1_top_stories.png")
print("outputs/chart2_categories.png")
print("outputs/chart3_scatter.png")
print("outputs/dashboard.png")