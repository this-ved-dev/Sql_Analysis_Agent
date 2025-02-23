# SQL Error Analysis and Rubric Validation Tool

This is a Flask-based AI-powered tool that analyzes SQL queries, identifies errors, and explains them. The tool uses the Google Gemini API to enhance SQL debugging and learning for students.

## 🚀 Features
- **Fix SQL Queries**: Identify and correct errors in SQL queries.
- **Format SQL Queries**: Properly format SQL queries for better readability.
- **Simplify SQL Queries**: Suggest simplified versions of SQL queries.
- **Explain SQL Queries**: Provide explanations for the SQL query structure and logic.

---

## 🛠️ Installation and Setup

### **1️⃣ Clone the Repository**
Open a terminal and run the following command:

```sh
git clone https://github.com/your-username/SQL-Error-Analysis.git
cd SQL-Error-Analysis
```

### **2️⃣ Create a Virtual Environment**
Before running the application, create and activate a virtual environment:

- **On macOS/Linux:**
  ```sh
  python -m venv venv
  source venv/bin/activate
  ```
- **On Windows:**
  ```sh
  python -m venv venv
  venv\Scripts\activate
  ```

### **3️⃣ Install Dependencies**
Once the virtual environment is activated, install the required dependencies:

```sh
pip install -r requirements.txt
```

---

## ▶️ Running the Application

To start the Flask application, use:

```sh
python app.py
```

The application should now be running at:  
➡️ `http://127.0.0.1:5000/`

---

## 📝 Usage
1. Enter an SQL query in the **left box** of the interface.
2. Select one of the functionalities:
   - **Fix SQL Query**
   - **Format SQL Query**
   - **Simplify SQL Query**
   - **Explain SQL Query**
3. The result will be displayed in the **right box**.

---

## 🛠️ Development & Contribution
If you'd like to contribute:
1. **Fork** the repository.
2. Create a new **feature branch**:
   ```sh
   git checkout -b feature-branch-name
   ```
3. **Commit your changes**:
   ```sh
   git commit -m "Added new feature X"
   ```
4. **Push to GitHub** and create a **pull request**.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📩 Contact
For questions or suggestions, feel free to reach out.

💡 **Happy Coding!**
