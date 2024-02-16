# POWER BI (расширенный)

## Вопросы к данным
Вычисления логики операций со временем могут помочь ответить на следующие вопросы, связанные со временем:

- Каково накопление дохода за год, квартал или месяц?
- Какой доход получен за тот же период прошлого года?
- Какой рост дохода достигнут за тот же период прошлого года?
- Сколько новых заказчиков сделали первый заказ в каждом месяце?
- Какова стоимость складских запасов продуктов компании?

## Формулы
### Продажи с накоплением
    Sales YTD = TOTALYTD(SUM(Sales[Sales]), 'Date'[Date], "6-30")

### Продажи по сравнению с пред. периодом
    Sales YoY Growth = 
    VAR sales_prev_year =     
      CALCULATE(
        SUM(Sales[Sales]),
        PARALLELPERIOD(
          'Date'[Date],
          -12,
          MONTH
        )
      )
      
    RETURN
      DIVIDE(
        (SUM(Sales[Sales]) - sales_prev_year),
        sales_prev_year
      )
### Ранжирование по колонке
Ранжирование по кол-ву, используем так называемое "плотное ранжирование" - указан DENSE (исключает пропуски)

    Product Quantity Rank =
    IF(
      HASONEVALUE('Product'[Product]),
      RANKX(
        ALL('Product'[Product]),
        [Quantity],
        ,
        ,
        DENSE
      )
    )

### Доля доходности в %
Вычисляет долю доходности в %, используется REMOVEFILTERS для сброса контекста фильтра (позволяет получить общий доход)

    Revenue % Total Region =
    VAR CurrentRegionRevenue = [Revenue]
    VAR TotalRegionRevenue =
      CALCULATE (
        [Revenue],
        REMOVEFILTERS ( 'Sales Territory' )
      )
    RETURN
      DIVIDE (
        CurrentRegionRevenue,
        TotalRegionRevenue
      )
![доля доходности в %](./img/dax-matrix-sales-territory-revenue-2-ss.png)

### Вывод даты последнего обновления
В power query (pq) сделать таблицу простую, столбец неважно, доб. настр. столбец с формулой: 

    DateTime.LocalNow()

### Новые пользователи
Мера вычисляет прирост новых пользователей по сравнению с предущим периодом

    New Customers = 
    VAR CustomersLTD =
        CALCULATE(
            DISTINCTCOUNT(Sales[CustomerKey]),
            DATESBETWEEN(
                'Date'[Date],
                BLANK(),
                MAX('Date'[Date])
            ),
            'Sales Order'[Channel] = "Internet"
        )
    
    VAR CustomersPrior =
        CALCULATE(
            DISTINCTCOUNT(Sales[CustomerKey]),
            DATESBETWEEN(
                'Date'[Date],
                BLANK(),
                MIN('Date'[Date]) - 1
            ),
            'Sales Order'[Channel] = "Internet"
        )
    RETURN
        CustomersLTD - CustomersPrior

![новые пользователи](./img/new_usesrs.jpg)

### Вычисление моментальных снимков
Мера вычисляет остаток на последнюю дату. Актуально для случаев когда необходимо получить остаток на дату, т.е. скрипт делает снимок остатоков по продуктам на каждый день и записывается в таблицу остатков в виде Дата, Ид продукта, Остаток. Таким образом чтобы получить остаток на дату необходимо применит формулу:

    Stock on Hand Last Date = 
    CALCULATE(
        SUM(Inventory[UnitsBalance]),
        LASTNONBLANK(
            'Date'[Date],
            CALCULATE(SUM(Inventory[UnitsBalance]))
        )
    )

Важно: LASTNONBLANK - позволяет получить остаток даже в случае когда остаток не был на сегодня выгружен, но при этом он есть за пред. день, функция получит последний существующий.

Если применить формулу:

    Stock on Hand = 
    CALCULATE(
        SUM(Inventory[UnitsBalance]),
        LASTDATE('Date'[Date])
    )
то мы получим остатки только если была выгрузка, а нам нужно взять последний остаток который есть в таблице. На картинке ниже демонстрируется различая между формулами (таб. 2 - верное решение, есть остаток июнь 2020; таб. 1 - данные на июнь 2020 отсутствуют, хотя они есть на май 2020)

![остаток на дату](./img/balance_as_of_date.jpg)

### Формат даты
Выч. колонка в виде "Год Месяц_буквами"
    
    Month = FORMAT('Date'[Date], "yyyy MMM")

### Ключ даты
Выч. колонка формирует ключ даты. Используется в календаре дат, для корректной сортировки в отчетах

     MonthKey =
     (YEAR('Date'[Date]) * 100) + MONTH('Date'[Date])

### Неактивные отношения
USERELATIONSHIP - позволяет активировать неактивную связь таблицы. Например, когда у таблицы фактов есть две даты (дата продажи и дата отгрузки). Обе даты ссылаются на общую таблицу дат, т.е. имеет место так называемое "ролевое измерение" (отчет можем стоить по дате продажи или по дате отгрузки)

    Sales Shipped = 
    CALCULATE(
        SUM('Sales'[Sales Amount]),
        USERELATIONSHIP('Date'[DateKey], 'Sale'[ShipDateKey])
    )
