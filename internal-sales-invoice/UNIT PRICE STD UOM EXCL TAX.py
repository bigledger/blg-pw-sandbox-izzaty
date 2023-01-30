from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://akaun.com/")
    page.goto("https://akaun.com/#/auth/login")
    page.get_by_label("Email or Mobile Number").click()
    page.locator("form div").filter(has_text="Email or Mobile Number").nth(4).click()
    page.get_by_label("Email or Mobile Number").fill("norizzaty+playwright@wavelet.net")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Playwright+ERP_2023")
    page.locator("form").get_by_role("button", name="Sign In").click()
    page.locator("app-icon").filter(has_text="testingInternal Sales Invoice").get_by_role("img").click()
    page.get_by_role("button", name="add").click()
    page.get_by_role("combobox", name="Sales Agent*").locator("span").click()
    page.get_by_text("Mary").click()
    page.get_by_text("Account").click()
    page.get_by_label("Entity Id*").click()
    page.get_by_text("AUTO-1012").click()
    page.get_by_role("tab", name="Lines").click()
    page.get_by_role("tabpanel", name="Lines").get_by_role("button", name="add").click()
    page.get_by_label("Search...").click()
    page.get_by_label("Search...").fill("playwright")
    page.get_by_label("Search...").press("Enter")
    page.get_by_role("gridcell", name="Testing Playwright").first.click()
    page.get_by_text("PCSUOM").click()
    page.get_by_text("BOX").click()
    page.locator("app-pricing-scheme-uom div").filter(has_text="Pricing Scheme").nth(2).click()
    page.get_by_text("450.00 (EMP_LIST_PRICE)").click()
    page.get_by_role("button", name="ADD").filter(has_text="ADD").click()
    page.get_by_role("button", name="CREATE").click()
    page.get_by_text("1000287").click()
    page.get_by_text("Lines").click()
    page.get_by_role("button", name="SAVE").click()
    page.get_by_role("gridcell", name="Press Space to toggle row selection (unchecked)  1000287").get_by_role("checkbox", name="Press Space to toggle row selection (unchecked)").check()
    page.get_by_role("button", name="FINAL").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
