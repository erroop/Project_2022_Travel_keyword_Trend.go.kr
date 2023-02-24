import pandas as pd
import dash
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df_visitor = pd.read_csv('./방문자 데이터/순위권_방문자_수.csv', encoding = 'cp949')
df_mention = pd.read_csv('./언급량 데이터/국내여행지_언급량.csv', encoding = 'cp949')
df_keyword = pd.read_csv('./키워드 분석 데이터 전처리/키워드 분석 데이터.csv', encoding = 'cp949')
df_navigation = pd.read_csv('./네비게이션 데이터/네비게이션전체.csv', encoding = 'cp949')
df_lodging_food = pd.read_csv("./네비게이션 데이터/네비게이션_숙소_음식.csv", encoding = "cp949")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Card( 
        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    html.H1("2022년 국내여행 키워드 트렌드 분석", style = {'border' : '3px solid skyblue', 'border-radius': '10px', 'font-weight' : 'bolder', "background":"white", 'font-size' : '30px', 'text-align' : 'center'})
                )
            ]),
            html.Br(),
            dbc.Row([
                    dbc.Col(
                        html.Div([
                            html.H4("국 내 여 행", style = {'border' : '3px solid skyblue', 'border-radius': '10px','padding' :'10px', 'font-weight' : 'bolder', "margin-top" : "7px","margin-left" : '872px', "font-size" : "20px", "background":"white"}),
                            dcc.Dropdown(
                            id = "month_Dropdown",
                            options = [
                                {"label" : i, "value" : i} for i in df_mention['월'].unique()],
                                multi = False,
                                value = "1월",
                                searchable = True,
                                placeholder = "날짜를 선택해 주세요.",
                                style={"margin-right" : "41px" , 'width':'200px', "float" : "right",'font-weight' : 'bolder', "border-width" : "2px", "border-color" : "skyblue"})], style = {'display' : 'flex', 'justify-content': 'space-between'}))
            ]),
            html.Br(),
            dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.H4("방문자 수", style = {"width" :"50%" , 'font-weight' : 'bolder', "font-size" : "20px", "text-decoration" : "underline", "text-underline-position": "under"}),
                            html.H4("SNS 국내여행 언급량", style = {"width" :"50%" , 'font-weight' : 'bolder', "font-size" : "20px", "text-decoration" : "underline", "text-underline-position": "under"})
                        ], style = {'display' : 'flex', 'justify-content': 'space-between', 'text-align' : 'center'})
                    ])
                ]),
            dbc.Row([
                    dbc.Col(html.Div([dcc.Graph(id = "visitor_graph")]), width = 6),
                    dbc.Col(html.Div([dcc.Graph(id = "mention_graph")]), width = 6),
            ]),
            html.Br(),
            html.Br(),
            dbc.Row([
                html.Div([
                    dbc.Col(
                        html.Div([
                        html.H4("키 워 드", style = {'border' : '3px solid skyblue', 'border-radius': '10px','padding' :'10px', 'font-weight' : 'bolder', "margin-top" : "7px","margin-left" : '885px', "font-size" : "20px", "background":"white"}),
                        dcc.Dropdown(
                            id = 'area_Dropdown',
                            options = [], multi = False, style={"margin-right" : "41px" , 'width':'200px', "float" : "right",'font-weight' : 'bolder', "border-width" : "2px", "border-color" : "skyblue"})], style = {'display' : 'flex', 'justify-content': 'space-between'})
                    )
                ])
            ]),
            html.Br(),
            html.Br(),
            dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.H4("SNS 키워드 언급량", style = {"width" :"100%" , 'font-weight' : 'bolder', "font-size" : "20px", "text-decoration" : "underline", "text-underline-position": "under"})
                        ], style = {'display' : 'flex','text-align' : 'center'})
                    ])
                ]),
             dbc.Row([
                dbc.Col(html.Div([dcc.Graph(id = "keyword_graph")]))]),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H4("네비게이션 검색 기록", style = {"width" :"68%" , 'font-weight' : 'bolder', "font-size" : "20px", "text-decoration" : "underline", "text-underline-position": "under"}),
                        html.H4("검색 유형 비율", style = {"width" :"32%" , 'font-weight' : 'bolder', "font-size" : "20px", "text-decoration" : "underline", "text-underline-position": "under"})
                    ], style = {'display' : 'flex', 'justify-content': 'space-between', 'text-align' : 'center'})
                ])
            ]),
            dbc.Row([
                dbc.Col(html.Div([dcc.Graph(id = "navigation_graph")]),width = 8),
                dbc.Col(html.Div([dcc.Graph(id = "navigation_pie")]), width = 4),
            ]),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H4("숙박 검색 순위", style = {"width" :"68%" , 'font-weight' : 'bolder', "font-size" : "20px", "text-decoration" : "underline", "text-underline-position": "under"}),
                        html.H4("숙박 유형 비율", style = {"width" :"32%" , 'font-weight' : 'bolder', "font-size" : "20px", "text-decoration" : "underline", "text-underline-position": "under"})
                    ], style = {'display' : 'flex', 'justify-content': 'space-between', 'text-align' : 'center'})
                ])
            ]),
            dbc.Row([
                dbc.Col(html.Div([dcc.Graph(id = "lodging_graph")]), width = 8),
                dbc.Col(html.Div([dcc.Graph(id = "lodging_pie")]), width = 4),
            ]),
            html.Br(),
            html.Br(),
            dbc.Col([
                html.Div([
                    html.H4("음식점 검색 순위", style = {"width" :"68%" , 'font-weight' : 'bolder', "font-size" : "20px", "text-decoration" : "underline", "text-underline-position": "under"}),
                    html.H4("음식 종류 비율", style = {"width" :"32%" , 'font-weight' : 'bolder', "font-size" : "20px", "text-decoration" : "underline", "text-underline-position": "under"})
                ], style = {'display' : 'flex', 'justify-content': 'space-between', 'text-align' : 'center'})
            ]),
            dbc.Row([
                dbc.Col(html.Div([dcc.Graph(id = "food_graph")]), width = 8),
                dbc.Col(html.Div([dcc.Graph(id = "food_pie")]), width = 4),
            ]),
            html.Br(),
        ], style = {"background":"#F3F3F3"})
    )
])
@app.callback(
    Output('area_Dropdown', 'options'),
    Input('month_Dropdown', 'value')
)
def set_area_options(month_Dropdown):
    dff_mention = df_mention[df_mention['월'] == month_Dropdown]
    return [{'label' : c, 'value' : c} for c in dff_mention['지역'].unique()]

@app.callback(
    Output('area_Dropdown', 'value'),
    Input('area_Dropdown', 'options')
)
def set_area_value(area_Dropdown_options):
    return [x['value'] for x in area_Dropdown_options]    

@app.callback(
    Output(component_id= "visitor_graph", component_property= "figure"),
    Output(component_id= "mention_graph", component_property= "figure"),
    Output(component_id= "keyword_graph", component_property= "figure"),
    Output(component_id= "navigation_graph", component_property= "figure"),
    Output(component_id= "navigation_pie", component_property= "figure"),
    Output(component_id= "lodging_graph", component_property= "figure"),
    Output(component_id= "lodging_pie", component_property= "figure"),
    Output(component_id= "food_graph", component_property= "figure"),
    Output(component_id= "food_pie", component_property= "figure"),
    Input(component_id= "month_Dropdown" , component_property= "value"),
    Input(component_id= "area_Dropdown" , component_property= "value")
)

def update_fig (month_Dropdown, area_Dropdown) :


    fig_visitor = px.bar(x = df_visitor[df_visitor['월'] == month_Dropdown]['기초지자체명'],
                         y = df_visitor[df_visitor['월'] == month_Dropdown]['기초지자체 방문자 수'])
    fig_visitor.update_xaxes(title_text = '지역명', categoryorder = "category ascending")
    fig_visitor.update_yaxes(title_text = '방문자 수')

    fig_mention = px.bar(x = df_mention[df_mention['월'] == month_Dropdown]['지역'],
                         y = df_mention[df_mention['월'] == month_Dropdown]['언급수'])
    fig_mention.update_xaxes(title_text = '지역명', categoryorder = "category ascending")
    fig_mention.update_yaxes(title_text = 'SNS 언급량')

    if len(month_Dropdown) == 0:
        return dash.no_update
    else :
       df_keyword_1 = df_keyword['월'] == month_Dropdown
       df_keyword_2 =  df_keyword['지역'].isin([area_Dropdown])
       df_keyword_3 = df_keyword[df_keyword_1 & df_keyword_2]
       fig_keyword = px.bar(df_keyword_3, x ='키워드', y = '언급수')

       df_navigation_1 = df_navigation['월'] == month_Dropdown
       df_navigation_2 = df_navigation['시/군/구'].isin([area_Dropdown])
       df_navigation_3 = df_navigation[df_navigation_1 & df_navigation_2]
       fig_navigation = px.bar(df_navigation_3, x = '관광지명', y = '검색건수')
       
       fig_navigation_pie = px.pie(df_navigation_3, names = '소분류 카테고리', hole = 0.4)
       
       df_lodging_1 = df_lodging_food['월'] == month_Dropdown
       df_lodging_2 = df_lodging_food['시/군/구'].isin([area_Dropdown])
       df_lodging_3 = df_lodging_food[df_lodging_1 & df_lodging_2]
       fig_lodging = px.bar(df_lodging_3[df_lodging_3['중분류 카테고리'] == '숙박'], x = '관광지명', y = '검색건수')
       
       fig_lodging_pie = px.pie(df_lodging_3[df_lodging_3['중분류 카테고리'] == '숙박'], names = '소분류 카테고리' , hole = 0.4)
       
       fig_food = px.bar(df_lodging_3[df_lodging_3['중분류 카테고리'] == '음식'], x = '관광지명' , y = '검색건수')

       fig_food_pie = px.pie(df_lodging_3[df_lodging_3['중분류 카테고리'] == '음식'], names = '소분류 카테고리', hole = 0.4)

    return fig_visitor, fig_mention, fig_keyword, fig_navigation, fig_navigation_pie, fig_lodging , fig_lodging_pie, fig_food, fig_food_pie

if __name__ == "__main__":
    app.run_server()