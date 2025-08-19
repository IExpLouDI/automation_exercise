def test_verify_product_page_and_product_detail_page(setup_remote_browser, application):
	application.navigation_bar.products()
	application.products.verify_open_products_page()
	application.products.scroll_page(100)
	application.products.open_product_deatail()
	application.products.verify_product_detail_is_open()
	application.products.check_product_detail_is_visible()


def test_search_product(setup_remote_browser, application):
	application.navigation_bar.open_products_page()
	application.products.search_product('Tshirt')
	application.products.verify_searched_products_is_visible()
	application.products.verify_all_products_are_visible()
