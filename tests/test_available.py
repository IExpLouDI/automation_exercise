from selene import browser, be
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from dotenv import load_dotenv
import os


def test_available():
    browser.element("h2.title").should(be.present)
