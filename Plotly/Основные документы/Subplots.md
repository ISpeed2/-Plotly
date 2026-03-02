# Subplots (Подграфики)

Модуль `Plotly.subplots` позволяет создавать сетки (ряды и колонки), в которых каждый сегмент содержит отдельный график. Это необходимо для сравнения разных наборов данных в одном окне.

### 1. Создание базовой сетки
Для работы используется функция `make_subplots`. После создания сетки графики добавляются через `add_trace` с указанием строки и столбца.

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Создаем сетку 1 ряд и 2 колонки
fig = make_subplots(rows=1, cols=2, subplot_titles=("График А", "График Б"))

# Добавляем первый график
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=1, col=1)

# Добавляем второй график
fig.add_trace(go.Bar(x=[1, 2, 3], y=[2, 3, 5]), row=1, col=2)

fig.update_layout(title_text="Работа с подграфиками")
fig.show()
```

### 2. Специфические типы графиков
Если вы используете 3D-графики или карты в подграфиках, нужно явно указать тип (specs).

```
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}]] # xy для обычных, domain для круговых
)

fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2]), row=1, col=1)
fig.add_trace(go.Pie(labels=['A', 'B'], values=[40, 60]), row=1, col=2)
```

### 3. Настройка общих осей
Можно заставить графики синхронизироваться при масштабировании.

```
fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
```

### Параметры make_subplots


| Параметр | Описание |
| :--- | :--- |
| `rows` | Количество строк в сетке. |
| `cols` | Количество столбцов в сетке. |
| `shared_xaxes` | Если True, ось Х будет общей для всех столбцов. |
| `vertical_spacing` | Расстояние между строками (от 0 до 1). |
| `subplot_titles` | Список заголовков для каждого графика. |



