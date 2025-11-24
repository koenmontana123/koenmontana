import random
import re
from pathlib import Path

STATUSES = [
    "🐛 Debugging bugs and brewing coffee — replies may arrive after the next successful compile",
    "🚀 Exploring open‑source galaxies, signal delay expected across light‑years of code",
    "🧑‍💻 In a merge conflict with reality… please wait while I rebase my thoughts",
    "🐢 Slow but steady, like a turtle learning recursion — commits may take the scenic route",
    "🎮 AFK: battling bosses in code and games, will return with loot (and commits)",
    "☕ Coffee in hand, curiosity in mind — expect responses at espresso speed",
]

README = Path("README.md")

def update_readme():
    status = random.choice(STATUSES)
    text = README.read_text(encoding="utf-8")

    # Replace or insert a Status line marked by anchors
    start_anchor = "<!-- STATUS:START -->"
    end_anchor = "<!-- STATUS:END -->"
    block = f"{start_anchor}\n> {status}\n{end_anchor}"

    pattern = re.compile(
        rf"{re.escape(start_anchor)}.*?{re.escape(end_anchor)}",
        flags=re.DOTALL
    )

    if pattern.search(text):
        text = pattern.sub(block, text)
    else:
        # Insert at top if anchors not present
        text = block + "\n\n" + text

    README.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    update_readme()
