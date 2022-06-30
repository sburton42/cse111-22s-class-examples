def get_entries():
    entries = {
    "2022-06-30": ["run", 3.1, 27.5],
    "2022-06-29": ["run", 5.2, 48.1],
    "2022-06-26": ["bike", 28.5, 123.2],
    "2022-06-19": ["run", 4.7, 44.7],
    "2022-06-17": ["bike", 34.9, 140.5],
    "2022-06-15": ["bike", 18, 62.1],
    "2022-06-13": ["run", 3.5, 34.2],
    }
    return entries

def main():
    entries = get_entries()
    print(entries)

if __name__ == "__main__":
    main()

