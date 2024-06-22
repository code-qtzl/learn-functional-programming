def get_median_font_size(font_sizes):
    length = len(font_sizes)

    if length == 0:
        return None

    font_sizes_sorted = sorted(font_sizes)
    middle_index = length // 2
    
    if length % 2 == 0:
        middle_index1 = middle_index - 1
        middle_index2 = middle_index
        return min(font_sizes_sorted[middle_index1], font_sizes_sorted[middle_index2])
    else:
        return font_sizes_sorted[middle_index]