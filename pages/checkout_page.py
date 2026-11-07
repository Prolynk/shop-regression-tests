class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.error = page.get_by_test_id("error")
        self.confirmation = page.get_by_test_id("complete-header")

    def continue_with(self, first_name="Habeeb", last_name="Tester", postal_code="NE1 1AA"):
        self.page.get_by_test_id("firstName").fill(first_name)
        self.page.get_by_test_id("lastName").fill(last_name)
        self.page.get_by_test_id("postalCode").fill(postal_code)
        self.page.get_by_test_id("continue").click()

    def finish(self):
        self.page.get_by_test_id("finish").click()
