import re
def solution(files):
    splitted_files = []
    for file in files:
        match_result = re.match(r"^([A-Za-z][A-Za-z.\-\s]*)(\d+)(.*)$", file)
        
        head = match_result[1]
        number = match_result[2]
        tail = match_result[3]
        
        splitted_files.append([head, number, tail])
        
    answer = sorted(
        splitted_files,
        key=lambda x: (x[0].upper(), int(x[1]))
    )
    
    return ["".join(row) for row in answer]