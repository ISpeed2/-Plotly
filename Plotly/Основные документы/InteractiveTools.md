# Interactive Tools & Animation

Plotly позволяет добавлять элементы управления (Custom Controls) прямо на график. Это дает возможность пользователю менять данные или тип визуализации без перезапуска кода.

### 1. Анимация (Animations)
Самый простой способ создать анимацию — использовать Plotly Express с аргументами `animation_frame` и `animation_group`.

```python
import plotly.express as px
df = px.data.gapminder()

fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", 
                 animation_group="country", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

fig.show()
```

### 2. Кнопки (Update Buttons)
Кнопки позволяют изменять параметры графика (например, переключаться между линейным и столбчатым видом).

```
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines'))

fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="left",
            buttons=list([
                dict(
                    args=[{"type": "scatter", "mode": "lines"}],
                    label="Линии",
                    method="restyle"
                ),
                dict(
                    args=[{"type": "bar"}],
                    label="Столбцы",
                    method="restyle"
                )
            ]),
        )
    ]
)
fig.show()
```

### 3. Слайдеры (Sliders)
Слайдеры удобны для фильтрации данных по времени или порогу значений.

```
# Слайдер обычно настраивается через layout.sliders
fig.update_layout(
    sliders=[dict(
        active=0,
        currentvalue={"prefix": "Выбранный год: "},
        pad={"t": 50},
        steps=steps # steps - это список конфигураций для каждого шага
    )]
)
```

Типы интерактивных методов

| Метод | Описание |
| :--- | :--- |
| `restyle` | Изменяет данные или параметры самих графиков (traces). |
| `relayout` | Изменяет параметры оформления (layout), например, оси. |
| `update` | Позволяет изменять и данные, и оформление одновременно. |
| `animate` | Запускает или настраивает последовательность кадров. |
