




def split_text_into_parts(text, num_parts):
    total_length = len(text)
    part_size = total_length // num_parts
    extra_chars = total_length % num_parts

    parts = []
    start = 0

    for _ in range(num_parts):
        end = start + part_size
        if extra_chars > 0:
            end += 1
            extra_chars -= 1

        parts.append(text[start:end])
        start = end

    return parts

# 读取输入文件
with open(r"C:\Users\zhijiel\Downloads\NASA-RZSM\NASA-RZSM.txt", "r", encoding="utf-8") as file:
    content = file.read()

num_parts = 8
split_parts = split_text_into_parts(content, num_parts)

# 将分割后的内容写入输出文件
for i, part in enumerate(split_parts):
    with open(f"output_part_{i+1}.txt", "w", encoding="utf-8") as file:
        file.write(part)
        file.write("\n")
