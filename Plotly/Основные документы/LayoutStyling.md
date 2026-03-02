# Layout & Styling

Настройка внешнего вида (Layout) — это ключ к созданию профессиональных визуализаций. В Plotly за это отвечает метод `.update_layout()` или объект `go.Layout`.

### 1. Настройка осей и заголовка
Вы можете изменять подписи, диапазоны и сетку для каждой оси отдельно.

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))

fig.update_layout(
    title={
        'text': "Заголовок графика",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title="Название оси X",
    yaxis_title="Название оси Y",
    font=dict(family="Arial", size=14, color="RebeccaPurple")
)
fig.show()
```

### 2. Использование встроенных тем
Plotly поставляется с несколькими готовыми шаблонами (templates), которые меняют фон и палитру.

```
# Доступные темы: "plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "none"
fig.update_layout(template="plotly_dark")
```

### 3. Настройка легенды
Управление положением и стилем пояснительных обозначений.

```
fig.update_layout(
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        bgcolor="LightSteelBlue"
    )
)
```

### Популярные параметры настройки
Параметр	Описание	Пример значения
paper_bgcolor	Цвет области вокруг графика	'white' или '#ffffff'
plot_bgcolor	Цвет фона самой диаграммы	'rgba(0,0,0,0)'
margin	Отступы (l, r, t, b)	dict(l=20, r=20, t=20, b=20)
hovermode	Режим подсказок	'x', 'y', 'closest'

### Цветовые шкалы
Для графиков с градиентом можно использовать встроенные наборы:

```
import plotly.express as px
# Использование цветовой шкалы Viridis
fig = px.scatter(df, x="x", y="y", color="z", color_continuous_scale=px.colors.sequential.Viridis)
```