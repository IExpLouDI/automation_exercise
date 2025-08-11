def test_contact_us_form(setup_browser, application, create_account):
    application.navigation_bar.open_contact_us_page()
    application.contact_us_page.verify_page_is_open()
    (application.contact_us_page
     .type_user_name(create_account['nick_name'])
     .type_user_email(create_account['email'])
     .type_mail_subject('Test')
     .type_message('lorem')
     .upload_user_file('/Users/vssuchkov/PycharmProjects/automation_exercise/resources/images/cat.jpeg')
     .press_submit_button()
     )