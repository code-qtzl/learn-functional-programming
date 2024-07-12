def list_files(current_filetree, current_path=""):
    file_paths = []

    for node in current_filetree:
        if current_path:
            new_path = f"/{current_path}/{node}"
        else:
            new_path = node
            
        if current_filetree[node] is None:
            file_paths.append(new_path)
        else:
            file_paths.extend(list_files(current_filetree[node], new_path))
    
    
    return file_paths