# WinWin.travel — UI Test Automation

Automated UI test suite for [winwin.travel](https://winwin.travel/), built with **Playwright** (Python) and **pytest**, using the **Page Object** pattern and **Allure** for reporting. Tests run automatically on every push/PR via **GitHub Actions**, and the Allure report is published to **GitHub Pages**.

## Tech Stack

- [Python 3.11](https://www.python.org/)
- [pytest](https://docs.pytest.org/)
- [pytest-playwright](https://playwright.dev/python/docs/test-runners)
- [allure-pytest](https://allurereport.org/docs/pytest/)
- GitHub Actions + GitHub Pages (via [simple-elf/allure-report-action](https://github.com/simple-elf/allure-report-action) and [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages))

## Project Structure

```
.
├── .github/workflows/
│   └── playwright.yml          # CI pipeline: run tests, build & deploy Allure report
├── actions/                    # Page Object classes
│   ├── mainPage.py
│   ├── adultsSection.py
│   └── filtersSection.py
├── tests/                      # Test files
│   └── test_main_page.py
├── conftest.py                 # Shared fixtures (base URL, browser context)
├── requirements.txt            # Python dependencies
├── testcases.txt               # Manual test case documentation
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
git clone <repo-url>
cd WinWin.travel-test-task
pip install -r requirements.txt
playwright install --with-deps chromium
```

### Running Tests Locally

Run the full suite:

```bash
pytest
```

Run with Allure results collection:

```bash
pytest --alluredir=allure-results
```

View the report locally (requires the [Allure commandline tool](https://allurereport.org/docs/install/)):

```bash
allure serve allure-results
```

## Page Object Model

Each page/section of the site is represented by a class encapsulating its locators and actions:

- **`MainPage`** — header search bar, guest selector, filters button, search navigation.
- **`AdultsSection`** — guest counter controls (increment/decrement adults).
- **`FiltersSection`** — filter panel interactions (checkboxes, "see more").

Test files import these classes and compose them into scenarios, keeping locators out of the test logic.

## Fixtures (`conftest.py`)

| Fixture | Scope | Description |
|---|---|---|
| `url` | session | Base URL of the site under test (`https://winwin.travel/`) |
| `browser_context_args` | session | Overrides default Playwright context to use a `1920x1080` viewport |

## Test Coverage

Automated (`tests/`):

- **Max Adults section** — verifies the guest counter increments up to its maximum and disables the "+" button correctly.
- **Active pets checkboxes** — verifies the expected number of filter checkboxes become active after applying the pets filter.
- **Page URL after filters** — verifies applying recommended filters and searching updates the URL with the correct filter query parameters.

Manual (`testcases.txt`):

- Header component test cases (logo redirection, CTA button, navigation icons, register/sign-in modals, responsive layout).

## CI/CD Pipeline

On every push or pull request to `main`/`master`, the [`playwright.yml`](.github/workflows/playwright.yml) workflow:

1. Checks out the repository and sets up Python 3.11.
2. Installs dependencies from `requirements.txt`.
3. Installs Playwright's Chromium browser with system dependencies.
4. Runs the pytest suite, collecting Allure results.
5. Fetches previous Allure history from the `gh-pages` branch (if it exists).
6. Generates a new Allure report (merging in history for trend graphs).
7. Deploys the report to GitHub Pages via the `gh-pages` branch.

## Notes

- The `gh-pages` branch is managed automatically by the workflow — do not edit it manually.
- If a workflow run fails, check the Allure report artifacts and job logs under the **Actions** tab for details.