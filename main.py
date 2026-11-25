import os

LINE = "My cat walked across my keyboard during work and typed random letters to my boss and then went to sleep like nothing happened."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
