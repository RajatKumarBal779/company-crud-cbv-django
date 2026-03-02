# Django Company Management System

A simple CRUD (Create, Read, Update, Delete) web application built using **Django Class-Based Views (CBVs)**.

This project demonstrates how to perform database operations using Django Generic Views such as:

- ListView  
- DetailView  
- CreateView  
- UpdateView  
- DeleteView  

---

## 🚀 Features

- View list of companies  
- View detailed company information  
- Add new company  
- Update company details  
- Delete company with confirmation page  
- Clean UI using Bootstrap 5  
- Uses `get_absolute_url()` for automatic redirection  

---

## 🛠️ Tech Stack

- Python 3  
- Django  
- SQLite  
- HTML5  
- Bootstrap 5  

---

## 📂 Project Structure

```
cbvproject3/
│
├── testapp/
│ ├── models.py
│ ├── views.py
│ ├── templates/
│ │ └── testapp/
│ │ ├── base.html
│ │ ├── company_list.html
│ │ ├── company_detail.html
│ │ ├── company_form.html
│ │ └── company_confirm_delete.html
│ └── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

## How to Run
- Clone the Repository ```bash
git clone https://github.com/your-username/django-company-crud-cbv.git
cd django-company-crud-cbv ```
- Apply Migrations ```python manage.py makemigrations
python manage.py migrate ```
- Run Development Server ```python manage.py runserver```
- Send Request ```http://127.0.0.1:8000/```

## Author & Contact

<strong>Rajat Kumar Bal </strong><br>
📧 Email: rajatkumarbal961@gmail.com<br>
🔗 <a href="https://www.linkedin.com/in/rajat-kumar-bal">LinkedIn</a><br>
<div align='center'>
  Made With 💖 by <strong>Rajat</strong>
</div>
