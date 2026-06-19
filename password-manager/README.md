# 🔐 Password Manager (Python + Tkinter)

A simple password manager built using Python that helps store and retrieve login credentials securely using a local JSON file. This project demonstrates core concepts of file handling, exception handling, GUI development, and data persistence.

---

## 🚀 Features

* Generate strong random passwords
* Save website credentials (website, email, password)
* Search saved credentials by website name
* Copy generated password automatically to clipboard
* Simple graphical user interface using Tkinter
* Handles missing or corrupted data files safely using exception handling

---

## 🧠 Concepts Used

* Python Functions
* Tkinter GUI (Labels, Buttons, Entry fields, Canvas)
* File Handling (read/write JSON files)
* Exception Handling (`try`, `except`, `else`, `finally`)
* Dictionaries for structured data storage
* Random module for password generation
* Pyperclip for clipboard operations

---

## 📁 Project Structure

```
password-manager/
│
├── main.py            # Main application code
├── data.json          # Stores saved credentials (auto-created)
├── logo.png           # UI logo image
└── README.md          # Project documentation
```

---

## ⚙️ How It Works

1. Enter website, email, and password
2. Click **Generate Password** to create a strong password (optional)
3. Click **Add** to save credentials in a JSON file
4. Use **Search** to retrieve saved credentials by website name

---

## 🔐 Exception Handling

The project safely handles:

* Missing `data.json` file
* Corrupted or empty JSON data
* Empty input fields

This ensures the application does not crash unexpectedly.


---

## 📌 Future Improvements

* Add password encryption (AES/Fernet)
* Master password authentication
* Delete and update saved entries
* Improve UI design (dark mode, better layout)
* Export data securely

---

## ⚠️ Disclaimer

This project is for educational purposes only. Passwords are stored in plain text inside a local JSON file and should not be used for production security systems.

---

## 👨‍💻 Author

Built as a learning project to improve Python skills and understand real-world application development concepts.
