import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://akaun.com/")
        await page.goto("https://akaun.com/#/auth/login")
        await page.get_by_label("Email or Mobile Number").click()
        await page.locator("form div").filter(has_text="Email or Mobile Number").nth(4).click()
        await page.get_by_label("Email or Mobile Number").fill("norizzaty+playwright@wavelet.net")
        await page.get_by_label("Password").click()
        await page.get_by_label("Password").fill("Playwright+ERP_2023")
        await page.locator("form").get_by_role("button", name="Sign In").click()
        await page.locator("app-icon").filter(has_text="testingInternal Sales Invoice").get_by_role("img").click()
        await page.get_by_role("button", name="add").click()
        await page.get_by_role("combobox", name="Sales Agent*").locator("span").click()
        await page.get_by_text("Mary").click()
        await page.get_by_text("Account").click()
        await page.get_by_label("Entity Id*").click()
        await page.get_by_text("AUTO-1012").click()
        await page.get_by_role("tab", name="Lines").click()
        await page.get_by_role("tabpanel", name="Lines").get_by_role("button", name="add").click()
        await page.get_by_label("Search...").click()
        await page.get_by_label("Search...").fill("playwright")
        await page.pause()
        await page.get_by_label("Search...").press("Enter")
        await page.get_by_role("gridcell", name="Testing Playwright").first.click()
        await page.get_by_text("PCSUOM").click()
        await page.get_by_text("BOX").click()
        await page.locator("app-pricing-scheme-uom div").filter(has_text="Pricing Scheme").nth(2).click()
        await page.get_by_text("450.00 (EMP_LIST_PRICE)").click()
        await page.get_by_role("button", name="ADD").filter(has_text="ADD").click()
        await page.get_by_role("button", name="CREATE").click()
        await page.get_by_text("1000287").click()
        await page.get_by_text("Lines").click()
        await page.get_by_role("button", name="SAVE").click()
        await page.get_by_role("gridcell", name="Press Space to toggle row selection (unchecked)  1000287").get_by_role("checkbox", name="Press Space to toggle row selection (unchecked)").check()
        await page.get_by_role("button", name="FINAL").click()

    # ---------------------
        await browser.close()

asyncio.run(main())