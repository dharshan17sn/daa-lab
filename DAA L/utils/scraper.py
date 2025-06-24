import os
import wikipedia

def get_best_match(topic):
    search_results = wikipedia.search(topic)
    return search_results[0] if search_results else None

def scrape_articles(topics_input=None):
    # Clear previous scraped files
    for old_file in os.listdir("scraped_data"):
        os.remove(os.path.join("scraped_data", old_file))

    if isinstance(topics_input, list):
        topics = topics_input
    elif isinstance(topics_input, str):
        topics = topics_input.split("\n")
    else:
        topics = []

    scraped_files = []

    for topic in topics:
        topic = topic.strip()
        if not topic:
            continue

        best_match = get_best_match(topic)
        if not best_match:
            print(f"[X] No match found for: {topic}")
            continue

        try:
            print(f"[+] Scraping: {best_match}")
            content = wikipedia.page(best_match).content
        except Exception as e:
            print(f"[!] Failed to scrape '{best_match}': {e}")
            continue

        filename = best_match.replace(" ", "_") + ".txt"
        path = os.path.join("scraped_data", filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        scraped_files.append(filename)

    return scraped_files
