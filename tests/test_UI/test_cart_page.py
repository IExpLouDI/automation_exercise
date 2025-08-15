def test_add_product_in_cart(setup_browser, application):
    application.navigation_bar.products()
    application.products.scroll_page(300)
    application.products.add_wanted_product_in_cart(1)
