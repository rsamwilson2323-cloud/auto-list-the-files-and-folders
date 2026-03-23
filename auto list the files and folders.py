import os

print("\n==============================")
print(" FILE & FOLDER LIST VIEWER")
print("==============================\n")

# Ask user for folder path
folder_path = input("Enter the folder path: ").strip()

# Check if path exists
if not os.path.exists(folder_path):
    print("\n❌ Path does not exist.")
    input("Press Enter to exit...")
    exit()

# Check if it's a directory
if not os.path.isdir(folder_path):
    print("\n❌ Given path is not a folder.")
    input("Press Enter to exit...")
    exit()

print(f"\n📂 Contents of: {folder_path}\n")

# List items in folder
items = os.listdir(folder_path)

if not items:
    print("⚠️ Folder is empty.")
else:
    for item in items:
        full_path = os.path.join(folder_path, item)

        if os.path.isdir(full_path):
            print(f"[FOLDER] {item}")
        else:
            print(f"[FILE] {item}")

print("\n==============================")
input("Press Enter to exit...")
