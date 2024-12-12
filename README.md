## Library Management

Library Management System

A Library Management System (LMS) built using the Frappe Framework. This system allows librarians to efficiently manage books, users, and transactions, with powerful features like searching, borrowing, returning, and tracking book availability.
Features

-Book Management: Add, update, or delete books in the library system.
-User Management: Manage user information and track their borrowing history.
-Borrowing System: Track books borrowed by users, including due dates and overdue books.
-Return System: Mark books as returned and update the system's inventory.
-Search Functionality: Search for books by title, author, or genre.
-Reports: Generate reports for overdue books and borrowing statistics.

Tech Stack

-Framework: Frappe Framework
-Backend: Python (Frappe)
-Frontend: HTML, CSS, JavaScript (Frappe's web interface)
-Database: MariaDB (used by Frappe)
-Authentication: Integrated user management with Frappe's built-in authentication system
-Version Control: Git and GitHub

Setup and Installation

To get started with the Library Management System, follow these instructions to set up the project locally using the Frappe framework.

Prerequisites:
    Python 3.7+: Make sure you have Python installed.
    Node.js: Frappe uses Node.js for building frontend assets.
    MariaDB: Frappe uses MariaDB as the default database.
    Redis: Required for caching and queuing in Frappe.
    Yarn: Frappe uses Yarn for managing frontend dependencies.

You can follow the official Frappe installation guide to install these dependencies.

Steps to Install:
Follow these:

    git clone https://github.com/derapper4567/Library_Management_system_eastc.git
    cd library-management-system
    pip install frappe-bench
    bench new-site library.localhost
    bench --site library.local install-app library_management
    bench start

Environmental Configuration:
create .env file 

Usage

Access the System: After running the development server, navigate to http://localhost:8000 in your browser to interact with the Library Management System.

Admin Panel: Access the admin panel to manage books, users, and transactions by logging in with the administrator credentials.

User Registration: Users can register, borrow article, and create membership.

Search Articles: Use the search functionality to find books by title, author, or genre.


Contributing

welcome for contributions! If you'd like to help improve the Library Management System, follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature/your-feature).
    Make your changes and add tests if necessary.
    Commit your changes (git commit -m "feat: added new feature").
    Push your branch (git push origin feature/your-feature).
    Open a Pull Request.

Please ensure your code follows the existing style, and write tests for any new features.

License

This project is licensed under the MIT License – see the LICENSE file for details.


Acknowledgments

Inspired by library management systems and ERPNext.
Thanks to the Frappe community for providing an excellent framework.
Special thanks to  Aakvatech Company Limited and the open-source contributors for their valuable tools and libraries.




