import requests
import json
import os
import time
import urllib3
from datetime import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {"User-Agent": "TrendPulse/1.0"}

category_keywords = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

all_stories = []
collected_ids = set()
collected_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

session = requests.Session()
session.headers.update(headers)

try:
    response = session.get(top_url, timeout=5, verify=False)
    response.raise_for_status()
    top_story_ids = response.json()[:500]
except Exception as e:
    print(f"Failed to fetch top stories: {e}")
    top_story_ids = []

for category, keywords in category_keywords.items():
    print(f"Collecting: {category}")
    count = 0

    for story_id in top_story_ids:
        if count >= 25:
            break

        if story_id in collected_ids:
            continue

        item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

        try:
            item_response = session.get(item_url, timeout=5, verify=False)
            item_response.raise_for_status()
            story = item_response.json()
        except Exception as e:
            print(f"Failed to fetch story {story_id}: {e}")
            continue

        if not story:
            continue

        title = story.get("title", "")
        title_lower = title.lower()

        if any(keyword in title_lower for keyword in keywords):
            story_data = {
                "post_id": story.get("id"),
                "title": title,
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "unknown"),
                "collected_at": collected_time
            }
            all_stories.append(story_data)
            collected_ids.add(story_id)
            count += 1
            print(f"{category}: {count}")

    time.sleep(2)

os.makedirs("data", exist_ok=True)
filename = datetime.now().strftime("data/trends_%Y%m%d.json")

with open(filename, "w", encoding="utf-8") as file:
    json.dump(all_stories, file, indent=4)

print(f"Collected {len(all_stories)} stories. Saved to {filename}")