<a name="Вернуться в начало"></a>

<div align="center">

  <h3>Лабораторные работы команды "Неповторимая четверка"</h3>
  <h4>по дисциплине: "Облачные технологии и услуги"</h4>

```
    Состав команды:
    
    Королева Анастасия
    Горлов Андрей
    Соколова Дарья
    Драчева Елена
```

</div>


<details>
  <summary> Навигация </summary>
  <ol>
    <li>
      <a href="#DEVOPS ЛАБЫ">DEVOPS ЛАБЫ</a>
      <ul>
        <li><a href="#Лабораторная 1">Лабораторная 1</a></li>
        <li><a href="#Лабораторная 1* (со звездочкой)">Лабораторная 1* (со звездочкой)</a></li>
        <li><a href="#Лабораторная 2">Лабораторная 2</a></li>
        <li><a href="#Лабораторная 3">Лабораторная 3</a></li>
      </ul>
    </li>
    <li>
      <a href="#АНАЛИТИЧЕСКИЕ ЛАБЫ">АНАЛИТИЧЕСКИЕ ЛАБЫ</a>
      <ul>
        <li><a href="#AWS">AWS</a></li>
        <li><a href="#Azure">Azure</a></li>
      </ul>
    </li>
  </ol>
</details>

<a name="DEVOPS ЛАБЫ"></a>
# DEVOPS ЛАБЫ

<a name="Лабораторная 1"></a>
## Лабораторная 1

```
Пользуясь терминалом на компьютере А перенести файл с компьютера Б на компьютер С,
находящиеся в одной локальной сети.

Понадобится ssh. Просьба использовать MacOS/Linux/WSL.
```

Перед началом выполнения лабораторной работы был изучен **теоретический материал**, необходимый для данной ЛР. 

Для ее выполнения понадобилось:
_**scp (Secure CoPy)** — утилита для безопасного копирования данных между Linux-системами по протоколу SSH. Она входит в состав OpenSSH, поэтому для работы с утилитой не нужно устанавливать дополнительное ПО._

---

1. Убедились, что SSH сервер запущен и настроен (на некоторых ноутбуках пришлось настроить, изменив настройки общего доступа - MacOS).
2. Применили команду **scp**, чтобы перенести скопировать файл с одного компьютера, а затем перенести на другой. Пример команды выглядит следующим образом:
   
   ```
      scp путь/к/файлу/на/компьютере/Б имя_пользователя@IP_компьютера_Б:/путь/назначения/на/компьютере/С
   ```
В данном случае файл переносится с устройста Б на устройство С (с устройства А)

---

**Выполнение работы:**

P.S. Для более краткого изложения в отчете используются имена - Лена, Настя, Даша (имя устройств). Важно также отметить, что все на MacOS.

Нам понадобятся имена пользователей (логины), пароли, а тажке IP. Первые две характеристики известны владельцу каждого устройста, IP же найдем через команды - **_ifconfig | grep "inet " | grep -v 127.0.0.1_** или **_ifconfig_**

1. Для начала убедились, что соединение выполняется успешно. Затем с устройста Даши перенесли картинку на устройство Насти (пользуясь терминалом Лены):
   
   ![photo_2023-09-15_14-26-24 (2)](https://github.com/luckyapin/clouds/assets/87613601/3efc3e24-7b88-490b-b799-ab1f08d3aa16)


2. С устройства Даши на устройство Лены (пользуясь терминалом Насти):
   
   ![photo_2023-09-15_14-30-21](https://github.com/luckyapin/clouds/assets/87613601/67cf3dd4-e467-4a36-8a9e-b53e8f63abd0)

3. Также в качестве эксперимента скинули файл с Настиного устройста на Дашино (еще проще, чем п.1 и п.2), терминал Насти:

   ![image](https://github.com/luckyapin/clouds/assets/87613601/e39a0482-04d2-4b44-b6b6-f6566814fe58)

<a name="Лабораторная 1* (со звездочкой)"></a>
## Лабораторная 1* (со звездочкой)

```
Дополнить лабораторную работу 1, использовать публичные и приватные ключи (не логин и пароль)
```

Дополним работу 1...

Для выполнения данного задания использованы новые **команды:**

``` ssh-keygen ``` - используется для создания пары SSH-ключей, которая состоит из приватного и публичного ключей. SSH-ключи представляют собой безопасный способ аутентификации при подключении к удаленному серверу через протокол SSH

``` ssh-copy-id ``` - используется для упрощения процесса копирования публичного ключа

---
**Выполнение работы:**

1. Для начала были созданы ключи с помощью команды, описанной выше

![image](https://github.com/luckyapin/clouds/assets/87613601/0ac3ea55-1516-4153-affc-4aaf181ae7ad)

2. Далее скопировали ключи на другое устройство. На другое также по аналогии. Необходимо было ввести пароль. Но если
протестировать, то видно, что ввод пароля уже не требуется, так как у каждого устройства сохранены ключи. Можно
проверить доступ, перекидывая файлы по аналогии, как в [лабораторной работе 1](https://github.com/luckyapin/clouds/edit/main/README.md#лабораторная-1)

![image](https://github.com/luckyapin/clouds/assets/87613601/af821bea-422d-4614-af92-ec958e83956a)

![image](https://github.com/luckyapin/clouds/assets/87613601/cc2e1ebf-ae4b-4f5a-bfb7-c2483b1c8746)


<a name="Лабораторная 2"></a>
## Лабораторная 2
```
Написать два Dockerfile – плохой и хороший. Плохой должен запускаться и работать корректно, но
в нём должно быть не менее 3 “bad practices”. В хорошем Dockerfile они должны быть исправлены.
В Readme описать все плохие практики из кода Dockerfile и почему они плохие, как они были исправлены
в хорошем  Dockerfile, а также две плохие практики по использованию этого контейнера.
```

Было решено обернуть в docker-контейнер [телеграм-бот](https://github.com/luckyapin/clouds/blob/main/lab2/tgbot.py), написанный на языке python. 
Были созданы файлы dockerfile: [плохой](https://github.com/luckyapin/clouds/blob/main/lab2/dockerfileBad) и [хороший](https://github.com/luckyapin/clouds/blob/main/lab2/dockerfileGood), в котором были описаны инструкции для Docker-a.

Основные команды, которые были использованы:   
```FROM python``` - берем образ питона   
```WORKDIR``` - обозначаем корневую директорию   
```RUN``` - устанавливаем и обновляем пакеты, необходимые для нашего образа   
```COPY``` - копируем файлы с компьютера, который запускает сборку, внутрь образа    
```CMD/ENTRYPOINT``` - обращаемся к питону и запускаем файл     

---
**Выполнение работы:**     

### Плохой Dockerfile

1. Использование образа ```python:latest``` без указания версии. Это может привести к несовместимостям и непредсказуемым результатам.
<p align='center'>
<img width='600px' src="https://github.com/luckyapin/clouds/assets/112976450/354ebef2-d2d4-4693-baa9-19bd1d7fb7c7">
</p>


2. Множественные ```run``` (в нашем случае, 2) создают 2 слоя в docker-образе. Это может привести к увеличению сложности и трудностям в управлении контейнерами и неправильной изоляции компонентов.
<p align='center'>
<img width='600px' src="https://github.com/luckyapin/clouds/assets/112976450/82b6696d-30b3-4895-80ef-acab3b0ac0e4">
</p>

3. Использование ```CMD``` для запуска приложения. Так пользователи могут переопределять исполняемый файл.
<p align='center'>
<img width='600px' src="https://github.com/luckyapin/clouds/assets/112976450/b09ea261-aade-42e9-8f37-09250d8ce2db">
</p>

### Хороший Dockerfile


1. Указание конкретной версии образа ```python```. Это обеспечивает стабильность и повторяемость сборки.   
<p align='center'>
<img width='600px' src="https://github.com/luckyapin/clouds/assets/112976450/551484a2-9dc1-4df2-a6bd-07fd349fc6c5">
</p>

2. Использование одной ```run``` команды облегчает управление контейнерами, обеспечивает лучшую изоляцию и эффективное использование ресурсов.  
<p align='center'>
<img width='600px' src="https://github.com/luckyapin/clouds/assets/112976450/f6db1f69-dbed-4b4f-88f1-287e2836a599">
</p>

3. Использование ```ENTRYPOINT``` для запуска приложения - позволяет установить исполняемый файл по умолчанию и передавать аргументы. Так пользователь образа не сможет переопределить поведение приложения в контейнере.     
<p align='center'>
<img width='600px' src="https://github.com/luckyapin/clouds/assets/112976450/9be004b9-19e5-4b80-9448-724b9e2d7bb3">
</p>


### Запуск контейнера


Приложение в Docker-е:
<p align='center'>
<img width='600px' src="https://github.com/luckyapin/clouds/assets/112976450/075dfe06-f593-4dac-a4b2-3973b38968c7">
</p>       

Запускаем контейнер командой ```docker build -t cloudbot .```  
<p align='center'>
<img width='600px' src="https://github.com/luckyapin/clouds/assets/112976450/d4faeefe-72eb-4634-9aff-4ac92456b518">
</p>     

... и получаем рабочий телеграм-бот.
<p align='center'>
<img width='300px' src="https://github.com/luckyapin/clouds/assets/112976450/b9bdef09-b58c-4166-88cc-8a2ceb07e495">
</p>


### Плохие практики по использованию этого контейнера   
1. **Игнорирование обновлений и безопасности.** Отсутствие регулярных обновлений базовых образов и компонентов внутри контейнеров может привести к использованию устаревших и уязвимых версий.
2. **Огромные и неподдерживаемые образы.** Создание образов, включающие в себя большое количество неиспользуемых файлов или зависимостей. Это увеличивает их размер, замедляет развертывание и увеличивает потребление ресурсов.

<a name="Лабораторная 3"></a>

## Лабораторная 3
```
Сделать, чтобы после пуша в ваш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь.
(например, если результат - текстовый файлик, он должен автоматически сохраниться на локальную машину, в ваш репозиторий или на ваш сервер). 
```
Было решено создать новый репозиторий для тестирования [репозиторий](https://github.com/luckyapin/docker_lab3/)
Для загрузки взят проект из предыдущей оабораторной[проект](https://github.com/luckyapin/docker_lab3/blob/main/dockerfile)
Итоговый контейнер выгружается на docker hub[docker hub](https://hub.docker.com/repository/docker/luckyapin/docker_lab3/general)

Основные команды, которые были использованы:   
```name``` - навзание шага в github actions
```uses``` - с помощью какой библиотеки выполняется шаг
```with``` - доп данные


---
**Выполнение работы:** 
Для начала создаем репозиторий.
Добавляем в проект новый github_actions, создаем .github/workflows/publish.yml

![image](https://github.com/luckyapin/clouds/assets/63948716/c9bd39ba-0025-4551-8ff6-438511d8d72a)

В нем пишем данный код, в tags нужно написать путь к своему репозиторию

![image](https://github.com/luckyapin/clouds/assets/63948716/922dc972-79d6-4a6b-a9e2-9e9000ff4c9f)

Позже добавляем в репозиторий секретные ключи settings/Secrets and variables/Actions/New repository secret:

![image](https://github.com/luckyapin/clouds/assets/63948716/3702ac28-61db-4ecf-8f5c-30089f2ff426)


В поле name пишем DOCKER_LOGIN, а в поле secret пишем логин от docker hub

Далее создаем секретный ключ в docker hub, нажимаем account settings/security/new acces token
![image](https://github.com/luckyapin/clouds/assets/63948716/fc83b3fa-7a16-43c3-8761-93f2308febc8)

Создаем ключ и копируем его

В репозитории на гитхаб добавляем еще один ключ с названием DOCKER_PASSWORD и в secret вставляем сгенерированный ключ

Далее добавялем необходимый код в репозиторий 
![image](https://github.com/luckyapin/clouds/assets/63948716/6acf6700-3e31-4e4f-8835-7480ce2ef22a)

И пушим на гитхаб

Нажимаем actions и проверяем все ли сработало

![image](https://github.com/luckyapin/clouds/assets/63948716/355ec27d-eac0-40c8-be1f-b084176f3709)

Далее проверяем на docker hub

![image](https://github.com/luckyapin/clouds/assets/63948716/3dfffc4e-6ce2-42bc-84af-caf5f7685568)

Все готово, можно теперь писать код и пушить, все сработает автоматически

ОТВЕТ НА ДОП ВОПРОС: когда вы запускаете ваш ci cd код, на каком устройстве происходит сборка кода?

У нас сборка происходит через github actions и поэтому сборка кода происходит на серверах Github.

В документации github actions написано, что github предоставляет виртуальные машины для сборки кода, но можно и настроить свои, мы этого не делали, поэтому мы использовали для нашей сборки сервера Github.
![image](https://github.com/luckyapin/clouds/assets/63948716/482532fc-5a47-4973-b8d6-3b250ae9d4e1)

Источник: https://docs.github.com/ru/actions/learn-github-actions/understanding-github-actions

<a name="АНАЛИТИЧЕСКИЕ ЛАБЫ"></a>
# АНАЛИТИЧЕСКИЕ ЛАБЫ

<a name="AWS"></a>
## AWS

### Цель работы:

```
Знакомство с облачными сервисами. Понимание уровней абстракции над инфраструктурой в облаке. Формирование понимания типов потребления сервисов в сервисной-модели. Сопоставление сервисов между разными провайдерами. Оценка возможностей миграции на отечественные сервисы.
```

### Дано:

```
Слепок данных биллинга от провайдера после небольшой обработки в виде SQL-параметров. Необходимо заполнить пустые ячейки с заголовками IT Tower, Service Family, Service Type, Service Sub-Type, используя элементы модели Apptio TBM Unified Model (ATUM) для упрощения соответствия сервисов. Определить соответствие каждого сервиса международного провайдера русскому сервису.
```

### Ход работы:

**Описание Apptio TBM Unified Model**

**Apptio TBM Unified Model (ATUM)** — это стандартизированная модель для категоризации IT-затрат. Она позволяет бизнесу лучше понимать затраты на IT, облегчая принятие решений о бюджетировании, инвестировании и управлении затратами. ATUM разделяет затраты по определенным категориям для создания ясности.

**IT Tower**: отображает область технологических затрат.

**Service Family**: определяет основные категории услуг.

**Service Type**: отражает тип конкретной услуги

**Service Sub-Type**: указывает на более детальное подразделение типа услуги

<img width="468" alt="image" src="https://github.com/luckyapin/clouds/assets/112975832/c679c63b-b389-4d98-82df-47d878dd51a5">

<img width="468" alt="image" src="https://github.com/luckyapin/clouds/assets/112975832/52ffb54f-f334-4b61-9adf-e72182320840">

**Описание встретившихся сервисов Amazon**

**1. Amazon EC2**\
Amazon EC2 (Elastic Compute Cloud) представляет собой веб-сервис, который обеспечивает масштабируемые вычислительные ресурсы в облаке.
EC2 позволяет арендовать виртуальные компьютеры для запуска различных приложений. Пользователи могут выбирать объем вычислительных, памяти, хранилища и других ресурсов в соответствии с требованиями своих приложений. Эластичное вычислительное облако Amazon (Amazon EC2) предлагает самую широкую и глубокую вычислительную платформу с более чем 700 инстансами и набором новейших процессоров, хранилищ, сетей, операционных систем и моделей покупок, обеспечивая должное соответствие нуждам конкретной рабочей нагрузки. 

**2. Amazon DynamoDB Accelerator (DAX)**\
Ускоритель Amazon DynamoDB (DAX) – это полностью управляемый высокодоступный сервис кэширования для Amazon DynamoDB. DAX обеспечивает повышение производительности в 10 раз – с миллисекунд до микросекунд – даже при миллионах запросов в секунду. DAX выполняет всю работу по реализации ускорения в памяти для таблиц DynamoDB, избавляя разработчиков от трудоемких задач по инвалидации кэша, его заполнению данными и по управлению кластерами.

**3. Amazon DynamoDB**\
Amazon DynamoDB – полностью управляемая бессерверная база данных NoSQL на основе пар «ключ-значение», созданная для запуска высокопроизводительных приложений в любом масштабе. DynamoDB предлагает встроенную защиту, непрерывное резервное копирование, автоматическую репликацию в нескольких регионах, кэширование в памяти и инструменты импорта и экспорта данных

**4. AWS Database Migration Service**\
Сервис миграции баз данных AWS (AWS DMS) – это управляемый сервис миграции и репликации, который помогает быстро, безопасно, с минимальными простоями и нулевой потерей данных перенести рабочие нагрузки баз данных и аналитики на AWS. AWS DMS поддерживает миграцию между более чем 20 движками баз данных и аналитики


**5. AWS Device Farm**\
AWS Device Farm – это сервис для тестирования приложений, который позволяет повысить производительность мобильных и веб-приложений. Для этого используются различные браузеры для настольных компьютеров и реальные мобильные устройства, поэтому вам не требуется создавать собственную инфраструктуру для тестов. Сервис позволяет проводить тесты одновременно в нескольких браузерах для настольных компьютеров или использовать для этого реальные мобильные устройства. Это ускоряет процесс тестирования, во время которого также создаются видео и журналы для быстрого выявления ошибок в работе вашего приложения.


**6. AWS IoT Device Management**\
AWS IoT Device Management - это сервис управления устройствами Интернета вещей (IoT), который помогает регистрировать, упорядочивать, отслеживать устройства IoT и осуществлять управление ими в любых масштабах

**7. Amazon Translate**\
Amazon Translate – это сервис нейронного машинного перевода, обеспечивающий быстрый, высококачественный, доступный по стоимости перевод с пользовательскими настройками с одного языка на другой.

**8. Amazon Transcribe**\
Amazon Transcribe - это сервис распознавания речи, предоставляемый Amazon Web Services (AWS). Он предназначен для автоматической транскрибации аудиофайлов в текст, что позволяет пользователям легко извлекать смысловую информацию из разговоров, видео, конференций и других аудиозаписей.


**9. AWS CloudHSM (Hardware Security Module)**\
AWS CloudHSM — это управляемый облачный сервис, который позволяет вам управлять ключами и получать к ним доступ на оборудовании, прошедшем проверку FIPS, защищенном принадлежащими клиенту инстансами HSM с одним арендатором, которые работают в вашем собственном виртуальном частном облаке (VPC).

**10. AWS CodeBuild**\
AWS CodeBuild — это полностью управляемый сервис непрерывной интеграции, который компилирует исходный код, выполняет тестирование и формирует готовые к развертыванию пакеты программного обеспечения. Благодаря CodeBuild больше не нужно распределять и масштабировать собственные серверы сборок, а также обеспечивать управление ими. Достаточно указать, где располагается код, выбрать параметры сборки – и CodeBuild сам запустит скрипты компиляции, тестирования и сборки пакетов кода.

**11. Amazon Comprehend** \
Amazon Comprehend – это сервис обработки естественного языка (NLP), в котором для поиска ценной информации и взаимосвязей в тексте применяются технологии машинного обучения. Он позволяет анализировать текстовую информацию для извлечения полезной информации, такой как ключевые фразы, языковая окраска, настроения, идентификация личностей, персонализированные рекомендации и многое другое.

**12. Amazon Comprehend Medical**\
Amazon Comprehend Medical - это служба обработки естественного языка (Natural Language Processing, NLP), предоставляемая Amazon Web Services (AWS), специально нацеленная на медицинские данные. Она обладает способностью анализировать и извлекать информацию из медицинских текстов, таких как клинические записи, рецепты, результаты обследований и многое другое.


**13. AWS Backup** \
AWS Backup — это экономичный, полностью управляемый сервис на основе политик, с помощью которого можно существенно упростить защиту данных в проекте любого масштаба. Он обеспечивает централизованное управление и автоматическое резервное копирование данных в облачной инфраструктуре AWS. Этот сервис предназначен для обеспечения безопасности и восстановления данных для различных служб AWS, таких как Amazon EBS (Elastic Block Store), Amazon RDS (Relational Database Service), Amazon DynamoDB и другие.

**Описание отечественного аналога**

Аналоги были взяты с сайта Yandex Cloud. [Сопоставление с Amazon Web Services](https://cloud.yandex.ru/docs/overview/platform-comparison/aws)

### Итоговая таблица:

<img width="1184" alt="image" src="https://github.com/luckyapin/clouds/assets/112975832/70f5fc09-d99e-4205-b4c2-c88c78854f2d">

### Вывод:

Лабораторная работа включала в себя анализ функциональных возможностей Amazon сервисов, с использованием информации из официальной документации. Эти данные затем были использованы для составления таблицы, содержащей подробную информацию о типах и подтипах сервисов Amazon. Yandex Cloud предлагает широкий спектр аналогичных сервисов и продуктов, которые могут быть использованы в качестве замен AWS-сервисов.

<a name="Azure"></a>
## Azure

### Цель работы:

```
Знакомство с облачными сервисами. Понимание уровней абстракции над инфраструктурой в облаке. Формирование понимания типов потребления сервисов в сервисной-модели. Сопоставление сервисов между разными провайдерами. Оценка возможностей миграции на отечественные сервисы.
```

### Дано:

```
Слепок данных биллинга от провайдера после небольшой обработки в виде SQL-параметров. Необходимо заполнить пустые ячейки с заголовками IT Tower, Service Family, Service Type, Service Sub-Type, используя элементы модели Apptio TBM Unified Model (ATUM) для упрощения соответствия сервисов. Определить соответствие каждого сервиса международного провайдера русскому сервису.
```

### Ход работы:

**Описание Apptio TBM Unified Model**

**Apptio TBM Unified Model (ATUM)** — это стандартизированная модель для категоризации IT-затрат. Она позволяет бизнесу лучше понимать затраты на IT, облегчая принятие решений о бюджетировании, инвестировании и управлении затратами. ATUM разделяет затраты по определенным категориям для создания ясности.

**IT Tower**: отображает область технологических затрат.

**Service Family**: определяет основные категории услуг.

**Service Type**: отражает тип конкретной услуги

**Service Sub-Type**: указывает на более детальное подразделение типа услуги

<img width="468" alt="image" src="https://github.com/luckyapin/clouds/assets/112975832/c679c63b-b389-4d98-82df-47d878dd51a5">

<img width="468" alt="image" src="https://github.com/luckyapin/clouds/assets/112975832/52ffb54f-f334-4b61-9adf-e72182320840">

**Описание встретившихся сервисов Amazon**

**1. Azure managed databases**\
Azure managed databases - это служба в облаке, предоставляемая Microsoft Azure, которая позволяет пользователям управлять базами данных без необходимости устанавливать, настраивать и обслуживать инфраструктуру баз данных. Эта служба предоставляет полностью управляемые базы данных, включая автоматическое резервное копирование, масштабирование, мониторинг и безотказность.

**2. Machine Learning Studio**\
Machine Learning Studio – это интегрированная среда разработки, которая позволяет специалистам по данным и разработчикам создавать, развертывать и управлять высококачественными моделями быстрее и с уверенностью.

**3. Azure Bastion**\
Azure Bastion – это полностью управляемая служба, которая обеспечивает более безопасный и простой доступ к виртуальным машинам с помощью подключения RDP и SSH без риска, который представляет использование общедоступных IP-адресов. Подготовьте службу непосредственно в локальной или одноранговой виртуальной сети, чтобы получить поддержку для всех работающих в ней виртуальных машин.

**4. Azure API Management**\
Azure API Management –  это служба управления интерфейсами программирования приложений (API). Она позволяет организациям легко создавать, развертывать, защищать и монетизировать свои API.

**5. Azure Monitor**\
Azure Monitor - это сервис мониторинга и управления. С его помощью вы можете собирайть и анализировать данные телеметрии, поступающие из облачных и гибридных сред. Azure Monitor поддерживает масштабные операции, помогая повысить производительность и доступность ресурсов, а также заблаговременно выявлять проблемы.

**6. Azure Backup**\
Azure Backup - централизованная облачная служба резервного копирования и соответствующее решение для защиты от программ-шантажистов. Это экономичное и безопасное решение, обеспечивающее резервное копирование одним щелчком, которое масштабируется в зависимости от ваших потребностей в хранилище резервных копий. Централизованный интерфейс управления позволяет легко определять политики резервного копирования и защищать широкий спектр корпоративных рабочих нагрузок, включая Виртуальные машины Azure, базы данных SQL и SAP, а также общие папки Azure.

**7. Azure Business Analytics (Business intelligence)**\
Business intelligence – это сервис, который позволяет компаниям анализировать данные и получать ценные инсайты для принятия бизнес-решений. С помощью Azure BI пользователи могут собирать, хранить, анализировать и визуализировать данные из различных источников, таких как базы данных, облака, гигабайты данных хранения.

**8. Virtual Machines Licenses (Azure Virtual Machines)**\
Azure Virtual Machines - это служба облачных вычислений, которая позволяет пользователям создавать и управлять виртуальными машинами в облаке. С помощью Azure Virtual Machines пользователи могут развертывать виртуальные машины с различными операционными системами, такими как Windows и Linux, и настраивать их в соответствии с потребностями своих приложений. 


**9. Azure Compute Hours (Azure Compute)**\
Azure Compute — это служба облачных вычислений, позволяющая пользователям создавать, управлять и масштабировать виртуальные машины и контейнеры в облаке, обеспечивая вычислительные ресурсы для запуска приложений и обработки данных. 

**Описание отечественного аналога**

Аналоги были взяты с сайта Yandex Cloud. [Сопоставление с Microsoft Azure](https://cloud.yandex.ru/docs/overview/platform-comparison/azure)

### Итоговая таблица:

<img width="1248" alt="image" src="https://github.com/luckyapin/clouds/assets/112975832/cb2792fd-d0e5-44c1-81f5-cc655a5c9116">

### Вывод:

Лабораторная работа включала в себя анализ функциональных возможностей Azure сервисов, с использованием информации из официальной документации. Эти данные затем были использованы для составления таблицы, содержащей подробную информацию о типах и подтипах сервисов Azure. Yandex Cloud предлагает широкий спектр аналогичных сервисов и продуктов, которые могут быть использованы в качестве замен Azure-сервисов.

<p align="right"><a href="#Вернуться в начало">Вернуться в начало</a></p>
