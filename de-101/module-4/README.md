# Модуль 4: Интеграция и трансформация данных - ETL и ELT
## Рынок решений ETL
- AirFlow
- Apache NiFi
- Pentaho DI
- Azure Data Factory

## ETL подсистемы

### Data Extracting
#### 1 - Data Profiling System
Система для сбора данных о наших данных:

- структура данных
- статистические данных
- количество Null в столбце
- Max/Min/Avg
- количество строк
- количество уникальных значений в столбце

#### 2 - Change Data Capture
Задача системы выявить механизм изменения данных в исходных системах, чтобы загрузить только свежие или измененные данные в хранилище

- source data based - самый распрастраненный
- trigger based - исходная база данных может выполнять команды INSERT/UPDATE/DELETE в нашем хранилище(обновление в реальном времени)
- snapshot based - если нет timestamp, чтобы отслеживать историю и изменения, мы можем делать снимок(snapshot) текущей таблицы и сохранять его в нашем DW
- log based - часто БД умеют хранить историю операций в логах, некоторые инструменты умеют читать эти логи и воспроизводить команды

Другими словами, мы должны ответить на вопрос, как мы будем выявлять свежие записи и загружать в наше хранилище ?

Пример для Source Based:

- часто используется timestamp в столбце, по которому мы можем выявить свежие строки и загрузить

    WHERE update_date >= MAX(event_date)

- иногда используется числовая последовательность
- если нет изменений в прошлом (например обновление статуса заказа), то можно копировать дни по дням или по часам (в случае большого объмема данных)

Хотим загрузить 1 день 2020-12-31:

1. Копируем данные с помощью ETL/ELT процесса в наше DW хранилище в staging
2. На всякий случай удаляем существующие записи, чтобы избежать вохможные дубликаты

```sql
    DELETE FROM fact_table
    WHERE event_date = "2020-12-31"
```

3. Вставляем свежие строки

```sql
  INSERT INTO fact_table AS
  SELECT * FROM stg.events
```

#### 3 - Extracting System
Задача системы понять систему источник и уметь к ней подключаться, чтобы забирать данные:

- файлы (локально или удаленно, например FTP, Shared Folders)
- базы данных(коннектор, поддержка синтаксиса)
- приложения(CRM, ERP и другие). Внутри БД, но часто нужно использовать специальный коннектор
- web-based - api, RSS, HTTPS и другие

### Cleaning and Conforming Data
#### 4 - Data Cleaning and Quality Screen Handler System
Задача системы подготовить данные для анализа, необходимо очистить данные и проверить их качество, частые операции:

- замена NULL на "unknown" / "NA"
- форматирование даты и времени к общему формату
- unit tests(например, кол-во строк > 0)
- работа с текстом - UPPERCASE / LOWERCASE, TRIM и тп
- LOOKUP операции, чтобы использовать стандартизированные измерения
- валидация данных(например, email должен быть в правильном формате, город должен быть реальным и тп)

#### 5 - Error Event Handler
Задача системы отлавливать ошибки и принимать решения, что делать дальше, чтобы не сломать весь ETL процесс. Мы можем:

- пропустить плохие значения и загрузить хорошие
- записать плохие значения в лог или файл
- обработать плохие значения в отдельном job
- при сбое (например из-за отсутствия подключения), мы можем перезапустить job(операция retry)
![5-error-event-handler](./assets/5-error-event-handler.jpg)

#### 6 - Audit Data
Задача системы мониторить качество данных и выявлять отклонения
![assets/6-audit-data](./assets/6-audit-data.jpg)

#### 7 - Dedublication System
Задача системы выявлять дубликаты записей (например, id, события и показатели) и устранять их. 

Пример SQL:

Таблица sales имеет гранулярность order_id. Каждый заказ уникален, чтобы выявить такие записи можно выполнить след. запрос:

    SELECT 
      order_id,
      count(*) AS rows
    FROM sales
    GROUP BY
      order_id
    HAVING count(*) > 1

#### 8 - Data Conformer
Задача системы согласовывать измерения и показатели из разных систем источников для использования их в отчетности (dimensions, measures) или data science (features / attributes)
![8-data-conformer](./assets/8-data-conformer.jpg)

### Data Delivery
#### 9 - Slowly Changing Dimension Processor
Задача системы отображать изменения в измерениях (dimension). Существует много типов изменений измерений (часто 6, но не удивляйтесь встретить SCD 7 и 8). Но важно знать 3 основных. Рассмотрим пример, в котором Боб жил в UK, а потом стал жить в US.

![scd](./assets/9-scd.jpg)

В зависимости от типа SCD мы можем отобразить это по разному:

- SCD Type 1 - наше измерение всегда имеет последнее значение. То есть, мы просто перезаписываем значение и нам не важно, какое было в прошлом                      
![scd](./assets/9-scd.jpg)
- SCD Type 2 - мы отслеживаем историю с помощью вспомогательных столбцов
![scd](./assets/9-scd-2.jpg)
- SCD Type 3 - мы сохраняем предыдущее значение в соседней колонке
![scd](./assets/9-scd-3.jpg)

#### 10 - Surrogate Key Creation System
Задача системы генерировать суррогатные ключи для наших натуральных ключей. Например, вместо номера заказа, у нас есть id заказа, вместо номера клиента мы создадим customer_id. Если из исходной системы приходит order_id, мы сделаем свой ключ - order_sur_id. Существуют следующие способы:

- использовать вычисление MAX(val) + 1
- исползовать SEQUENCE в БД
- использовать auto increment field

#### 11 - Hierarchy Dimension Builder
Задача системы создавать и поддерживать иерархии. Например:
- год, квартал, месяц, неделя, день
- категория, подкатегория, продукт


#### 12 - Special Dimension Builder
Задача системы подобрать правильный тип для таблицы измерений (Dimension Table). Бывают следующие типы измерений:

- Junk Dimension - измерения, для которых нет своей таблицы. Часто это флаг "Yes/No" и другие измерения с низкой кардинальностью
- Mini Dimension - часто используются для разбивки гиганской таблицы измерения на более маленькие
- Shrunken or rolled dimension - дополнительная таблица измерений, созданая на базе существующей. Например для агрегированной таблицы фактов.
- Static dimension - LOOKUP таблица, которая крайне редко обновляется, часто вручную
- User maintained dimension - custom измерения, которые создаются пользователями

#### 13 - Fact Table Loader
Задача системы выбрать правильный тип таблицы фатов:

- transaction grain fact table - классическая таблица фактов, где каждая строчка представляет какое-нибудь событие (заказ, звонок, клик, просмотр и тд)
- periodic snapshot fact table - мы делаем периодические снимки с заданным промежутком времени (день, месяц, неделя и тп)
- accumulation snapshot fact table - сводная таблица фактов моментального снимка: таблица фактов, в которой время и состояние из разных точек во времени помещаются как разные столбцы в одной строке. Строка описывает одного конкретного клиента.

#### 14 - Surrogate Key Pipeline
Задача системы использовать правильный суррогатный ключ при создании таблицы фактов.

Сначала мы заменяем натуральный ключ для Dimension и потом делаем Lookup операцию при загрузки в Хранилище

![14-surrogate-key-pipeline](./assets/14-surrogate-key-pipeline.jpg)

#### 15 - Multy-Valued Dimension Bridge Table Builder
Задача системы поддержать связки "многие-ко-многим" (many to many). 

Вопрос на собесе: как соединять таблицу фактов с таб измерений в которой со связью многие ко многим (\* : \*) ?

Ответ: с помощью bridge таблицы, таблица которая позволяет поддерживать связь \* : \*

![bridge table](./assets/bridge-table.jpg)

#### 16 - Late-Arriving Data Handler
Задача системы обрабатывать данные Dimension, которые появились позже(late arriving). Обычно подходит для SCD-2 типа

#### 17 - Dimemsion Manager System
Задача системы упралять Dimensions

#### 18 - Fact Table Provide System
Задача системы управлять Fact Tables

#### 19 - Aggregate Builder
Задача системы создавать агригированные Fact Tables, для увелечения производительности запросов

#### 20 - Multidimensional (OLAP) Cube Builder
Задача системы создавать и управлять Multidimensional (OLAP) кубами. Пример системы - Microsoft Analysis Services

#### 21 - Data Integration Manager
Задача системы забирать данные из хранилища данных и загружать их в другие системы

### Managing the ETL Enviroment
#### 22 - Job Scheduler
Задача системы запускать ETL jobs (data pipelines) по расписанию, можно использовать CRON, Windows Task Manager или встроенную функциональность

#### 23 - Backup System
Задача системы организовать backup данных, например в Staging или в файловом хранилище

#### 24 - Recovery and Restart System
Задача системы перезапустить ETL job при сбои с того же самого места, без риска создания дубликатов или других проблем

#### 25 - Version Control System and Subsystem
Задача системы использовать практики разработки ПО для ETL/DW (DevOps, CI/CD и тп.)

#### 26 - Version Migration System from test to product
Задача системы использовать практики разработки ПО для ETL/DW (DevOps, CI/CD и тп.)

#### 27 - Workflow Monitor
Задача системы мониторить работу ETL решения

#### 28 - Sort System 
Задача системы упорядочивать строки

#### 29 - Lineage and Dependency Analyzer
Задача системы отслеживать трансформацию показателей начиная с бизнес метрик и измерений

#### 30 - Proplem Escalation System
Задача системы сообщать о проблемах и автоматически создавать тикет в системе Jira или подобной

#### 31 - Parallelizing/Pipelineg System
Задача системы обрабатывать данные параллельно

#### 32 - Security System
Задача системы обеспечивать безопасность - аутентификацию и авторизацию

#### 33 - Compliance Reporter
Задача системы собирать данные для возможного аудита, где можно отследить все действия в ETL решении

#### 34 - Metadata Repository Manager
Задача системы хранить все метаданные о ETL решении (jobs, пользователи и тп.)

## Практика
С помощью инструмента ETL построить модель данных типа "Звезда" (таблицы измерений и таблица фактов) на данных из модуля 2

![модель данных](../module-2/assets/de%20model%20-%20SqlDBM.jpg)

Результат:

Читаем файл базы данных и загружаем данные в область staging

[Трансформация в staging](./assets/my_stage_orders.ktr)

![Трансформация staging](./assets/my_stage_orders.jpg)
![Область staging в бд](./assets/db_stage.jpg)

Создаем слой модели данных dw

[Трансформация в dw](./assets/my_dim_tables.ktr)

![Трансформация в dw](./assets/my_dim_tables.jpg)
![Область dw в бд](./assets/db_dw.jpg)

Таблица фактов в слой dw

[Трансформация в dw](./assets/my_gen_fact_table.ktr)

![Трансформация в dw](./assets/my_gen_fact_table.jpg)

Итоговый job

[job](./assets/my_job.kjb)

![job](./assets/my_job.jpg)