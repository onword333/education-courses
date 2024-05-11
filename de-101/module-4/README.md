# Модуль 4: Интеграция и трансформация данных - ETL и ELT
## Рынок решений ETL
- AirFlow
- Apache NiFi
- Pentaho DI
- Azure Data Factory

## Практика
С помощью инструмента ETL построить модель данных типа "Звезда" (таблицы измерений и таблица фактов) на данных из модуля 2

Результат:

Читаем файл базы данных и загружаем данные в область staging

[Трансформация в staging](./assets/my_stage_orders.ktr)

![Трансформация staging](./assets/my_stage_orders.jpg)
![Область staging в бд](./assets/db_stage.jpg)

Создаем слой модели данных dw

[Трансформация в dw](./assets/my_dim_tables.ktr)

![Трансформация в dw](./assets/my_dim_tables.jpg)
![Область dw в бд](./assets/db_dw.jpg)