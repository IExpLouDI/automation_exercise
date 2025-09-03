# Проект по автоматизации Automation Exercise
<p align="center">
<img title="Allure Overview Dashboard" src="resources/readme/home_page.png">
</p>

##  Содержание:

> ➠ [Технологический стек](#технологический-стек)
>
> ➠ [Покрытый функционал](#покрытый-функционал)
>
> ➠ [Сборка в Jenkins](#Jenkins-job)
>
> ➠ [Allure отчет](#Allure-отчет)
> 
> ➠ [AllureTO отчет](#AllureTO-отчет)
> 
> ➠ [Интеграция с Jira](#JIRA-интеграция)
>
> ➠ [Отчет в Telegram](#Telegram-оповещение)
>
> ➠ [Видео примеры прохождения тестов](#Пример-test-ui)

  
## 🧰 <p id="технологический-стек">Технологии и инструменты</p>

<p align="center">
<a href="https://www.jetbrains.com/pycharm/"><img src="resources/readme/icons/pycharm-icon.svg" width="50" height="50"  alt="IDEA"/></a>
<a href="https://github.com/"><img src="resources/readme/icons/github-icon.svg" width="50" height="50"  alt="Github"/></a>
<a href="https://github.com/yashaka/selene"><img src="resources/readme/icons/selene.png" width="50" height="50"  alt="Selene"/></a>
<a href="https://aerokube.com/selenoid/"><img src="resources/readme/icons/Selenoid.svg" width="50" height="50"  alt="Selenoid"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="resources/readme/icons/Allure.svg" width="50" height="50"  alt="Allure"/></a>
<a href="https://www.jenkins.io/"><img src="resources/readme/icons/Jenkins.svg" width="50" height="50"  alt="Jenkins"/></a>
<a href="https://qameta.io/"><img src="resources/readme/icons/Allure_TO.svg" width="50" height="50"  alt="Allure TestOps"/></a>  
<a href="https://www.atlassian.com/ru/software/jira/"><img src="resources/readme/icons/Jira.svg" width="50" height="50"  alt="Jira"/></a>
<a href="https://python-poetry.org"><img src="resources/readme/icons/poetry.svg" width="50" height="50"  alt="Jira"/></a>
</p>

<p>В данном проекте представлены:  </p>

- автотесты API, расположенные в дирректории <code>./tests/test_API</code>;
- автотесты UI, с использованием библиотеки <code>Selene</code>, расположены в  <code>./tests/test_UI</code>.

<p>Для работы с виртуальным окружением и зависимостями, используется <code>Poetry</code></p>

#### UI тесты реализованы паттерном PageObject
>
> <code>Selenoid</code> выполняет запуск браузера в контейнере <code>Docker</code>.
>
> <code>Allure Report/Allure TestOps</code> формируют отчеты о запуске тестов.
>
> <code>Jenkins</code> выполняет запуск тестов.
> После завершения прогона отправляются уведомления с помощью бота в <code>Telegram</code>.

## <p id="покрытый-функционал">Покрытый функционал</p>

> Разработаны автотесты для <code>UI</code> и <code>API</code>.

<h2 align="center"> UI тесты</h2>

- [x] Тестирование регистрации пользователя
- [x] Тестирование авторизации пользователя
- [x] Тестирование добавления товара в корзину
- [x] Тестирование добавления товара в корзину с последующей авторизацией
- [x] Тестирование добавления товара в корзину с последующей регистрацией
- [x] Тестирование оформления заказа
- [x] Тестирование заполнения и отправки формы обратной связи
- [x] Тестирование оформления подписки на главной странице 

<h2 align="center"> API тесты</h2>

- **Тестирование запросов GET**
  - [x] `all_products`
  - [x] `all_brands`
  - [x] `user_account_detail`

- **Тестирование запросов POST**
  - [x] `test_search_product`
  - [x] `verify_login`
  - [x] `create_account`

- **Тестирование запросов DELETE**
  - [x] `userAccount`

### Функционал в разработке
<p>Разрабатываемый функционал - помечен маркером <code>pytest.mark.xfail/skip</code> или <code>pytest.mark.skip</code>
с указанием причины</p>

## <img id="Jenkins-job" src="resources/readme/icons/Jenkins.svg" width="25" height="25"  alt="Jenkins"/></a> Jenkins <a target="_blank" href="https://jenkins.autotests.cloud/job/Johnnie_Walker_UI_tests/"> job </a>
<p align="center">
<a href="https://jenkins.autotests.cloud/job/suchkov_vs_grade_project/"><img src="resources/readme/jenkins_job.png" alt="Jenkins"/></a>
</p>

# Примеры использования

###  Основной Allure отчет
<p align="center">
<img id="Allure-отчет" title="Allure Overview Dashboard" src="resources/readme/allure-report.png">
</p>


### Тесты 
<p align="center">
<img title="Allure Tests" src="resources/readme/allure-tests.png">
</p>

## <img id="AllureTO-отчет" src="resources/readme/icons/Allure_TO.svg" width="25" height="25"  alt="Allure"/></a> Отчет в <a target="_blank" href="https://allure.autotests.cloud/launch/48029">Allure TestOps</a>
<p align="center">
<img title="Allure Overview Dashboard" src="resources/readme/test_ops.png">
</p>

## <img id="JIRA-интеграция" src="resources/readme/icons/Jira.svg" width="25" height="25"  alt="Allure"/></a> Интеграция с <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1492">Jira</a>
<p align="center">
<img title="Allure Overview Dashboard" src="resources/readme/JIRA.png">
</p>

## <img id="Telegram-оповещение" src="resources/readme/icons/Telegram.svg" width="25" height="25"  alt="Allure"/></a> Уведомление в Telegram при помощи бота
> После завершения сборки специальный бот, созданный в <code>Telegram</code>, автоматически обрабатывает и отправляет сообщение с отчетом о прогоне.

<p align="center">
<img title="Allure Overview Dashboard" src="resources/readme/telegram.png" >
</p>

## Пример запуска тестов в Selenoid
### <img id="Пример-test-ui" src="resources/readme/icons/Selenoid.svg" width="25" height="25" alt="Jenkins"/>Добавление товара в корзину с последующей регистрацией
<p align="center">
<img title="Local launch example" src="resources/readme/gif/ui_autotest.gif">
</p>
