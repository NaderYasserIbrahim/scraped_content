# 🧪 Odoo Developer Task: Web Scraping, API Integration & Custom Module

This project provides a full pipeline for scraping external content, pushing it into Odoo, and managing it through a custom module.

---

## 📦 Project Structure

- `scrapers/`  
  └ Contains scraping scripts for:  
  &nbsp;&nbsp;&nbsp;&nbsp;✔ LinkedIn Jobs  
  &nbsp;&nbsp;&nbsp;&nbsp;✔ TechCrunch Blogs  
  &nbsp;&nbsp;&nbsp;&nbsp;✔ VentureBeat Pages  

- `api_pusher.py`  
  └ A standalone script that reads scraped data and sends it to Odoo via JSON-RPC or XML-RPC.

- `scraped_content/`  
  └ A custom Odoo module with models:  
  &nbsp;&nbsp;&nbsp;&nbsp;✔ `scraped.job`  
  &nbsp;&nbsp;&nbsp;&nbsp;✔ `scraped.blog`  
  &nbsp;&nbsp;&nbsp;&nbsp;✔ `scraped.page`

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/odoo-scraping-task.git
cd odoo-scraping-task
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Odoo

- Place `scraped_content` in your Odoo `addons` directory.
- Add the module path to your `odoo.conf` file.

---

## 🕷️ How to Run the Scrapers

Each scraper can be executed independently:

```bash
# LinkedIn Jobs
python scrapers/linkedin_scraper.py

# TechCrunch Blogs
python scrapers/techcrunch_scraper.py

# VentureBeat Pages
python scrapers/venturebeat_scraper.py
```

Scraped data is stored in structured CSVs under `data/`.

---

## 🔁 How to Push Data to Odoo

After running the scrapers, you can push the data using:

```bash
python api_pusher.py
```

- Ensure Odoo is running
- Verify credentials and endpoint settings in `api_pusher.py`

---

## 🧩 Installing & Using the Odoo Module

### 1. Install the Module

- In Odoo, go to **Apps**
- Click **Update App List**
- Search for **Scraping Manager** or `scraped_content`
- Click **Install**

### 2. Explore the UI

Once installed, you'll find a new menu:  
📁 **Scraping Manager**

This contains:

- 📄 **Jobs**
- 📰 **Blogs**
- 📘 **Pages**

Each has:
- Tree View
- Form View
- Status (new, in_review, approved, archived)

### 3. API Support

All models are exposed to Odoo’s JSON-RPC / XML-RPC API so they can receive external data from the pusher script.

---

## ✅ Features Summary

| Component         | Features                                                                 |
|------------------|--------------------------------------------------------------------------|
| Scrapers         | LinkedIn, TechCrunch, VentureBeat extraction using Python               |
| API Pusher       | Sends mapped content to Odoo using JSON/XML-RPC                         |
| Odoo Module      | Structured models and UI under a custom menu                            |
| Status Workflow  | Status field: `new`, `in_review`, `approved`, `archived`                |
| API Ready        | Models are exposed for integration via external scripts                 |

---

## 🧠 Evaluation Criteria

- ✅ Clear modular separation between scraping, pushing, and the Odoo module
- ✅ Functional UI views and API endpoints
- ✅ Well-documented and maintainable code
- ✅ Use of Python and Odoo development best practices

---

## 📸 Screenshot

Here is an example of the UI:

![App Screenshot](images/Screenshot%202025-05-18%20225117.png)

![App Screenshot](images/Screenshot%202025-05-18%20225143.png)

![App Screenshot](images/Screenshot%202025-05-18%20225354.png)

![Screenshot 3](images/Screenshot%202025-05-18%20225451.png)


## 📩 Contact

For questions or support, contact: **naderyasseribrahim@gmail.com**
