import os
import wikipedia

def get_best_match(topic):
    """
    Attempts to find the best Wikipedia page match for the given topic.
    Returns the title of the best match if available, else None.
    """
    try:
        search_results = wikipedia.search(topic)
        for result in search_results:
            try:
                page = wikipedia.page(result, auto_suggest=False)
                if not page.title.lower().startswith("list of"):  # Skip list-based pages
                    return page.title
            except wikipedia.DisambiguationError as e:
                if e.options:
                    return e.options[0]  # fallback to first disambiguation option
            except Exception:
                continue
        return None
    except Exception as e:
        print(f"[!] Error during search for '{topic}': {e}")
        return None

def scrape_articles(topics_input=None):
    # Ensure the directory exists and clean it
    os.makedirs("scraped_data", exist_ok=True)
    for old_file in os.listdir("scraped_data"):
        try:
            os.remove(os.path.join("scraped_data", old_file))
        except Exception as e:
            print(f"[!] Couldn't remove file {old_file}: {e}")

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

        print(f"[*] Searching: {topic}")
        best_match = get_best_match(topic)

        if not best_match:
            print(f"[X] No match found for: {topic}")
            continue

        try:
            print(f"[+] Scraping: {best_match}")
            content = wikipedia.page(best_match, auto_suggest=False).content
        except Exception as e:
            print(f"[!] Failed to fetch page '{best_match}': {e}")
            continue

        filename = best_match.replace(" ", "_") + ".txt"
        file_path = os.path.join("scraped_data", filename)
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            scraped_files.append(filename)
        except Exception as e:
            print(f"[!] Error writing file '{filename}': {e}")

    return scraped_files
