import allure
import requests
from allure_commons.types import AttachmentType


class AllureSession(requests.Session):

    def __init__(self):
        super().__init__()
        self.request_data = {}

    def send(self, request, **kwargs):
        self.request_data = {
            'method': request.method,
            'url': request.url,
            'headers': dict(request.headers),
            'body': request.body
        }

        response = super().send(request, **kwargs)

        request_text = (
            f"Request Method: {self.request_data.get('method', 'UNKNOWN')}\n"
            f"Request URL: {self.request_data.get('url', 'UNKNOWN')}\n"
            f"Request Headers: {self.request_data.get('headers', {})}\n"
            f"Request Body: {self.request_data.get('body', '')}\n\n"
        )

        response_text = (
            f"Response Status: {response.status_code}\n"
            f"Response Body: {response.text}"
        )

        allure.attach(
            body=request_text,
            name=f"Request: {self.request_data.get('method')} {self.request_data.get('url')}",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            body=response_text,
            name=f"Response: {response.status_code}",
            attachment_type=allure.attachment_type.TEXT
        )

        self.request_data = {}
        return response


def add_video(browser):
    video_url = (
        "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    )
    html = (
        "<html><body><video width='100%' height='100%' controls autoplay><source src='"
        + video_url
        + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html'
    )


def add_logs(browser):
    try:
        log_text = "".join(
            f'{text}\n'
            for text in browser.driver.execute('getLog', {'type': 'browser'})['value']
        )
    except Exception as error:
        log_text = f"{error}\nлоги не доступны."

    allure.attach(log_text, 'browser_logs', AttachmentType.TEXT, '.log')
