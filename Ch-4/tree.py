def list_files(current_filetree, current_path=""):
    file_paths = []

    for node, subtree in current_filetree.items():
        new_path = f"{current_path}/{node}" if current_path else f"/{node}"
            
        if subtree is None:
            file_paths.append(new_path)
        else:
            file_paths.extend(list_files(subtree, new_path))
    
    return file_paths