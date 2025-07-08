# 💼 Expense Management Dashboard

An end-to-end expense tracking and analytics solution built using **Streamlit**, **FastAPI**, and **MySQL**.

---

## 📸 Dashboard Screenshots

### ➕ Add / Update Expenses

![Add / Update Expenses](expense_ui_01.png)

### 📊 Analytics by Category

![Analytics by Category](expense_ui_02.png)

### 📅 Analytics by Month

![Analytics by Month](expense_ui_03.png)

### 📄 Custom Reports

![Custom Reports](expense_ui_04.png)

---

## 📌 Project Overview

This project delivers a fully functional expense management system comprising:

* A responsive **Streamlit frontend** for user interaction.
* A high-performance **FastAPI backend** for data processing.
* **MySQL** for persistent storage and analytics.

The system empowers users to manage personal or business expenses, analyze trends, and generate custom financial reports with ease.

---

## 🛠️ Technology Stack

| Layer          | Technology                                       |
| -------------- | ------------------------------------------------ |
| **Frontend**   | [Streamlit](https://streamlit.io/)               |
| **Backend**    | [FastAPI](https://fastapi.tiangolo.com/)         |
| **Database**   | [MySQL](https://www.mysql.com/)                  |
| **ORM**        | [SQLAlchemy](https://www.sqlalchemy.org/)        |
| **Validation** | [Pydantic](https://pydantic-docs.helpmanual.io/) |
| **Server**     | [Uvicorn](https://www.uvicorn.org/) (ASGI)       |
| **Testing**    | [pytest](https://docs.pytest.org/)               |

---

## 🚀 Features

* ✅ **Expense Entry & Modification**
  Add, update, and manage daily expenses with category-wise tagging and notes.

* 📊 **Visual Analytics**
  Analyze expenses by **month** and **category** through bar charts and pie charts.

* 📄 **Custom Reports**
  Generate dynamic reports with filters such as date range, category, vendor, and amount.

* 💾 **MySQL Integration**
  All transactions are stored securely in a relational database.

* 🧪 **Unit & Integration Testing**
  Robust test coverage using `pytest`.

---

## 📂 Project Structure

```
expense-dashboard-python-streamlit/
├── backend/           # FastAPI backend logic
├── frontend/          # Streamlit frontend UI
├── database/          # SQL schema and seed files
├── server/            # FastAPI server entry point
├── tests/             # Test cases (pytest)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SurajK221b/expense-dashboard-python-streamlit.git
cd expense-dashboard-python-streamlit
```

### 2️⃣ Configure the Database

* Import the `.sql` file from the `/database` folder using MySQL Workbench or CLI.
* Ensure the database is named `expense-manager`.

### 3️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Launch the FastAPI Server

```bash
uvicorn server.server:app --reload
```

> 🔄 If issues persist, try:

```bash
cd expense-dashboard-python-streamlit/frontend
fastapi dev .\server.py
```

### 5️⃣ Start the Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

## 📈 Future Enhancements (Planned)

* 🔐 User authentication and multi-user support
* 📅 Recurring expenses & subscriptions
* 📦 Expense imports from CSV/Excel
* 📤 Email-based report delivery
* 🧠 AI-based insights and anomaly detection

---

## 🤝 Contributing

Pull requests and issue reports are welcome. Please follow best practices and ensure tests pass locally.
