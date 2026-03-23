import os

print("\n==============================")
print(" FILE & FOLDER CREATOR")
print("==============================\n")

# Get base path
base_path = input("Enter main folder path: ").strip()

if not os.path.exists(base_path):
    os.makedirs(base_path)
    print("📁 Main folder created.")

# Get structure input
structure = input("\nEnter structure: ").strip()

items = structure.split(",")

for item in items:
    item = item.strip()

    # Folder with files
    if "{" in item and "}" in item:
        folder_name = item.split("{")[0]
        files = item.split("{")[1].replace("}", "").split(",")

        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"[FOLDER] {folder_name}")

        for f in files:
            file_path = os.path.join(folder_path, f.strip())
            open(file_path, "w").close()
            print(f"  └── [FILE] {f.strip()}")

    else:
        # File or empty folder
        if "." in item:
            file_path = os.path.join(base_path, item)
            open(file_path, "w").close()
            print(f"[FILE] {item}")
        else:
            folder_path = os.path.join(base_path, item)
            os.makedirs(folder_path, exist_ok=True)
            print(f"[FOLDER] {item}")

print("\n==============================")
input("Press Enter to exit...")
