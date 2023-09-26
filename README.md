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
        <li><a href="#Лабораторная 2">Лабораторная 2</a></li>
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


<a name="Лабораторная 2"></a>
## Лабораторная 2
```
Написать два Dockerfile – плохой и хороший. Плохой должен запускаться и работать корректно, но
в нём должно быть не менее 3 “bad practices”. В хорошем Dockerfile они должны быть исправлены.
В Readme описать все плохие практики из кода Dockerfile и почему они плохие, как они были исправлены
в хорошем  Dockerfile, а также две плохие практики по использованию этого контейнера.
```

Было решено обернуть в docker-контейнер [телеграм-бот](https://github.com/luckyapin/clouds/blob/main/lab2/tgbot.py), написанный на языке python. 
Был создан файл [dockerfile](https://github.com/luckyapin/clouds/blob/main/lab2/dockerfile), в котором были описаны инструкции для Docker-a.

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


<p align="right"><a href="#Вернуться в начало">Вернуться в начало</a></p>


