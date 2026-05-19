# 🧬 DNA Sequence Analyzer

A full-stack web application that analyzes DNA sequences using **Stack** and **Queue** data structures, built with Django framework.

## 📌 Project Idea
The user enters a DNA sequence like `ATCGGCTA`.
The system will validate it, count each character, check complementary pairs, and save the result to the database.

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** Django
- **Database:** SQLite
- **Frontend:** HTML + CSS
- **Data Structures:** Stack + Queue

## ⚙️ How It Works
1. DNA sequence is loaded into a **Queue**
2. First half is pushed into a **Stack**
3. Stack and Queue are compared pair by pair
4. A↔T and C↔G are valid pairs
5. Result is saved to the database

## 📄 Project Files
| File | Description |
|------|-------------|
| `dna_logic.py` | Stack + Queue analysis logic |
| `models.py` | Database model |
| `views.py` | Connects everything |
| `urls.py` | URL routing |
| `home.html` | Input page |
| `result.html` | Result page |
| `history.html` | History page |

## 🚀 How to Run
```bash
python manage.py runserver
```
Then open: http://127.0.0.1:8000

