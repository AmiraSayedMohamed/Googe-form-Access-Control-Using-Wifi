# 🚀 Google Form Access Control Using WiFi  

## 🔒 Restrict Access to a Google Form Based on WiFi IP  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.0%2B-green) ![Status](https://img.shields.io/badge/Status-Active-success)  

---

## 📌 About the Project  
This Flask-based application restricts access to a Google Form based on the user's WiFi network IP. Only users within a specific IP range (e.g., `192.168.1.x`) can access the form, while others are denied access.  

### ✅ Features  
- 🛡️ **Restricts access** to a Google Form based on local network IP  
- 🌐 **Redirects authorized users** to the form  
- 🚫 **Blocks unauthorized users** with a 403 error  
- ⚡ **Lightweight and easy to deploy**  

---

## 🖼️ Project Preview  

### 🔹 Authorized User  
![Allowed User](assets/allowed_user.png)  

### 🔹 Unauthorized User  
![Blocked User](assets/blocked_user.png)  

---

## 📂 Installation  

### 🔧 Prerequisites  
Ensure you have **Python 3.8+** installed.  

### 📥 Clone the Repository  
```bash
git clone https://github.com/AmiraSayedMohamed/Googe-form-Access-Control-Using-Wifi.git
cd Googe-form-Access-Control-Using-Wifi
```
### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```
### 🚀 Run the Application
```bash
python app.py
```
### ⚙️ Configuration
- Change the allowed subnet in app.py:
```bash
ALLOWED_SUBNET = "192.168.1"
```
This allows only devices within the 192.168.1.x range to access the Google Form.

Replace the Google Form URL in app.py:
```bash
FORM_URL = "https://forms.microsoft.com/Pages/ResponsePage.aspx?id=..."
```
### 💡 Contribution
Feel free to fork the repository, create a new branch, and submit a pull request. 🚀


### 👩‍💻 Author
- **Amira Sayed Mohamed Ali**
🔗 [LinkedIn Profile](https://www.linkedin.com/in/amira-sayed-mohamed-79822b245/)  | 🐙 [GitHub Profile](https://github.com/AmiraSayedMohamed)


