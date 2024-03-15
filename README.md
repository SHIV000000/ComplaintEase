# ComplaintEase

ComplaintEase is a web application that allows users to file complaints, track their status, and enables administrators to manage and respond to complaints efficiently.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Installation

 **Clone the repository:**

```bash
 git clone https://github.com/SHIV000000/ComplaintEase.git
```
```bash
cd ComplaintEase
 ```
### Create a Virtual Environment

#### For macOS/Linux:

```bash
python3 -m venv venv
```

#### For Windows:

```bash
python -m venv venv
```

### Activate the Virtual Environment:

#### For macOS/Linux:

```bash
source venv/bin/activate
 ```

#### For Windows:

```bash
.\venv\Scripts\activate
```

## Install Dependencies:

```bash
pip install -r requirements.txt
```

Apply Migrations:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

**Run the Development Server**

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.
