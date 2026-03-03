import plotly.graph_objects as go
from plotly.subplots import make_subplots

#  2. Пример для Graph_Objects
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 1, 2], name="Линия"))
fig2.add_trace(go.Bar(x=[1, 2, 3], y=[2, 5, 3], name="Столбцы"))
fig2.update_layout(title="Graph Objects Demo")


fig2.write_html("graph_objects.html", auto_open=True)


