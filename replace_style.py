import os
import re

# 1. 指定 HTML 文件所在目录
folder_path = r"C:\Users\Administrator\Desktop\mcp-servers\mcp-server-marketplace\huaweicloud_services_server"  # 替换成你的文件夹路径

# 2. 新的 style 内容
new_style_content = """
    /* 基础设置 */
    body {
      font-family: "Segoe UI", "Microsoft YaHei", sans-serif;
      line-height: 1.6;
      color: #333;
      background-color: #f8f9fa;
      margin: 0;                /* 去掉默认外边距，避免页面出现空白边 */
      padding: 0;
    }

    /* 整体容器 */
    .container {
      background-color: #fff;
      border-radius: 8px;
      margin-top: 20px;     /* 距离顶部 20px */
      padding: 40px;
      display: flex;
      flex-direction: row;      /* 主轴水平 */
      gap: 40px;                /* 子项间距 */
      width: 100%;              /* 宽度自适应 */
      max-width: none;      /* 去掉最大宽度限制 */
    }


    /* 主内容区 */
    .main-content {
      flex: 1;                  /* 自动占据剩余空间 */
      margin: 0 20px;           /* 两侧保留 20px 间距 */
      min-width: 0;             /* 避免 flex 子项内容溢出 */
    }


    /* 标题设置 */
    h1, h2, h3, h4 {
        font-weight: 600;
        margin-top: 0;
        margin-bottom: 12px; /* 标题和正文之间 */
        text-align: left;
    }

    h1 {
        font-size: 24px;
        color:#191919;
    }

    h2 {
        font-size: 18px;
        color:#191919;
    }

    h3 {
        font-size: 16px;
        color: #191919;
    }

    /* 正文设置 */
    p, ul, ol {
        margin-bottom: 40px; /* 段落之间的间距：40px */
        font-size: 14px; /* 正文字体大小 */
        color: #191919; /* 正文颜色 */
        line-height: 1.7; / * 行高 */
        text-align: left; /* 段落文本居左 */
    }

    /* 列表设置 */
    ul, ol {
        padding-left: 25px;
    }

    li {
        margin-bottom: 10px;
        font-size: 14px;
    }

    /* 可跳转文字高亮 */
    a {
        color: #1476FF; /* 使用指定的蓝色 */
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
    }

    a:hover {
        text-decoration: underline;
    }

    /* 代码区块 */
    code {
        font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
        font-size: 14px;
        background-color: #f8f9fa;
        padding: 2px 6px;
        border-radius: 4px;
    }

    pre {
        background-color: #f8f9fa;
        border-radius: 4px;
        padding: 16px;
        overflow-x: auto;
        margin: 20px 0;
        font-size: 14px;
    }

  /* 工具栏外观 */
      .sidebar {
          flex: 0 0 450px; /* 固定宽度 */
          background: #fff; /* 背景色 */
          white-space: normal;  /* 允许换行 */
          word-break: break-word; /* 单词过长自动断行 */
          overflow-wrap: break-word; /* 支持更多浏览器 */
          border: 1px solid #eaeaea; /*边框 */
          border-radius: 12px; /* 圆角 */
          padding: 32px; /* 内部填充 */
          max-height: calc(100vh - 40px); / * 窗口高度减去工具栏外边距 */
          box-sizing: border-box; /* 宽度包含内边距 */
          overflow-y: auto; /* 滚动条 */
          text-align: left; /* 文本居左 */
          position: sticky;/* 粘性定位 */
          top: 20px; /* 顶部外边距 */
      }

    /* 主标题 */
    .sidebar h2 {
        font-size: 20px;
        font-weight: 600;
        color: #191919;
        margin: 0 0 24px 0;
    }

    /* 分组标题 */
    .sidebar h3 {
        font-size: 16px;
        font-weight: 600;
        color: #191919;
        margin: 24px 0 12px 0;
        padding-left: 8px;
    }

    /* 列表整体 */
    .sidebar ul {
        list-style: none;
        padding-left: 0;
        margin: 0;
    }

    /* 每个条目 */
.sidebar li {
    margin-bottom: 5px; /* 减小间距 */
    font-size: 14px;
    color: #595959;
    line-height: 1.5; /* 行高稍微紧凑 */
    padding: 6px 8px; /* 内边距小一点，避免过于稀疏 */
    border-radius: 6px;
    transition: all 0.2s ease;
    cursor: pointer;
}

/* hover 效果 */
.sidebar li:hover {
    background-color: #F7F8FA; /* 图片中的浅灰色 */
    color: #000000; /* 字体黑色 */
}

"""

# 3. 遍历文件夹
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 用正则替换 <style>...</style> 内容
        # 注意 re.DOTALL 让 . 匹配换行
        content_new = re.sub(
            r"<style.*?>.*?</style>",
            f"<style>{new_style_content}</style>",
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        # 写回文件
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content_new)

        print(f"已更新: {filename}")

print("批量替换完成！")
