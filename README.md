# Captcha Handling Snippet (Death By Captcha)

This repository demonstrates how to integrate Death by Captcha with Selenium to solve CAPTCHAs in an automated browser session.

**⚠️ FOR STUDY PURPOSES ONLY! I DO NOT RECOMMEND TO USE THIS TO VIOLATE ANY TERMS OF USE OR EVEN ILLEGAL ACTIVITIES! ⚠️**

## Setup

1. Install required libraries:
   ```
   pip install selenium deathbycaptcha
   ```

2. Set up environment variables:
   - `DEATHBYCAPTCHA_USER`: Your Death by Captcha username.
   - `DEATHBYCAPTCHA_PASSWORD`: Your Death by Captcha password.

## Usage

- The script `captcha_solver.py` demonstrates how to:
  - Extract the reCAPTCHA site key.
  - Solve the CAPTCHA using Death by Captcha.
  - Inject the CAPTCHA response into the webpage.
