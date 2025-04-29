import os
#generated 
def generate_index_md(folder):
    # Create a basic index.md file listing .md files and subfolders, if index.md doesn't already exist.
    index_path = os.path.join(folder, "index.md")
    if os.path.exists(index_path):
        print(f"✅ Skipping existing: {index_path}")
        return
    else:
        print(f"📄 Creating: {index_path}")

    # Section title from folder name
    folder_name = os.path.basename(folder)
    title = folder_name.replace("_", " ").replace("-", " ").title()

    lines = [
f'''
# 📂 {index_path.split('\\')[1]} {title}\n
## Contents:\n
'''
]

    # List Markdown files (except index.md)
    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".md") and filename != "index.md" and not filename.endswith(".hidden.md"):
            display_name = os.path.splitext(filename)[0].replace("-", " ").title()
            lines.append(f"- [{display_name}]({filename})")

    # List subfolders that contain an index.md
    for subdir in sorted(os.listdir(folder)):
        subfolder_path = os.path.join(folder, subdir)
        if os.path.isdir(subfolder_path):
            sub_index = os.path.join(subfolder_path, "index.md")
            if os.path.exists(sub_index):
                lines.append(f"- [{subdir.title()}]({subdir}/)")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def walk_through_docs(base_dir):
    # Recursively walk through documentation folder and generate index.md files as needed.
    for dirpath, dirnames, filenames in os.walk(base_dir):
        # Only process folders that contain Markdown or subfolders
        if any(f.endswith(".md") for f in filenames) or dirnames:
            generate_index_md(dirpath)

# === CONFIG HERE ===
if __name__ == "__main__":
    docs_root = "Documents"
    walk_through_docs(docs_root)
