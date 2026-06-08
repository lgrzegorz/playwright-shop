# 🛒 Playwright E2E Test Suite — SauceDemo

![Tests](https://github.com/lgrzegorz/playwright-shop/actions/workflows/playwright.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Playwright](https://img.shields.io/badge/playwright-1.44+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Portfolio project demonstrating **Python + Playwright** test automation with Page Object Model, pytest fixtures, automatic screenshots on failure, and GitHub Actions CI/CD running on Chromium and Firefox.

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
│       ├── test_auth.py        # Login / logout (5 tests)
│       ├── test_inventory.py   # Product listing & sorting (9 tests)
│       ├── test_cart.py        # Cart management (3 tests)
│       └── test_checkout.py    # Checkout flow & validation (5 tests)
├── utils/
│   └── helpers.py          # Faker data generators, price parser
├── .github/
│   └── workflows/
│       └── playwright.yml  # GitHub Actions CI/CD pipeline
├── conftest.py             # Shared fixtures + screenshot on failure
├── pytest.ini              # pytest config, markers, auto-reruns
├── requirements.txt
└── .env.example
```

---

## 🚀 Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/lgrzegorz/playwright-shop.git
cd playwright-shop
```

### 2. Create a virtual environment

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install chromium firefox
```

### 5. Configure environment

```bash
cp .env.example .env
# .env already contains correct values for saucedemo.com
```

---

## ▶️ Running Tests

```bash
# Full suite
pytest

# Only smoke tests
pytest -m smoke

# Specific file
pytest tests/e2e/test_checkout.py

# Firefox
pytest --browser firefox

# Headed mode (see the browser)
pytest --headed

# Parallel — 4 workers
pytest -n 4
```

---

## 📊 Test Report

After each run an HTML report is generated at `reports/report.html`.

```bash
open reports/report.html        # macOS
xdg-open reports/report.html    # Linux
start reports/report.html       # Windows
```

---

## 📸 Screenshots on Failure

When a test fails, a full-page screenshot is saved automatically to:

```
test-results/screenshots/<test_name>.png
```

In CI, screenshots are uploaded as a GitHub Actions artifact and available for download from the Actions run summary.

---

## 🏷️ Markers

| Marker       | Description                           |
|--------------|---------------------------------------|
| `smoke`      | Critical happy-path checks (~8 tests) |
| `regression` | Full suite including edge cases       |
| `auth`       | Login / logout tests                  |
| `cart`       | Shopping cart tests                   |
| `checkout`   | Checkout flow tests                   |

---

## ⚙️ CI/CD — GitHub Actions

The pipeline runs automatically on:

- Every push to `main` or `develop`
- Every pull request targeting `main`
- Nightly at 02:00 UTC
- Manual trigger with optional marker filter

### Artifacts available after each run

| Artifact | Contents |
|---|---|
| `report-chromium` | Full HTML test report |
| `report-firefox` | Full HTML test report |
| `screenshots-chromium` | Screenshots of failed tests (only on failure) |

### Manual run with marker filter

In GitHub → Actions → **Playwright Tests** → **Run workflow**, enter a marker (e.g. `smoke`) to run only that subset.

---

## 🧩 Key Design Decisions

| Pattern | Why |
|---|---|
| **Page Object Model** | Separates selectors from test logic; one fix when UI changes |
| **Fixtures in conftest.py** | Reusable setup/teardown; keeps tests DRY |
| **Faker for test data** | Avoids hardcoded names; prevents data pollution |
| **Screenshot on failure** | Instant visual diagnosis without re-running |
| **Auto-reruns (x2)** | Handles transient network flakiness automatically |
| **Matrix strategy in CI** | Catches browser-specific bugs automatically |

---

## 📌 Requirements

- Python 3.11+
- Playwright 1.44+
- pytest 8+
