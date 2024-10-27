import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QCheckBox
)
from PyQt6.QtCore import Qt

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

# Register window
class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.resize(300, 200)
        
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.show_password_checkbox = QCheckBox("Show Password")
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        
        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register_user)
        
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.show_password_checkbox)
        layout.addWidget(self.register_button)
        
        self.setLayout(layout)
    
    def toggle_password_visibility(self):
        if self.show_password_checkbox.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
    
    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Both fields are required.")
            return

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            QMessageBox.information(self, "Success", "Registration successful!")
            self.clear_inputs()
            self.close()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Error", "Username already exists.")
        finally:
            conn.close()
    
    def clear_inputs(self):
        self.username_input.clear()
        self.password_input.clear()
        self.show_password_checkbox.setChecked(False)

# Menu window with logout option
class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.resize(300, 200)
        
        self.welcome_label = QLabel("Welcome to the main menu!")
        self.logout_button = QPushButton("Logout")
        self.logout_button.clicked.connect(self.logout)
        
        layout = QVBoxLayout()
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.logout_button)
        self.setLayout(layout)
    
    def logout(self):
        self.close()
        login_window.show()  # Show the login window again after logout

# Login window
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(300, 200)
        
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.show_password_checkbox = QCheckBox("Show Password")
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login_user)
        
        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.open_register_window)
        
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.show_password_checkbox)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        
        self.setLayout(layout)
    
    def toggle_password_visibility(self):
        if self.show_password_checkbox.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
    
    def login_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            QMessageBox.information(self, "Success", "Login successful!")
            self.clear_inputs()
            self.open_menu_window()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")
    
    def clear_inputs(self):
        self.username_input.clear()
        self.password_input.clear()
        self.show_password_checkbox.setChecked(False)
    
    def open_register_window(self):
        self.username_input.clear()
        self.password_input.clear()
        self.register_window = RegisterWindow()
        self.register_window.show()
    
    def open_menu_window(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()

# Main application
app = QApplication(sys.argv)
init_db()  # Initialize the database

login_window = LoginWindow()
login_window.show()

sys.exit(app.exec())
