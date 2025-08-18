def test_add_product_in_cart(setup_remote_browser, application):
	application.navigation_bar.open_products_page()
	application.products.scroll_page(300)
	application.products.add_wanted_product_in_cart(1)
	application.products.press_button_continue_shopping()
	application.products.add_wanted_product_in_cart(2)
	application.products.click_view_cart_page()
