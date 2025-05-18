# 🧪 Odoo Developer Task: Web Scraping, API Integration & Custom Module

This project delivers an integrated solution for scraping web data, pushing it to Odoo, and managing it through a custom Odoo module named `scraped_content`.

---

## 📦 Project Structure

- `scrapers/`
  - `linkedin_scraper.py`: Scrapes job postings from LinkedIn.
  - `techcrunch_scraper.py`: Scrapes blog posts from TechCrunch.
  - `venturebeat_scraper.py`: Scrapes static pages from VentureBeat.

- `api_pusher.py`: Pushes scraped data into Odoo via JSON-RPC or XML-RPC.

- `scraped_content/`: Custom Odoo module containing:
  - Models: `scraped.job`, `scraped.blog`, `scraped.page`
  - Views and Menus
  - API exposure for integration

- `data/`: CSV  files for scraped output.

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/odoo-scraping-task.git
cd odoo-scraping-task
