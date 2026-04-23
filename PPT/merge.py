import os
import sys

try:
    import pyperclip
except ImportError:
    print("错误: 找不到 pyperclip 库。")
    print("请先在终端运行: pip install pyperclip")
    sys.exit(1)

# ==========================================
# 自动排除的目录和文件后缀大全
# ==========================================
IGNORE_DIRS = {
    # 版本控制
    '.git', '.svn', '.hg',
    # IDE 和编辑器配置
    '.idea', '.vscode', '.vs',
    # 虚拟环境和包管理
    'venv', 'env', '.env', 'node_modules', 'bower_components',
    # 编译和构建输出
    '__pycache__', 'build', 'dist', 'target', 'out', 'bin', 'obj',
    # 缓存和测试数据
    '.mypy_cache', '.pytest_cache', '.tox', '.coverage'
}

IGNORE_EXTS = {
    # 图片
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico', '.tiff', '.psd',
    # 视频/音频
    '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.mp3', '.wav', '.flac', '.ogg', '.m4a',
    # 压缩包
    '.zip', '.tar', '.gz', '.rar', '.7z', '.bz2',
    # 编译后文件/可执行文件
    '.pyc', '.pyd', '.pyo', '.exe', '.dll', '.so', '.dylib', '.class', '.jar', '.bin', '.o', '.a',
    # 常见文档/数据文件 (非纯文本)
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.sqlite', '.db', '.DS_Store'
}


def merge_to_clipboard(base_dir=".", include_files=None, exclude_files=None):
    """
    整合文件内容并保存到剪贴板。
    :param base_dir: 基础目录
    :param include_files: 列表。如果提供，则*只*合并列表中的这些文件。
    :param exclude_files: 列表。如果提供，将在遍历目录时排除这些特定文件。
    """
    current_script_path = os.path.abspath(__file__)

    # 规范化包含/排除的路径为绝对路径，方便比对
    include_files = [os.path.abspath(f) for f in (include_files or [])]
    exclude_files = [os.path.abspath(f) for f in (exclude_files or [])]

    merged_content = []
    separator_line = "=" * 80

    processed_count = 0
    skipped_count = 0

    print("正在处理文件，请稍候...")

    # 定义一个读取文件并追加到 merged_content 的辅助函数
    def process_file(abs_path):
        nonlocal processed_count, skipped_count
        if abs_path == current_script_path:
            return

        rel_path = os.path.relpath(abs_path, start=base_dir)
        try:
            with open(abs_path, 'r', encoding='utf-8') as infile:
                content = infile.read()

            merged_content.append(f"\n{separator_line}\n")
            merged_content.append(f"File: {rel_path}\n")
            merged_content.append(f"{separator_line}\n\n")
            merged_content.append(content)
            merged_content.append("\n")
            processed_count += 1

        except UnicodeDecodeError:
            skipped_count += 1
        except Exception as e:
            print(f"读取失败 [{rel_path}]: {e}")
            skipped_count += 1

    # ==========================================
    # 模式 1: 如果指定了 include_files，则只处理这些具体的文件
    # ==========================================
    if include_files:
        print("模式：仅合并指定的文件")
        for file_path in include_files:
            if os.path.isfile(file_path):
                process_file(file_path)
            else:
                print(f"警告: 找不到文件 {file_path}")
                skipped_count += 1

    # ==========================================
    # 模式 2: 如果没有指定 include_files，则遍历目录并应用排除规则
    # ==========================================
    else:
        print(f"模式：遍历目录 ({os.path.abspath(base_dir)}) 并自动过滤")
        for root, dirs, files in os.walk(base_dir):
            # 1. 过滤掉不需要遍历的文件夹 (原地修改 dirs 列表)
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            for file in files:
                abs_file_path = os.path.abspath(os.path.join(root, file))

                # 2. 检查是否在显式排除列表中
                if abs_file_path in exclude_files:
                    continue

                # 3. 检查是否属于自动排除的后缀名
                _, ext = os.path.splitext(file)
                if ext.lower() in IGNORE_EXTS:
                    continue

                process_file(abs_file_path)

    # 将结果写入剪贴板
    if merged_content:
        final_string = "".join(merged_content)
        pyperclip.copy(final_string)
        print(f"\n✅ 成功！已将 {processed_count} 个文件的内容复制到系统剪贴板。")
        print(f"💡 自动/手动跳过的不相关文件数: {skipped_count}")
        print("👉 现在你可以直接去 AI 对话框使用 Ctrl+V / Cmd+V 粘贴了。")
    else:
        print("\n⚠️ 未找到任何有效文本文件可以复制。")


if __name__ == "__main__":
    # -----------------------------------------------------------------
    # 使用示例配置区
    # -----------------------------------------------------------------

    # 获取当前工作目录
    current_dir = os.getcwd()

    # 方式 A：只合并你明确指定的几个文件（取消注释下方代码即可使用）
    # target_files = ["main.py", "utils/helper.py", "config.json"]
    # merge_to_clipboard(base_dir=current_dir, include_files=target_files)

    # 方式 B：遍历整个目录，自动排除垃圾文件，并额外排除你不想合并的特定文件
    # 例如：不想把 README.md 和某个测试脚本加进去
    files_to_exclude = ["README.md", "test_temp.py"]
    merge_to_clipboard(base_dir=current_dir, exclude_files=files_to_exclude)