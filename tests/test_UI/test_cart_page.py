from selene import have


def test_add_product_in_cart(setup_remote_browser, application):
	application.navigation_bar.open_products_page()
	application.products.scroll_page(300)
	application.products.add_wanted_product_in_cart(1)
	application.products.press_button_continue_shopping()
	application.products.add_wanted_product_in_cart(2)
	application.products.click_view_cart_page()
	setup_remote_browser.all('.cart_description p').should(have.size(2))
	setup_remote_browser.all('td p').should(have.exact_texts(['Women > Tops', 'Rs. 500', 'Rs. 500',
															  'Men > Tshirts', 'Rs. 400', 'Rs. 400']))

