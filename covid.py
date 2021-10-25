import pandas as pd
import ploty.express as px

df = pd.read_csv(line_chart.csv)

fig = px.line(df,  x="date", y="number of covid cases",  color="country",  title="per covid cases")

fig.show()