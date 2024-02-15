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
