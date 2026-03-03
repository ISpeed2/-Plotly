import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 3. Пример для Subplots 
fig3 = make_subplots(rows=1, cols=2, subplot_titles=("Левый", "Правый"))
fig3.add_trace(go.Scatter(x=[1, 2], y=[1, 2]), row=1, col=1)
fig3.add_trace(go.Bar(x=[1, 2], y=[2, 1]), row=1, col=2)


fig3.write_html("subplots.html", auto_open=True)

