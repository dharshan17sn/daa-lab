# --- FILE: utils/highlighter.py ---

from difflib import SequenceMatcher

def highlight_matches(user_text, source_text):
    matcher = SequenceMatcher(None, user_text, source_text)
    user_html = ""
    source_html = ""

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        u_chunk = user_text[i1:i2]
        s_chunk = source_text[j1:j2]

        if tag == 'equal':
            user_html += f"<span>{u_chunk}</span>"
            source_html += f"<span>{s_chunk}</span>"
        else:
            user_html += f"<mark>{u_chunk}</mark>"
            source_html += f"<mark>{s_chunk}</mark>"

    return user_html, source_html
