def count_nested_levels(nested_documents, target_document_id, level=1):
    if target_document_id in nested_documents:
            return level

        # Recursively check in nested levels
    for key, value in nested_documents.items():
        if isinstance(value, dict):
            result = count_nested_levels(value, target_document_id, level + 1)
            if result != -1:
                return result

    # Return -1 if the target document is not found in the nested structure
    return -1