import plotly.express as px

# 1. Загружаем данные
df_iris = px.data.iris()

# 2. Создаем график
fig = px.scatter(df_iris, x="sepal_width", y="sepal_length", color="species", title="Forced Render")

fig.write_html("temp_plot.html", auto_open=True)

