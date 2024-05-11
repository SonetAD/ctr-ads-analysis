

'''
Function: draw_graph

Description: This function takes 5 arguments-
* data-pandas dataframe
* x_col- tarrget column(click)
* color_col- input column(user data like age,gender,his_app_size etc)
* title- the title which will be shown top of the graph

Developer: Team Deadline Doers

Date: 2 May,2024
'''

# import external libns

import plotly.express as px
import plotly.io as pio

def draw_graph(data, x_col, color_col, title, color_map=None):
    pio.templates.default='plotly_white'
    fig = px.box(data, 
                 x=x_col, 
                 color=color_col, 
                 title=title, 
                 color_discrete_map=color_map)
    fig.update_traces(quartilemethod="exclusive")
    fig.show()


