# 🛒 Python Playwright Automation – Demo E-Commerce Website

This project automates end-to-end test cases for a demo e-commerce website using **Playwright with Python** and **Pytest**.

## 🚀 Project Features

- ✅ Automated login functionality
- ✅ Page Object Model structure
- ✅ Asynchronous Playwright fixtures
- ✅ Allure & HTML reporting support
- ✅ Custom element locators for robust UI automation
- ✅ Easy to extend for product page, cart, checkout, and more

---

## 📁 Folder Structure

Main Folder
│
├── conftest.py # Reusable Playwright fixtures
├── tests/
│ └── test_login.py # Login test using POM
├── pages/
│ ├── base_page.py # Common reusable Playwright methods
│ └── login_page.py # Page object for login screen
├── reports/ # Allure or HTML reports generated here
├── pytest.ini # Pytest configuration
└── README.md # Project documentation
