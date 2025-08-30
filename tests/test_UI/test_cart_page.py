from allure import step


def test_add_product_in_cart_from_product_page(setup_remote_browser, application, products_list):
	with step(f'Открываем вкладку продуктов и делаем скролл вниз'):
		application.navigation_bar.open_products_page()
		application.products.scroll_page(300)

	with step('Добавляем товары в корзину'):
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
	with step('Выполняем проверку содержимого корзины'):
		application.cart_page.check_product_in_cart(products_list)


def test_verify_product_quantity_in_cart(setup_remote_browser, application, products_list):
	test_product = products_list[0]
	test_product.set_quantity(4)

	with step(f'Делаем скролл вниз до появления товаров и переходим в карточку товара - {test_product.name}'):
		(application.home_page
		 .scroll_page(500)
		 .click_view_product(test_product.product_id)
		 )
	with step('Проверяем наполнение карточки товара'):
		application.product_detail_page.check_product_detail(test_product)

	with step(f'Устанавливаем количество товара - {test_product.quantity}'):
		application.product_detail_page.set_product_quantity(test_product.quantity)
		application.product_detail_page.press_button_add_to_cart()

	application.products.press_button_continue_shopping()

	with step('Открываем корзину и проверяем добавленный товар'):
		application.navigation_bar.open_cart_page()
		application.cart_page.check_product_in_cart([test_product])


def test_remove_products_from_cart(setup_remote_browser, application, create_user_account, products_list):
	with step('Авторизация и переход на страницу с товарами'):
		application.navigation_bar.open_login_page()
		application.signup_login_page.type_email(create_user_account["email"], is_login=True)
		application.signup_login_page.type_password(create_user_account['password'])
		application.signup_login_page.pres_button_login()

		application.navigation_bar.open_products_page()

	with step('Добавляем товары в корзину'):
		application.stable_elements.scroll_page(500)
		for product in products_list:
			application.products.add_wanted_product_in_cart(product.product_id)
			application.products.press_button_continue_shopping()

	with step('Переходим в корзину и очищаем от содержимого'):
		application.navigation_bar.open_cart_page()
		application.cart_page.check_product_in_cart(products_list)
		application.cart_page.clear_cart(products_list)
