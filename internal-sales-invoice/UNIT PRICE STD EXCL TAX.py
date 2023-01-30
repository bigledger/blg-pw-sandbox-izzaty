from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.async_api import async_playwright
import time
import asyncio


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://akaun.com/")
    await page.goto("https://akaun.com/#/auth/login")
    await page.get_by_label("Email or Mobile Number").click()
    await page.get_by_label("Email or Mobile Number").fill("norizzaty+playwright@wavelet.net")
    await page.get_by_label("Email or Mobile Number").press("Tab")
    await page.get_by_label("Password").click()
    await page.get_by_label("Password").fill("Playwright+ERP_2023")
    await page.locator("form").get_by_role("button", name="Sign In").click()
    await page.locator("app-icon").filter(has_text="testingInternal Sales Invoice").get_by_role("img").click()
    await page.goto("https://akaun.com/#/applet/tnt/wavelet/erp/internal-sales-invoice-applet/sales-invoice")
    await page.get_by_role("button", name="add").click()
    await page.get_by_role("combobox", name="Branch B Company (Branch 1) | B Company Sdn Bhd").locator("div").nth(2).click()
    await page.get_by_text("B COMPANY (WAREHOUSE 1) | B COMPANY (WAREHOUSE 1)").click()
    await page.get_by_role("combobox", name="Sales Agent*").locator("div").nth(3).click()
    await page.get_by_text("Rose").click()
    await page.get_by_text("Account").click()
    await page.locator(".ng-star-inserted > .mat-form-field > .mat-form-field-wrapper > .mat-form-field-flex > .mat-form-field-infix").first.click()
    await page.locator("span").filter(has_text="1000218").first.click()
    await page.get_by_role("cell", name="add Select Customer Select Mode ' Search... Rows 10 page 1 of 2 view Code Type Name Contact Number Code Filter Input Type Filter Input Name Filter Input Contact Number Filter Input Press SPACE to deselect this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Press SPACE to select this row. Columns Filters").get_by_role("button", name="add").click()
    await page.get_by_text("Lines").click()
    await page.get_by_role("tabpanel", name="Lines").get_by_role("button", name="add").click()
    await page.get_by_label("Search...").click()
    await page.get_by_label("Search...").fill("play")
    await page.get_by_label("Search...").press("Enter")
    await page.get_by_role("gridcell", name="Testing Playwright").first.click()
    await page.get_by_role("combobox", name="Pricing Scheme").locator("div").nth(3).click()
    await page.get_by_text("40.00 (EMP_LIST_PRICE)").click()
    await page.get_by_role("button", name="ADD").filter(has_text="ADD").click()
    await page.locator("div:nth-child(3) > .mat-tab-header-pagination-chevron").click()
    await page.locator("div:nth-child(3) > .mat-tab-header-pagination-chevron").click()
    await page.get_by_role("tabpanel", name="Lines").get_by_role("button", name="view").click()
    await page.locator("div:nth-child(3) > .mat-tab-header-pagination-chevron").click()
    await page.get_by_role("button", name="CREATE").click()

    # a = True
    # while a == True :
    #     input_user = input("Enter Invoice Number : ")
    #     a = False
    #     break

    async def input_user(loop):
        input_user = input("Enter Invoice Number : ")
        print(f"input_user :" + input_user)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(input_user(loop))
    loop.close()

    invoice_number = "Press Space to toggle row selection (unchecked)  "+ input_user
    await page.get_by_role("gridcell", name=invoice_number).get_by_role("checkbox", name="Press Space to toggle row selection (unchecked)").check()
    await page.get_by_role("button", name="FINAL").click()

    # ---------------------
    context.close()
    browser.close()


with async_playwright() as playwright:
    run(playwright)
