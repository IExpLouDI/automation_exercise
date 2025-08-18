def test_add_product_in_cart(setup_remote_browser, application, products_list):
	application.navigation_bar.open_products_page()
	application.products.scroll_page(300)

	for iterate, product in enumerate(products_list):
		if len(products_list) != iterate + 1:
			(application.products
			 .add_wanted_product_in_cart(product.product_id)
			 .press_button_continue_shopping()
			 )
		else:
			(application.products
			 .add_wanted_product_in_cart(product.product_id)
			 .click_view_cart_page()
			 )
	application.cart_page.check_product_in_cart(products_list)
