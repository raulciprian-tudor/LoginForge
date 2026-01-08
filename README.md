# LoginForge 🔐

LoginForge is a command-line authentication system written in Python.
It was built as part of my learning journey to practice **program flow, state management, validation logic, and iterative refactoring**.

This project focuses on correctness, clarity, and evolution rather than frameworks or UI.

---

## ✨ Features

- User login with password validation
- Limited login attempts with automatic account locking
- Session handling (login / logout)
- Admin-only account unlocking
- Password change flow for authenticated users
- Audit trail with timestamps for authentication events

---

## 🧠 What This Project Demonstrates

- Clean control flow using conditionals and loops
- State management without frameworks
- Separation of concerns (process vs helper functions)
- Refactoring without breaking behavior
- Defensive input handling
- Incremental feature development
- Basic security logic (attempt limits, lockouts, permissions)

---

## 🛠️ How It Works

- Users are stored in an in-memory dictionary
- Authentication logic is handled explicitly (no exceptions for flow control)
- Login attempts are tracked per user
- Locked accounts require admin intervention
- All authentication-related events are logged with timestamps

---

## ▶️ How to Run

Requirements:
- Python 3.x

Run the program from the terminal:

```bash
python loginforge.py

## Available Commands
login            - Authenticate a user
logout           - End current session
unlock           - Unlock a locked user (admin only)
change password  - Update password for logged-in user
history          - View authentication audit log
help             - Show command list
exit             - Exit the program

