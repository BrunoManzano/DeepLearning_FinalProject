

# This file is just to compute the real accuracy or similarity between the CNN predictions and the ground truth labels of the names dataset (9).


import numpy as np

def levenshtein_distance(str1, str2):
    """Compute the Levenshtein distance between two strings."""
    if len(str1) < len(str2):
        return levenshtein_distance(str2, str1)

    # len(str1) >= len(str2)
    if len(str2) == 0:
        return len(str1)

    previous_row = range(len(str2) + 1)
    for i, c1 in enumerate(str1):
        current_row = [i + 1]
        for j, c2 in enumerate(str2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def compare_strings_from_file(file_path):
    total_similarity = 0
    pair_count = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('\t')  # Split using the tab character
            if len(parts) != 2:
                print(f"Skipping invalid line: {line.strip()}")
                continue
            str1, str2 = parts
            lev_distance = levenshtein_distance(str1, str2)
            max_len = max(len(str1), len(str2))
            similarity = (1 - lev_distance / max_len) if max_len > 0 else 1
            total_similarity += similarity
            pair_count += 1

    global_similarity = (total_similarity / pair_count) * 100 if pair_count > 0 else 0

    return {
        "Total Pairs": pair_count,
        "Global Similarity": global_similarity
    }

# Example usage
file_path = 'cnn_predictions_2.txt'
result = compare_strings_from_file(file_path)
print(result)
