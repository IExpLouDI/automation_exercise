def test_verify_product_page_and_product_detail_page(setup_browser, application):
	application.navigation_bar.products()
	application.products.verify_open_products_page()
	application.products.scroll_page(100)
	application.products.open_product_deatail()
	application.products.verify_product_detail_is_open()
	application.products.check_product_detail_is_visible()


def test_search_product(setup_browser, application):
	application.navigation_bar.open_products_page()
	application.products.verify_open_products_page()
	pass
