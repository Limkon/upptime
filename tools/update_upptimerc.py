import yaml

# 读取 urls 文件并解析其中的网址（一行一条）
def read_urls_file(filename="urls"):
    with open(filename, "r") as f:
        # 读取每一行，去除空行和首尾空白
        urls = [line.strip() for line in f if line.strip()]
    return urls

# 生成 sites 部分的格式
def generate_sites(urls):
    sites = []
    for url in urls:
        # 从 URL 中提取名称（例如 https://jxio.nyc.mn/ -> jxio.nyc.mn）
        name = url.replace("https://", "").replace("http://", "").rstrip("/")
        sites.append({"name": name, "url": url})
    return sites

# 更新 .upptimerc.yml 文件
def update_upptimerc(filename=".upptimerc.yml"):
    # 读取现有的 .upptimerc.yml 文件
    with open(filename, "r") as f:
        config = yaml.safe_load(f)

    # 获取新的 URL 列表并生成 sites
    urls = read_urls_file()
    new_sites = generate_sites(urls)

    # 更新 config 中的 sites 部分
    config["sites"] = new_sites

    # 将更新后的内容写回文件
    with open(filename, "w") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)

# 主程序入口
if __name__ == "__main__":
    print("开始更新 .upptimerc.yml 中的 sites 部分...")
    update_upptimerc()
    print("更新完成！")
