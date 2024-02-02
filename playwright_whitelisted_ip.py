# you can whitelist your IP in the dashboard
from playwright.sync_api import sync_playwright


def run(playwright):
    browser_type = (
        playwright.chromium
    )  # Choose your browser: chromium, firefox, or whatever you prefer
    proxy_server = "213.178.141.197:46007"  # Our proxy server

    # Launch the browser with the proxy configuration
    browser = browser_type.launch(
        headless=False,
        proxy={
            "server": f"http://{proxy_server}",
        },
    )

    page = browser.new_page()
    # navigate to the target page (in the real one you will use way more logic, but this is just a set up example)
    page.goto("https://ipv4.icanhazip.com")

    page.wait_for_timeout(5000)
    print(page.text_content("body"))

    # Close the browser
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
