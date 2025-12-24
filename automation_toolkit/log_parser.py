def parse_logs(log_file, keyword):
    """
    Return lines containing the keyword from a log file.
    """
    matches = []

    with open(log_file, "r") as f:
        for line in f:
            if keyword in line:
                matches.append(line.strip())

    return matches
