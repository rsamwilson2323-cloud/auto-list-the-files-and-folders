# 📂 File & Folder Creator Tool

File & Folder Creator Tool is a command-line utility built using **Python 🐍**.

The program allows users to quickly create folders and files using a single structured input command, making project setup faster and more efficient.

---

# ✨ Features

📁 **Automatic Folder Creation**

* Creates folders instantly  
* Supports multiple folders  

📄 **File Generation**

* Creates files inside folders  
* Supports multiple file creation  

⚡ **Single-Line Input System**

* Define full structure in one line  
* Simple and powerful syntax  

🖥 **CLI Based Tool**

* Easy to use  
* Fast execution  

💻 **Lightweight**

* No external libraries required  

---

# 📂 Project Structure

```
auto-list-the-files-and-folders
│
├── auto list the files and folders.py
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```
git clone https://github.com/rsamwilson2323-cloud/auto-list-the-files-and-folders.git
cd auto-list-the-files-and-folders
```

---

# 📦 Requirements

```
Python 3.x
```

---

# ▶️ Usage

Run the program:

```
python "auto list the files and folders.py"
```

Enter main folder path:

```
Enter main folder path: D:\Projects
```

Enter structure:

```
app{main.py},photo,game{game.py},index.html
```

---

# 🧪 Example Output

```
[FOLDER] app
  └── [FILE] main.py
[FOLDER] photo
[FOLDER] game
  └── [FILE] game.py
[FILE] index.html
```

---

# 🧠 How It Works

📂 **Input Parsing**

The program reads the structure string and splits items using commas.

📁 **Folder Creation**

Creates folders using `os.makedirs()`.

📄 **File Creation**

Creates files using Python file handling (`open()`).

⚡ **Logic Handling**

Detects `{}` to identify files inside folders and processes them accordingly.

---

# 🎯 Output

Creates folders and files in the specified directory exactly as defined in the input structure.

---

# 🚀 Future Improvements

📁 Nested folder support  
📊 Advanced structure parsing  
🎨 Colored CLI output  
📄 Export structure templates  
🖥 GUI version  

---

# ⚠️ Disclaimer

This project is intended for **educational and productivity purposes only**.

---

# 👨‍💻 Author

**Sam Wilson**

🌐 GitHub  
https://github.com/rsamwilson2323-cloud  

💼 LinkedIn  
https://www.linkedin.com/in/sam-wilson-14b554385  

---

# 📜 License

This project is licensed under the **MIT License**.
