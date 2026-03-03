import plotly.express as px

# 1. Загружаем данные
df_iris = px.data.iris()

# 2. Создаем график
fig = px.scatter(df_iris, x="sepal_width", y="sepal_length", color="species", title="Forced Render")

# 3. ПРИНУДИТЕЛЬНОЕ ОТКРЫТИЕ:
# Код создаст файл 'temp_plot.html' в папке с вашим скриптом и сам откроет его в браузере
fig.write_html("temp_plot.html", auto_open=True)
