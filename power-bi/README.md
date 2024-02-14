# POWER BI (расширенный)

## Вывод даты последнего обновления
В power query (pq) сделать таблицу простую, столбец неважно, доб. настр. столбец с формулой: 

    DateTime.LocalNow()

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
