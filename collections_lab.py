def word_counts(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        cleaned_word = word.strip(".,!?;:")
        if cleaned_word:
            counts[cleaned_word] = counts.get(cleaned_word, 0) + 1
    return counts


def print_word_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    set1 = set(first)
    set2 = set(second)
    return sorted(list(set1 & set2))


def all_topics(first, second):
    set1 = set(first)
    set2 = set(second)
    return sorted(list(set1 | set2))


def totals_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        amount = record["amount"]
        totals[category] = totals.get(category, 0) + amount
    return totals


def titles_in_category(records, category):
    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles


def main():
    sample_text = input("Введите текст для подсчета частот слов: ")
    counts = word_counts(sample_text)
    print("Частоты слов:")
    print_word_counts(counts)

    records = [
        {"title": "Лекция по Python", "category": "лекции", "amount": 2},
        {"title": "Практика по базам данных", "category": "практика", "amount": 4},
        {"title": "Лабораторная по сетям", "category": "практика", "amount": 3},
    ]

    print("\nСводка часов по категориям:")
    totals = totals_by_category(records)
    for category in sorted(totals):
        print(f"{category} - {totals[category]} часов")

    search_category = input("\nВведите категорию для поиска занятий: ")
    found_titles = titles_in_category(records, search_category)
    print(f"Занятия в категории '{search_category}': {found_titles}")


if __name__ == "__main__":
    main()
