import os

LINE = "My cat sat on my keyboard, sent 'asdkfj' to my boss, and then napped like she'd done her job."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
