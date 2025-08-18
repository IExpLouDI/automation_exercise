
def test_verify_subscription_in_home_page(setup_remote_browser, application):
    application.home_page.scroll_down_to_footer()
    (application.footer
     .enter_email('f@ff.tt')
     .press_button()
     )
    application.footer.verify_success_subscribe()
