import os
import glob
import pandas as pd
json_files = glob.glob("data/trends_*.json")
if not json_files:
    print("No JSON file found in data folder.")
    exit()
latest_file = max(json_files, key = os.path.getctime)
df = pd.read_json(latest_file)
print(f"Loaded {len(df)} stories from {latest_file}")
print(f"After removing duplicates: {len(df)}")
print(f"After removing nulls: {len(df)}")
print(f"After removing low scores: {len(df)}")
# Save cleaned data to CSV
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved {len(df)} rows to {output_file}")

# Print category summary
print("\nStories per category:")
print(df["category"].value_counts())