# ComplaintEase

ComplaintEase is a web application that allows users to file complaints, track their status, and enables administrators to manage and respond to complaints efficiently.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Installation

 **Clone the repository:**

```bash
 git clone https://github.com/your-username/ComplaintEase.git
```
```bash
cd ComplaintEase
 ```
**Create a Virtual Environment**
On macOS/Linux:
   ```bash

   python3 -m venv venv
   ```
 On Windows:
   ```bash
   python -m venv venv
   ```
On macOS/Linux:
Activate the Virtual Environment:
```bash
source venv/bin/activate
 ```
On Windows:
Activate the Virtual Environment:
```bash
.\venv\Scripts\activate
```
Install Dependencies:

```bash
pip install -r requirements.txt
```

Apply Migrations:

```bash
python manage.py migrate
```

**Run the Development Server**

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.
