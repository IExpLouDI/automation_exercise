# Демо проект по автоматизации Automation Exercise
<p align="center">
<img title="Allure Overview Dashboard" src="resources/readme/home_page.png">
</p>

##  Содержание:

> ➠ [Технологический стек](#classical_building-технологический-стек)
>
> ➠ [Покрытый функционал](#earth_africa-покрытый-функционал)
>
> ➠ [Сборка в Jenkins](#earth_africa-Jenkins-job)
>
> ➠ [Allure отчет](#earth_africa-Allure-отчет)
> 
> ➠ [Интеграция с Jira](#earth_africa-Allure-отчет)
>
> ➠ [Отчет в Telegram](#earth_africa-Уведомление-в-Telegram-при-помощи-бота)
>
> ➠ [Видео примеры прохождения тестов](#earth_africa-Примеры-видео-о-прохождении-тестов)

  
## 🧰 Технологии и инструменты

<p align="center">
<a href="https://www.jetbrains.com/pycharm/"><img src="resources/readme/icons/pycharm-icon.svg" width="50" height="50"  alt="IDEA"/></a>
<a href="https://github.com/"><img src="resources/readme/icons/github-icon.svg" width="50" height="50"  alt="Github"/></a>
<a href="https://github.com/yashaka/selene"><img src="resources/readme/icons/selene.png" width="50" height="50"  alt="Selene"/></a>
<a href="https://aerokube.com/selenoid/"><img src="resources/readme/icons/Selenoid.svg" width="50" height="50"  alt="Selenoid"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="resources/readme/icons/Allure.svg" width="50" height="50"  alt="Allure"/></a>
<a href="https://www.jenkins.io/"><img src="resources/readme/icons/Jenkins.svg" width="50" height="50"  alt="Jenkins"/></a>
<a href="https://qameta.io/"><img src="resources/readme/icons/Allure_TO.svg" width="50" height="50"  alt="Allure TestOps"/></a>  
<a href="https://www.atlassian.com/ru/software/jira/"><img src="resources/readme/icons/Jira.svg" width="50" height="50"  alt="Jira"/></a>  
</p>
В данном проекте представлены:  

- автотесты API, расположенные в дирректории <code>./tests/test_API</code>;
- автотесты UI, с использованием библиотеки <code>Selene</code>, расположены в  <code>./tests/test_UI</code>.

#### UI тесты реализованы паттерном PageObject
>
> <code>Selenoid</code> выполняет запуск браузера в контейнере <code>Docker</code>.
>
> <code>Allure Report/Allure TestOps</code> формируют отчеты о запуске тестов.
>
> <code>Jenkins</code> выполняет запуск тестов.
> После завершения прогона отправляются уведомления с помощью бота в <code>Telegram</code>.

## Покрытый функционал

> Автотесты для <code>UI</code> и <code>API</code>.
### UI
- [x] Тестирование регистрации пользователя
- [x] Тестирование авторизации пользователя
- [x] Тестирование добавления товара в корзину
- [x] Тестирование добавления товара в корзину с последующей авторизацией
- [x] Тестирование добавления товара в корзину с последующей регистрацией
- [x] Тестирование оформления заказа
- [x] Тестирование заполнения и отправки формы обратной связи
- [x] Тестирование оформления подписки на главной странице 

### API
- [x] Тестирование запросов GET (all_products, all_brands, user_account_detail)
- [x] Тестирование запросов POST (test_search_product, verify_login, create_account)
- [x] Тестирование запросов DELETE (userAccount)

### Функционал в разработке помечен маркерами <code>pytest.mark.xfail/skip</code>

## <img src="resources/readme/icons/Jenkins.svg" width="25" height="25"  alt="Jenkins"/></a> Jenkins <a target="_blank" href="https://jenkins.autotests.cloud/job/Johnnie_Walker_UI_tests/"> job </a>
<p align="center">
<a href="https://jenkins.autotests.cloud/job/suchkov_vs_grade_project/"><img src="resources/readme/jenkins_job.png" alt="Jenkins"/></a>
</p>

# Примеры использования

###  Основной отчет
<p align="center">
<img title="Allure Overview Dashboard" src="resources/readme/allure-report.png">
</p>


### Тесты 
<p align="center">
<img title="Allure Tests" src="resources/readme/tests.png">
</p>

## <img src="resources/readme/icons/Allure_TO.svg" width="25" height="25"  alt="Allure"/></a> Отчет в <a target="_blank" href="https://allure.autotests.cloud/launch/48029">Allure TestOps</a>
<p align="center">
<img title="Allure Overview Dashboard" src="resources/readme/test_ops.png">
</p>

## <img src="resources/readme/icons/Jira.svg" width="25" height="25"  alt="Allure"/></a> Интеграция с <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1492">Jira</a>
<p align="center">
<img title="Allure Overview Dashboard" src="resources/readme/JIRA.png">
</p>

## <img src="resources/readme/icons/Telegram.svg" width="25" height="25"  alt="Allure"/></a> Уведомление в Telegram при помощи бота
> После завершения сборки специальный бот, созданный в <code>Telegram</code>, автоматически обрабатывает и отправляет сообщение с отчетом о прогоне.

<p align="center">
<img title="Allure Overview Dashboard" src="resources/readme/telegram.png" >
</p>

## Пример запуска тестов в Selenoid
### <img src="resources/readme/icons/Selenoid.svg" width="25" height="25" alt="Jenkins"/>Добавление товара в корзину с последующей регистрацией
<p align="center">
<img title="Local launch example" src="resources/readme/gif/ui_autotest.gif">
</p>
