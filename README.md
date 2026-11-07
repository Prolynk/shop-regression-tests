# Shop regression tests

[![Tests](https://github.com/Prolynk/shop-regression-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/Prolynk/shop-regression-tests/actions/workflows/tests.yml)

Python regression checks for [Sauce Demo](https://www.saucedemo.com/) and the [DummyJSON Products API](https://dummyjson.com/docs/products). The API is a separate demo service, not the shop backend.

## Setup

Requires Python 3.12 and internet access.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest
```

On Windows use `python` and `.venv\Scripts\activate`. On Linux install browser system packages with `python -m playwright install --with-deps chromium`.

## Coverage

| Area | Cases |
|---|---:|
| Login and logout | 6 |
| Product inventory and sorting | 3 |
| Cart | 2 |
| Checkout | 2 |
| Products API | 6 |
| Total | 19 |

The browser cases cover valid, invalid and locked login; required fields; product count; price and name sorting; cart contents and badge changes; order completion; and logout. The API cases cover HTTP/JSON, required fields, positive prices, limits, resource identity and missing resources.

## Running checks

```bash
python -m pytest --headed
python -m pytest -m ui
python -m pytest -m api
python scripts/smoke_check.py
```

The smoke pack reuses three browser cases (login, cart and checkout) and one API case. These four checks are included in the total of 19.

HTML and JUnit reports are written to `reports/`. Browser failures retain screenshots and traces in `test-results/` when a browser context exists. Open a trace with `python -m playwright show-trace PATH_TO_TRACE.zip`.

## Structure

- `pages/`: page objects containing selectors and actions.
- `tests/ui/`: browser checks using fresh contexts.
- `tests/api/`: read-only API checks with request timeouts.
- `utils/`: public demo credentials and product identifiers.
- `ai_review/`: accepted and rejected test suggestions.
- `scripts/`: smoke runner with pass/fail exit status.

Selectors use `data-test` attributes. Playwright assertions wait for expected state; there are no fixed sleeps or automatic assertion retries beyond Playwright's built-in waiting.

## Automation

GitHub Actions runs the full suite on every push and pull request. Manual dispatch offers full or smoke. A daily 07:00 UTC timer selects smoke on the default branch; GitHub may delay scheduled jobs. The workflow uses Ubuntu 24.04 and Python 3.12, installs Chromium and uploads reports and failure evidence for 14 days. The status badge and Actions history show actual outcomes. A manual smoke result does not establish that the scheduled trigger ran.

## Configuration and limits

`SHOP_URL` and `PRODUCTS_API_URL` override the demo targets. `PLAYWRIGHT_PROXY` optionally sets an explicit browser proxy. HTTPS verification stays enabled.

The suite targets Chromium and the English demo interface. It assumes six shop products and the demo backpack's $29.99 subtotal. Catalogue or interface changes require reviewing those contracts. Public service outages can produce failures independently of application regressions. This pack does not cover mobile, performance, accessibility or real payment processing. Checkout uses fictional information.
