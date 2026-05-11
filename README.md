# Autodesk-QA-Automation
Modular Python/PyTest framework for automated API and UI validation of simulation workflows
**Developer:** Paskalina Mashimba

## Project Overview
This repository contains a modular automation framework built to validate backend and UI workflows. While designed as a standalone project, the architecture is optimized for complex simulation environments like **Autodesk Fusion**.

## Technical Accomplishments
- **Modular Architecture:** Organized into `tests`, `utils`, and `pages` for high maintainability.
- **Page Object Model (POM):** Implemented a scalable POM structure to decouple test logic from UI elements.
- **API Stability Testing:** Developed a custom `SimulationAPI` class to validate backend service reachability and performance.
- **CI/CD Integration:** Ready for GitHub Actions to ensure 100% build reliability on every push.

## Technical Stack
- **Language:** Python 3.13
- **Testing Engine:** PyTest
- **Libraries:** Requests (API Validation)
