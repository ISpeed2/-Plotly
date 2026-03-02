# Plotly Express

`Plotly.express` — это высокоуровневый интерфейс библиотеки, предназначенный для максимально быстрого создания графиков. Он автоматически обрабатывает структуру данных (Pandas DataFrame) и настраивает стили.

### Основные возможности
- Создание сложных графиков одной строкой кода.
- Автоматическая группировка данных по цветам, символам и размерам.
- Встроенная поддержка стандартных наборов данных для тестов.

### 1. Линейные графики (Line Charts)
Используются для отображения динамики данных во времени.

```python
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Продолжительность жизни в Канаде')
fig.show()
```

### 2. Диаграммы рассеяния (Scatter Plots)
Идеальны для поиска корреляций между двумя или тремя переменными.

```
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size="petal_length")
fig.show()
```

### 3. Гистограммы (Histograms)
Для анализа распределения величин.

```
import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="total_bill", nbins=20, color="sex")
fig.show()
```

### 4. Столбчатые диаграммы (Bar Charts)
Сравнение категориальных данных.

```
import plotly.express as px

df = px.data.medals_long()
fig = px.bar(df, x="medal", y="count", color="nation", barmode="group")
fig.show()
```

### Основные аргументы функций px:

### Основные аргументы функций px:


| Аргумент | Описание |
| :--- | :--- |
| `data_frame` | Объект DataFrame с данными. |
| `x`, `y` | Названия колонок для осей. |
| `color` | Группировка данных по цветам. |
| `facet_col` | Разделение на несколько подграфиков по колонкам. |
| `hover_name` | Данные, отображаемые в заголовке подсказки. |

