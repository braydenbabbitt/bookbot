def count_words(text):
    return len(text.split())


def count_all_characters(text):
    result = {}
    for char in text:
        previous_count = result.get(char.lower(), 0)
        result[char.lower()] = previous_count + 1
    return result


def sort_character_counts(character_counts):
    def sort_on(item):
        return item["num"]

    result = []
    for entry in character_counts.items():
        result.append({"char": entry[0], "num": entry[1]})

    result.sort(reverse=True, key=sort_on)
    return result
