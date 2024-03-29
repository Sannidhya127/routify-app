def vertical_split(code_segment1, code_segment2):
    lines1 = code_segment1.split('\n')
    lines2 = code_segment2.split('\n')
    
    max_lines = max(len(lines1), len(lines2))
    
    for i in range(max_lines):
        line1 = lines1[i] if i < len(lines1) else ''
        line2 = lines2[i] if i < len(lines2) else ''
        print(f"{line1.ljust(40)} | {line2}")

# Example code segments
code_segment1 = """
print("This is code segment 1.")
for i in range(5):
    print(i)
"""

code_segment2 = """
print("This is code segment 2.")
for i in range(3):
    print(i * 2)
"""

vertical_split(code_segment1, code_segment2)
