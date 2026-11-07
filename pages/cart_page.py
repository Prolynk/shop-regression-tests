class CartPage:
    def __init__(self, page):
        self.page = page
        self.items = page.get_by_test_id("inventory-item")
        self.names = page.get_by_test_id("inventory-item-name")

    def checkout(self):
        self.page.get_by_test_id("checkout").click()
