import os
import shutil

# File types to scan
allowed_extensions = ['.rs', '.dart', '.yaml', '.rc', '.md', '.txt']

# What to replace (only user-visible strings!)
replacements = {
    'RustDesk': 'CyberDesk',
    'rustdesk.com': 'cyberdesk.app',
    'RustDesk Remote Desktop': 'CyberDesk Remote Desktop'
}

# Files to skip
skip_files = ['Cargo.toml', 'pubspec.yaml']

def safe_replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        original_content = content
        for old, new in replacements.items():
            content = content.replace(old, new)

        if content != original_content:
            print(f"[MODIFIED] {filepath}")
            shutil.copyfile(filepath, filepath + ".bak")
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")

def scan_and_replace(root_folder):
    for root, _, files in os.walk(root_folder):
        for fname in files:
            if fname in skip_files:
                continue
            ext = os.path.splitext(fname)[1]
            if ext in allowed_extensions:
                safe_replace_in_file(os.path.join(root, fname))

if __name__ == "__main__":
    scan_and_replace(".")
    print("\n✅ Safe rebrand complete! Backups saved as *.bak")
