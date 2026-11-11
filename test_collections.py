from collections_lab import (
    all_topics,
    common_topics,
    totals_by_category,
    titles_in_category,
    word_counts,
)

assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}

topics1 = ["python", "sql", "python"]
topics2 = ["sql", "git"]
assert common_topics(topics1, topics2) == ["sql"]
assert all_topics(topics1, topics2) == ["git", "python", "sql"]
assert common_topics([], ["git"]) == []
assert all_topics([], ["git"]) == ["git"]

records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
records_copy = [record.copy() for record in records]

assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert totals_by_category([]) == {}

assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []

assert records == records_copy

print("Все проверки для работы 8 успешно пройдены")
