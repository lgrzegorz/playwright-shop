# 🛒 Playwright E2E Test Suite — SauceDemo

Portfolio project demonstrating **Python + Playwright** test automation with Page Object Model, pytest fixtures, HTML reports, and GitHub Actions CI/CD.

**Tested site:** [saucedemo.com](https://www.saucedemo.com) — a purpose-built e-commerce demo for QA practice.

---

## 📁 Project Structure

```
playwright-shop/
├── pages/                  # Page Object Model classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   └── e2e/
│       ├── test_auth.py        # Login / logout
│       ├── test_inventory.py   # Product listing & sorting
│       ├── test_cart.py        # Cart management
│       └── test_checkout.py    # Checkout flow & validation
├── utils/
│   └── helpers.py          # Faker data generators, price parser
├── .github/
│   └── workflows/
│       └── playwright.yml  # GitHub Actions pipeline
├── conftest.py             # Shared fixtures
├── pytest.ini              # pytest config & markers
├── requirements.txt
└── .env.example
```

---

## 🚀 Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/playwright-shop.git
cd playwright-shop
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install --with-deps chromium firefox
```

### 5. Configure environment

```bash
cp .env.example .env
# .env already contains the right values for saucedemo.com
# Edit if you're pointing at a different environment
```

---

## ▶️ Running Tests

### Run the full suite (Chromium)

```bash
pytest
```

### Run only smoke tests

```bash
pytest -m smoke
```

### Run a specific test file

```bash
pytest tests/e2e/test_checkout.py
```

### Run on Firefox

```bash
pytest --browser firefox
```

### Run in headed mode (see the browser)

```bash
pytest --headed
```

### Run tests in parallel (4 workers)

```bash
pytest -n 4
```

### Run with slow motion (useful for demos)

```bash
pytest --headed --slowmo 500
```

---

## 📊 Test Report

After each run an HTML report is generated at:

```
reports/report.html
```

Open it in any browser:

```bash
# macOS
open reports/report.html

# Linux
xdg-open reports/report.html

# Windows
start reports/report.html
```

---

## 🏷️ Markers

| Marker       | Description                        |
|--------------|------------------------------------|
| `smoke`      | Critical happy-path checks (~8 tests) |
| `regression` | Full suite including edge cases    |
| `auth`       | Login / logout tests               |
| `cart`       | Shopping cart tests                |
| `checkout`   | Checkout flow tests                |

---

## ⚙️ CI/CD — GitHub Actions

The pipeline runs automatically on:

- Every push to `main` or `develop`
- Every pull request targeting `main`
- Nightly at 02:00 UTC (scheduled)
- Manual trigger with optional marker filter

### Setup steps

1. Push this repo to GitHub.
2. Go to **Settings → Secrets and variables → Actions**.
3. Add these secrets (or leave them out — the workflow falls back to the public demo values):

   | Secret          | Value                        |
   |-----------------|------------------------------|
   | `BASE_URL`      | `https://www.saucedemo.com`  |
   | `STANDARD_USER` | `standard_user`              |
   | `PASSWORD`      | `secret_sauce`               |

4. Push a commit — the **Playwright Tests** workflow will start automatically.
5. Download the `report-chromium.html` artifact from the Actions run summary.

### Manual run with marker filter

In GitHub → Actions → **Playwright Tests** → **Run workflow**, enter a marker (e.g. `smoke`) to run only that subset.

---

## 🧩 Key Design Decisions

| Pattern | Why |
|---|---|
| **Page Object Model** | Separates selectors from test logic; one fix when UI changes |
| **Fixtures in conftest.py** | Reusable setup/teardown; keeps tests DRY |
| **Faker for test data** | Avoids hardcoded names; prevents data pollution |
| **pytest markers** | Enables targeted runs (smoke in CI, regression nightly) |
| **Matrix strategy in CI** | Catches browser-specific bugs automatically |

---

## 📌 Requirements

- Python 3.11+
- Playwright 1.44+
- pytest 8+
