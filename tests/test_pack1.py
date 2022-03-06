from time import sleep
from playwright.sync_api import Page


class TestPack1:

    def test_main_page(self, page: Page):
        page.goto("https://www.saucedemo.com/")
        sleep(1)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        sleep(1)
        # make sure we can see an item on the main page
        assert page.inner_text(
            'xpath=/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div') == "Sauce Labs Backpack"

    def test_nav(self, page: Page):
        page.goto("https://www.saucedemo.com/")
        sleep(1)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        sleep(1)
        page.click("#react-burger-menu-btn")
        page.click("#about_sidebar_link")
        assert page.url == "https://saucelabs.com/"

    def test_shopping_basket(self, page: Page):
        page.goto("https://www.saucedemo.com/")
        sleep(1)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        sleep(1)
        # add an item to the shopping basket
        page.click("#add-to-cart-sauce-labs-backpack")
        # check cart badge updates
        assert page.is_visible("#shopping_cart_container .shopping_cart_badge")
        assert page.inner_text("#shopping_cart_container .shopping_cart_badge") == "1"
        # check item in cart
        page.click("#shopping_cart_container")
        assert page.inner_text("#cart_contents_container .inventory_item_name") == "Sauce Labs Backpack"
        # remove item from cart and check gone
        page.click("#remove-sauce-labs-backpack")
        assert page.is_hidden("#cart_contents_container .inventory_item_name")

    def test_sort(self, page: Page):
        page.goto("https://www.saucedemo.com/")
        sleep(1)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        sleep(1)
        page.click('[data-test="product_sort_container"]')
        # check cheapest item first after sort change
        page.select_option('[data-test="product_sort_container"]', value="lohi")
        assert page.inner_text(
            'xpath=/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div') == "Sauce Labs Onesie"
