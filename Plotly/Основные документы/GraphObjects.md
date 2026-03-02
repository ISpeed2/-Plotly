# Plotly Graph Objects 

Модуль `Plotly.graph_objects` предоставляет иерархическую структуру классов для детальной настройки каждого элемента графика. Это необходимо, когда возможностей быстрого интерфейса Express становится недостаточно.

### Когда использовать Graph Objects?
- Если нужно комбинировать разные типы графиков на одном холсте.
- Для создания кастомных кнопок и сложных анимаций.
- Когда требуется полный контроль над структурой JSON-объекта фигуры.

### Базовая структура фигуры
Фигура состоит из двух основных частей: `data` (сами графики) и `layout` (оформление).

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[10, 20, 30])],
    layout=go.Layout(title="Базовый пример")
)
fig.show()
```

### Добавление нескольких слоев 
Вы можете добавлять новые слои к уже существующей фигуре с помощью метода .add_trace().

```
import plotly.graph_objects as go

fig = go.Figure()

# Добавляем первый график (Scatter)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[10, 15, 13], mode='lines', name='Линия'))

# Добавляем второй график (Bar)
fig.add_trace(go.Bar(x=[1, 2, 3], y=[12, 11, 14], name='Столбцы'))

fig.update_layout(title="Комбинированный график")
fig.show()
```

### Работа с 3D графиками

```
import plotly.graph_objects as go
import numpy as np

z = np.random.standard_normal((10, 10))

fig = go.Figure(data=[go.Surface(z=z)])
fig.update_layout(title='3D Поверхность')
fig.show()
```

### Сравнение с Plotly Express

### Сравнение с Plotly Express


| Характеристика | Plotly Express | Graph Objects |
| :--- | :--- | :--- |
| **Сложность** | Низкая (быстрый старт) | Средняя / Высокая |
| **Код** | 1 строка | Многострочный |
| **Кастомизация** | Ограничена шаблонами | Полная свобода |
| **Данные** | Только Pandas-подобные | Любые итерируемые объекты |




