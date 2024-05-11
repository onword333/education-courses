# Модуль 4: Интеграция и трансформация данных - ETL и ELT
## Рынок решений ETL
- AirFlow
- Apache NiFi
- Pentaho DI
- Azure Data Factory

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