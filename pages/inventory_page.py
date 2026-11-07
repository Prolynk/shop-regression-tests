class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.items = page.get_by_test_id("inventory-item")
        self.names = page.get_by_test_id("inventory-item-name")
        self.prices = page.get_by_test_id("inventory-item-price")
        self.badge = page.get_by_test_id("shopping-cart-badge")

    def sort(self, value):
        self.page.get_by_test_id("product-sort-container").select_option(value)

    def add(self, product):
        self.page.get_by_test_id(f"add-to-cart-{product}").click()

    def remove(self, product):
        self.page.get_by_test_id(f"remove-{product}").click()

    def open_cart(self):
        self.page.get_by_test_id("shopping-cart-link").click()

    def logout(self):
        self.page.get_by_role("button", name="Open Menu").click()
        self.page.get_by_test_id("logout-sidebar-link").click()
