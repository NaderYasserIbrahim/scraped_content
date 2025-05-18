import csv
import os
import xmlrpc.client

# 🔧 CONFIGURATION
ODOO_URL = 'http://localhost:8069'
DB = 'hms_db'            # Replace with your actual database name
USERNAME = 'admin'          # Replace with your Odoo login
PASSWORD = 'admin'          # Replace with your Odoo password

# Model -> CSV file path mapping
MODELS = {
    'jobs': ('scraped.job', 'data/linkedin_jobs.csv'),
    'blogs': ('scraped.blog', 'data/techcrunch_blogs.csv'),
    'pages': ('scraped.page', 'data/venturebeat_pages.csv'),
}

def get_absolute_path(relative_path):
    """Return full path to CSV relative to this script."""
    base_path = os.path.dirname(os.path.abspath(__file__))  # /pusher
    return os.path.abspath(os.path.join(base_path, '..', relative_path))

def authenticate():
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    uid = common.authenticate(DB, USERNAME, PASSWORD, {})
    if not uid:
        raise Exception("❌ Authentication failed. Check DB, username, or password.")
    print(f"✅ Authenticated with UID: {uid}")
    return uid

def push_data(uid, model_name, csv_path):
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    abs_csv_path = get_absolute_path(csv_path)

    with open(abs_csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        count = 0
        for row in reader:
            vals = {}

            if model_name == 'scraped.job':
                vals = {
                    'name': row.get('Job Title', '').strip(),
                    'company_name': row.get('Company Name', '').strip(),
                    'company_logo_url': row.get('Company Logo', '').strip(),
                    'location': row.get('Location', '').strip(),
                    'source_url': row.get('Source URL', '').strip(),
                    'status': 'new'
                }

            elif model_name == 'scraped.blog':
                vals = {
                    'title': row.get('title', '').strip(),
                    'summary': row.get('summary', '').strip(),
                    'content': row.get('content', '').strip(),
                    'source_url': row.get('source_url', '').strip(),
                    'status': 'new'
                }

            elif model_name == 'scraped.page':
                vals = {
                    'title': row.get('title', '').strip(),
                    'content': row.get('content', '').strip(),
                    'source_url': row.get('source_url', '').strip(),
                    'status': 'new'
                }

            # Send create request
            models.execute_kw(DB, uid, PASSWORD, model_name, 'create', [vals])
            count += 1

    print(f"✅ {count} records pushed to {model_name}")

if __name__ == '__main__':
    try:
        uid = authenticate()
        for label, (model_name, csv_file) in MODELS.items():
            print(f"\n🔄 Pushing {label} from {csv_file} into {model_name} ...")
            push_data(uid, model_name, csv_file)
    except Exception as e:
        print(f"❌ Error: {e}")
