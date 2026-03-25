# 读取输入文件
input_file = "week1_posts.txt"
output_file = "week1_long_posts.txt"

# 打开输入文件并读取所有行
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 去掉每行末尾的换行符，并过滤空行
posts = [line.strip() for line in lines if line.strip()]

# 统计总行数
total_count = len(posts)
print(f"总共有 {total_count} 条文本")

# 筛选长度大于 20 个字的文本
long_posts = [post for post in posts if len(post) > 20]

print(f"长度大于 20 个字的文本有 {len(long_posts)} 条")

# 把筛选结果写入输出文件
with open(output_file, "w", encoding="utf-8") as f:
    for post in long_posts:
        f.write(post + "\n")

print(f"筛选结果已保存到 {output_file}")
