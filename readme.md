

# **Lost and Found Web Application**

This is a **Django-based web application** that allows users to **report lost and found items**. The platform includes an **admin panel for staff moderation**, a database with **user profiles**, and a **secure authentication system**.

---

## **📌 Features**
✔ **User Registration & Authentication** – Users can sign up, log in, and manage their profiles.  
✔ **Lost & Found Items** – Users can post details of lost and found items.  
✔ **CRUD Operations** – Items can be created, edited, viewed, and deleted.  
✔ **Admin Moderation** – Staff users have permissions to manage items and users.  
✔ **Django Admin Panel** – Superusers can manage everything through the built-in Django admin panel.  
✔ **Responsive UI** – Bootstrap is used to make the interface clean and mobile-friendly.  

---

## **📌 Installation Guide**
Follow these steps to set up and run the project locally.

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/mukhametzhan-dev/lostandfound.git
cd lostandfound
```

### **2️⃣ Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Create a Superuser**
```bash
python manage.py createsuperuser
```
- Enter **username**, **email**, and **password** when prompted.

### **6️⃣ Run the Development Server**
```bash
python manage.py runserver
```
- Open **`http://127.0.0.1:8000/`** in your browser.

---

## **📌 Usage**
- **Home Page**: Displays a list of lost and found items.
- **Login/Register**: Users can register and log in to manage their items.
- **Admin Panel**: Visit **`http://127.0.0.1:8000/admin/`** to manage users and items.
- **Create/Edit/Delete Items**: Users can add new items, update details, or remove posts. (CRUD)

---

## **📌 Database Structure (UML)**
```
+----------------------+
|        User         |    Django built-in user model
|----------------------|
| id (PK)             |
| username            |
| email               |
| password            |
+----------------------+
        |
        | (1-to-1)
        ▼
+----------------------+
|      Profile        |    Extends User (OneToOne)
|----------------------|
| id (PK)             |
| user (FK -> User)   |
| image               |
+----------------------+

+----------------------+
|       Item          |    Represents a lost item
|----------------------|
| id (PK)             |
| title               |
| description         |
| image              |
| found_by (FK -> User) |
| contact_info        |
| created_at          |
| creator (FK -> User) |
+----------------------+

+----------------------+
|    StaffProfile     |    Represents staff users
|----------------------|
| id (PK)             |
| user (FK -> User)   |
| department          |
| phone_number        |
+----------------------+
```

---


   ```

---

  ```

---

## **📌 License**
This project is open-source and available under the **MIT License**.

---

🚀 **Now, you’re ready to contribute to the Lost and Found web app!** 🎯

---

Let me know if you want any modifications! 😊
![mukhametzhan-dev's GitHub stats](https://github-readme-stats.vercel.app/api?username=mukhametzhan-dev&show_icons=true&theme=radical)
