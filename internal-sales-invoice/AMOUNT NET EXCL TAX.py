from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://akaun.com/")
    page.goto("https://akaun.com/#/auth/login")
    page.get_by_label("Email or Mobile Number").click()
    page.get_by_label("Email or Mobile Number").fill("norizzaty+playwright@wavelet.net")
    page.get_by_label("Email or Mobile Number").press("Tab")
    page.get_by_label("Password").fill("Playwright+ERP_2023")
    page.locator("form").get_by_role("button", name="Sign In").click()
    page.locator("app-icon").filter(has_text="testingInternal Sales Invoice").get_by_role("img").click()
    page.get_by_role("button", name="add").click()
    page.get_by_text("B Company (Branch 1) | B Company Sdn Bhd").click()
    page.get_by_text("B COMPANY (WAREHOUSE 1) | B COMPANY (WAREHOUSE 1)").click()
    page.get_by_role("combobox", name="Sales Agent*").locator("span").click()
    page.get_by_text("Joyce").click()
    page.get_by_text("Account").click()
    page.locator(".ng-star-inserted > .mat-form-field > .mat-form-field-wrapper > .mat-form-field-flex > .mat-form-field-infix").first.click()
    page.get_by_text("1000218").click()
    page.get_by_role("cell", name="add Select Customer Select Mode ' Search... Rows 10 page 1 of 2 view Code Type Name Contact Number Code Filter Input Type Filter Input Name Filter Input Contact Number Filter Input Press SPACE to deselect this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Columns Filters").get_by_role("button", name="add").click()
    page.get_by_text("Lines").click()
    page.get_by_role("tabpanel", name="Lines").get_by_role("button", name="add").click()
    page.get_by_label("Search...").click()
    page.get_by_label("Search...").fill("play")
    page.get_by_label("Search...").press("Enter")
    page.get_by_role("gridcell", name="Testing Playwright").first.click()
    page.get_by_role("combobox", name="Pricing Scheme").locator("span").click()
    page.get_by_text("10.00 (EMP_LIST_PRICE)").click()
    page.get_by_label("Amount Net (Exclusive of tax)").click()
    page.get_by_label("Amount Net (Exclusive of tax)").fill("8")
    page.get_by_role("button", name="ADD").filter(has_text="ADD").click()
    page.get_by_role("button", name="CREATE").click()
    page.get_by_role("gridcell", name="Press Space to toggle row selection (unchecked)  1000281").get_by_role("checkbox", name="Press Space to toggle row selection (unchecked)").check()
    page.get_by_role("button", name="FINAL").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
