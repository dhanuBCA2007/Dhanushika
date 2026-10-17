# ==========================================
# ComicCraft - AI Comic Story Creator
# No API Key | No External Libraries
# ==========================================

import random

def create_comic():
    print("\n" + "=" * 45)
    print("       COMICCRAFT STORY CREATOR")
    print("=" * 45)

    title = input("Enter comic title: ").strip()
    hero = input("Enter hero name: ").strip()
    villain = input("Enter villain name: ").strip()
    idea = input("Enter story idea: ").strip()

    if not title or not hero or not villain or not idea:
        print("Please enter all details.")
        return

    print("\nSelect Genre:")
    print("1. Superhero")
    print("2. Fantasy")
    print("3. Adventure")
    print("4. Comedy")
    print("5. Science Fiction")

    genres = {
        "1": "Superhero",
        "2": "Fantasy",
        "3": "Adventure",
        "4": "Comedy",
        "5": "Science Fiction"
    }

    choice = input("Enter choice (1-5): ").strip()
    genre = genres.get(choice, "Adventure")

    panels = [
        (
            "The Beginning",
            f"{hero} discovers a mysterious problem. "
            f"The city is in danger. Story idea: {idea}",
            f"{hero}: Something strange is happening!"
        ),
        (
            "The Villain Appears",
            f"{villain} appears and challenges {hero}.",
            f"{villain}: Nobody can stop me!"
        ),
        (
            "The Big Challenge",
            f"{hero} faces a difficult challenge "
            f"and prepares a clever plan.",
            f"{hero}: I won't give up!"
        ),
        (
            "The Final Battle",
            f"{hero} confronts {villain} in an exciting battle.",
            random.choice([
                f"{hero}: This ends now!",
                f"{hero}: You cannot defeat courage!",
                f"{hero}: It's time to save the day!"
            ])
        ),
        (
            "The Ending",
            f"{hero} overcomes the challenge and brings hope "
            f"to everyone. The adventure is complete.",
            f"{hero}: Another adventure awaits!"
        )
    ]

    random.shuffle(panels[2:4]) if False else None

    story = []
    story.append(f"COMIC TITLE: {title}")
    story.append(f"GENRE: {genre}")
    story.append(f"HERO: {hero}")
    story.append(f"VILLAIN: {villain}")
    story.append("=" * 45)

    for number, (name, scene, dialogue) in enumerate(panels, 1):
        panel = (
            f"\nPANEL {number}: {name}\n"
            f"Scene: {scene}\n"
            f"Speech Bubble: {dialogue}\n"
            + "-" * 35
        )
        story.append(panel)

    result = "\n".join(story)

    print("\n" + result)

    try:
        with open("comiccraft_story.txt", "w",
                  encoding="utf-8") as file:
            file.write(result)

        print("\nComic saved to comiccraft_story.txt")
    except OSError:
        print("\nCould not save the file in this location.")


def main():
    while True:
        print("\n========== COMICCRAFT MENU ==========")
        print("1. Create Comic Story")
        print("2. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_comic()
        elif choice == "2":
            print("Thank you for using ComicCraft!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
