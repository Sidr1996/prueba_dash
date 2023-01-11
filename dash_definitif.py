import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from figures_final import *
import numpy as np


import pandas as pd
import scipy.stats as stat
import plotly.express as px
import prince

data2=data_brut()
f_m_2018=data2.loc[data2["Year"]=="2011"]
f_m_2019=data2.loc[data2["Year"]=="2012"]
f_m_2018=f_m_2018.groupby(["Cause","Genre"]).sum()
f_m_2019=f_m_2019.groupby(["Cause","Genre"]).sum()
f_m_2019.reset_index(inplace=True)
f_m_2018.reset_index(inplace=True)

mm_2018=f_m_2018.loc[f_m_2018["Genre"]=="M"]
ff_2018=f_m_2018.loc[f_m_2018["Genre"]=="F"]

mm_2019=f_m_2019.loc[f_m_2019["Genre"]=="M"]
ff_2019=f_m_2019.loc[f_m_2019["Genre"]=="F"]

causes_final=data2["Cause"].unique().tolist()
len(causes_final)

def p_test(m_use):
    alpha = 0.05
    a, p = stat.fisher_exact(m_use)
    if p < alpha:
        return 'H0 Rejetée'
    else :
        return 0

l1=[]
l2=[]
for i in range(0,len(causes_final)):
    if (((causes_final[i]) in (list(mm_2018["Cause"])) ) & ((causes_final[i])  in (list(ff_2018["Cause"])))) & (((causes_final[i])  in (list(mm_2019["Cause"]))) &((causes_final[i])  in (list(ff_2019["Cause"])))):
        l1.append(causes_final[i])
        t=np.array([[int(mm_2018.Total[mm_2018.Cause==causes_final[i]]),int(ff_2018.Total[ff_2018.Cause==causes_final[i]])],[int(mm_2019.Total[mm_2019.Cause==causes_final[i]]),int(ff_2019.Total[ff_2019.Cause==causes_final[i]])]])
        l2.append(p_test(t))
data_100={
    "Cause":l1,
    "Inference":l2
}
df=pd.DataFrame.from_dict(data_100)





#### test causes 2018 2019
fa_m_2018=data2.loc[data2["Year"]=="2018"]
fa_m_2019=data2.loc[data2["Year"]=="2019"]
fa_m_2018=fa_m_2018.groupby(["Cause","Genre"]).sum()
fa_m_2019=fa_m_2019.groupby(["Cause","Genre"]).sum()
fa_m_2019.reset_index(inplace=True)
fa_m_2018.reset_index(inplace=True)

mma_2018=fa_m_2018.loc[fa_m_2018["Genre"]=="M"]
ffa_2018=fa_m_2018.loc[fa_m_2018["Genre"]=="F"]

mma_2019=fa_m_2019.loc[fa_m_2019["Genre"]=="M"]
ffa_2019=fa_m_2019.loc[fa_m_2019["Genre"]=="F"]

causes_final=data2["Cause"].unique().tolist()
len(causes_final)

def p_test(m_use):
    alpha = 0.05
    a, p = stat.fisher_exact(m_use)
    if p < alpha:
        return 'H0 Rejetée'
    else :
        return 0

l1=[]
l2=[]
for i in range(0,len(causes_final)):
    if (((causes_final[i]) in (list(mma_2018["Cause"])) ) & ((causes_final[i])  in (list(ffa_2018["Cause"])))) & (((causes_final[i])  in (list(mma_2019["Cause"]))) &((causes_final[i])  in (list(ffa_2019["Cause"])))):
        l1.append(causes_final[i])
        t=np.array([[int(mma_2018.Total[mma_2018.Cause==causes_final[i]]),int(ffa_2018.Total[ffa_2018.Cause==causes_final[i]])],[int(mma_2019.Total[mma_2019.Cause==causes_final[i]]),int(ffa_2019.Total[ffa_2019.Cause==causes_final[i]])]])
        l2.append(p_test(t))
dataa_200={
    "Cause":l1,
    "Inference":l2
}
dfa=pd.DataFrame.from_dict(dataa_200)




app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Décès-Belgique", className="display-4"),
        html.Hr(),
        html.P(
            "Analyse statistique des causes de décès", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Analyse Descriptive", href="/page-1", active="exact",id='pag1'),
                dbc.NavLink("Analyse Infèrencielle", href="/page-3", active="exact", id="inference"),
                dbc.NavLink("Analyse Multivariée", href="/page-2", active="exact",id="pag2"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
# def create_sine_graph(length=3, ):
#     fig, ax = plt.subplots()
#     x = np.arange(0, length * np.pi, 0.1)
#     ax.set_title("Sine Wave Form")
#     ax.plot(x, np.sin(x), "r--")
#     return mpl_to_plotly(fig)


 

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])



def render_page_content(pathname):
    if pathname == "/":
        return [html.Div([dbc.Row([
            dbc.Col( dbc.Card( 
    [ dbc.CardHeader("Ingénieur statisticien", style={"font-size":"40px", "font-style":"italic"}),
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="/assets/perfil.jpg",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Samuel Diaz", className="card-title", style={"font-style":"italic"}),
                            html.P(
                                "Je suis passioné par l'analyse de données.",
                                className="card-text",
                            ),
                            html.Small(
                                "Statistique Descriptive. "
                                "Statistique Infèrencielle. "
                                "Statistique Multivariée. "
                                "Machine learning. "
                                "Rstudio. "
                                "Rshiny. "
                                "Power Bi. "
                                "Python.",
                                className="card-text text-muted",
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "400px"},
)
            #     dbc.Card(
            #     dbc.CardBody( [
            #         html.H4("Data", className="card-title"),
            #         dcc.Slider(1, 10, 1, value=3, id="graph-slider"),
            #         dcc.Graph(id='example-graph')
                    
            #     ])
            # ), width="auto"
            ),

            # dbc.Col(dbc.Card(
            #     dbc.CardBody( [
            #         html.H4("Data", className="card-title"),
            #         dcc.Slider(1, 10, 1, value=3, id="graph-slider1"),
            #         dcc.Graph(id='example-graph1')])), width="auto")
            ]),html.Div(id="content2")]), html.Br(),
        dbc.Row([dbc.Card(dbc.CardBody([
            html.H5("Introduction", className="card-title"),
            html.P(
                "Statbel est l'office belge de statistique, collecte, produit et diffuse des chiffres fiables et pertinents sur l'économie, la société et le territoire belge. Dans ce cas il est indispensable de connaître quelles sont les causes de décès les plus habituelles et leur évolution dans le temps. Statbel propose une étude sur ce sujet et en même temps, fournit la base de données sur laquelle l'étude est basée, ce Dashboard se servira de cette base de donnée pour élaborer une analyse descriptive, inférentielle et une analyse multivariée." 
                " Si vous souhaitez connaître un peu plus sur Statbel, cliquez sur le lien ci-dessous.", className="card-text"),
            dbc.CardLink("Statbel", href="https://statbel.fgov.be/fr/themes/population/mortalite-et-esperance-de-vie/causes-de-deces"),
        ]), style={"width": "150rem"},)
            ]), html.Br(),
        dbc.Row([
            dbc.Card(
                dbc.CardBody([
                    html.H3("Base de donnée"),
                    dbc.Table.from_dataframe(data2.head(10), striped=True, bordered=True, hover=True, )
            
                ]))
            
            
            ])
            
            ]
    elif pathname == "/page-1":
        return [html.Div([dbc.Row([
            dbc.Col(dbc.Card(
                dbc.CardBody(
                    dbc.Tabs([
                        dbc.Tab(label="Causes",tab_id="hist"),
                        dbc.Tab(label="Evolution", tab_id="annees")
                    ], id="tabs", active_tab="hist")
                )
            )),
        ]),html.Div(id="content")]),html.Br(),
        dbc.Row([
            html.Br(),
            dbc.Col(dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Age", tab_id="tab-age"),
                    dbc.Tab(label="Genre", tab_id="tab-genre"),
                ],
                id="card-tabs",
                active_tab="tab-age",
            )
        ),
        dbc.CardBody(html.P(id="card-content", className="card-text")),
    ]
)
            
                #  dbc.Card([
                # dcc.Dropdown(id="age", options=["Age","Genre"], value="Age"),
                # dcc.Graph(id="pastel", figure=fig_age_genre())])
            ),
            dbc.Col(dbc.Card([dbc.CardBody([
                dcc.Graph(id="age_genre", figure=fig_ag()),
                html.P("Nous pouvons observer ici le nombre de décès par âge et par sexe, il faut remarquer que seulement dans la catégorie ' 85+ ', c'est-à-dire égale ou supérieure à 85 ans, le sexe féminin prédomine avec une forte différence par rapport au nombre d'hommes, contrairement au reste des catégories où le genre masculin est en tête sans différence très prononcée, néanmoins, en affirmant cela nous aboutirions à de conclusions trop hâtives car nous pourrions recourir à des tests d'hypothèse pour les confirmer ou les rejeter.")])
            ]))
        ]), html.Br(),
        dbc.Row([
            dbc.Col(dbc.Card([
                dcc.Graph(id='region-3', figure=fig_ultimo_dopddown())]))
        ])
        

        
        ]
    elif pathname == "/page-3":
        return [html.Div([
            dbc.Row([dbc.Card([dbc.CardBody([
                html.P("Dans cette section, nous abordons quelques tests d'hypothèses."),
                html.P("Étant donné que nous disposons de nombreuses variables qualitatives (telles que les âges, sexe, maladies, régions et années), il est normal de se poser certaines questions, par exemple: "),
                html.P("Existe-t-il une réelle différence entre la proportion d'hommes et celle de femmes par type de cause de décès ?"),
                html.P("Pour l'instant nous testerons cette questions toutefois nous pouvons tester autant que nous voulions. ")
            ])])
            ])
        ]),html.Br(),
        dbc.Row([
            html.Br(),
            html.H2("Proportion d'hommes et de femmes par type de cause de décès. "),
            html.Br(),
            html.P("Nous tiendrons compte des comparaisons entre les différentes années et sexe, autrement dit, par exemple, nous vérifierons si la proportion d'hommes ou de femmes décédés de Maladie de l'appareil respiratoire en 2012 est la même qu'en 2013. Cependant, nous tiendrons compte de toutes les maladies à l'étude."),
            html.P("Tout d'abord, les hypothèses H0 et H1 doivent être établies.."),
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.P("Test de comparaison entre les années 2011 et 2012"),
                        html.P("H0: La proportion d'hommes décédés est égale"),
                        html.P("H1: La proportion d'hommes décédés n'est pas égale"),
                        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, ),
                        html.P("Ci-dessus, on constate que dans trois cas, l'hypothèse (H0) n'est pas acceptée, ce qui veut dire qu'entre 2011 et 2012, il existe une différence statistiquement significative dans la proportion d'hommes par rapport par rapport aux maladies infectieuses et parasitaires, de l'appareil respiratoire, du sang et des organes hématopoïétiques et certains troubles du système immunitaire. Pour les autres maladies, il n'y a pas de différence statistiquement significative entre les deux années.")
                        ])
                        
                        ])
                
                ,
                ),
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                    html.P("Test de comparaison entre les années 2018 et 2019"),
                    html.P("H0: La proportion d'hommes décédés est égale"),
                    html.P("H1: La proportion d'hommes décédés n'est pas égale"),
                    dbc.Table.from_dataframe(dfa, striped=True, bordered=True, hover=True, ),
                    html.P("Il n'y a qu'un seul cas où l'hypothèse (H0) n'est pas acceptée, nous garderons donc la même interprétation que dans le cas de 2011 et 2012. Entre 2011 et 2012, on remarque une différence statistiquement significative dans la proportion d'hommes par rapport aux maladies de l'appareil respiratoire. Pour toutes les autres maladies, il n'y a pas de différence statistiquement significative entre les deux années.")

                    ])])
            )



        ]),html.Br(),
        ]
    elif pathname == "/page-2":
        return [html.Div([
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id="AC-age_genre", figure=fig5),
                        html.P("Si nous examinons la catégorie 'Age_85+', nous constatons que les maladies causant le plus de décès dans cette catégorie sont les maladies de l'appareil circulatoire, les Maladies de l'appareil respiratoire, les Maladies de l'appareil génito-urinaire et Troubles mentaux et du comportement. Des conclusions similaires peuvent être formulées en examinant les maladies en fonction des différentes catégories d'âge. Dans le cas de l'opposé par coordonnées, on peut dire qu'il n'y a pas de relation.")
                    ])
                ])),
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='Ac-genre_age', figure=fig6),
                        html.P("On observe que la première composante discrimine le sexe des individus, ce qui signifie qu'à droite on trouve le sexe masculin et à gauche le sexe féminin. D'une part, on peut noter qu'il existe une similitude entre le sexe féminin et les Maladies infectieuses et parasitaires, les Maladies du système nerveux et des organes des sens. Par ailleurs, il convient de noter qu'il existe une forte relation avec les tumeurs. ")
                ])
                ])
                )
            ])
        ]),html.Br(),
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id="ACM", figure=fig4),
                    html.P("Dans le graphique ci-dessus, nous appliquons une analyse des correspondances multiples, toutes les variables d'intérêt seront étudiées en même temps. Nous observons que lorsque nous considérons les régions, la Région de Bruxelles-Capitale et la Région flamande présentent des similitudes, nous pourrions dire qu'il existe une relation avec les maladies du système nerveux et des organes des sens et les maladies du système circulatoire, ainsi qu'une relation avec le sexe féminin. Par ailleurs, nous avons la Région wallonne, qui est liée aux Maladies infectieuses et parasitaires, les Maladies de l'appareil digestif, des Tumeurs.")
                ])
            ])
        )
        ]
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

@app.callback(Output("region-3", "figure"),
[
    Input("drop-c2","value")
]
)

def region_option (option):
    return fig_ultimo_dopddown("Cause-CD_Region")
# @app.callback(Output("example-graph","figure"),
# [
#     Input("graph-slider","value"),
    
#     ])
# @app.callback(Output("example-graph1","figure"),
# [
#     Input("graph-slider1","value")
    
#     ])
# def update_graph(slider_value):
#     return create_sine_graph(slider_value)



@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "hist":
        return html.Div([
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(id='graph_maladies', figure=fig_cause_dece()),
                    html.P("Le graphique ci-dessus nous indique la quantité de personnes mortes selon le type de décès"),
                    html.P("On peut donc constater que la cause de décès qui est à la tête ce sont les Maladies d l'appareil circulatoire suivi des Tumeurs ")
                    
                    
                    
                    ])
                ), html.Div(id="div_3")])
    elif at == "annees":
        return html.Div([
            dbc.Card(
                dbc.CardBody([
                    # dcc.Dropdown(["friends","minutes"], id="drop-c", value="friends"),
                    dcc.Graph(id='graph', figure=fig_cause_year()),
                    html.P("Ce graphique donne un aperçu clair de l'évolution des causes de décès au cours des années. Cela permet en outre de corroborer ce que le graphique précédant a montré. Autrement dit, les causes les plus courantes sont les maladies du système circulatoire et les tumeurs. Il faut souligner le fait que la courbe des tumeurs est restée constante ces dernières années, tandis que la cause des maladies du système circulatoire n'a que légèrement diminué.")
                    
                    
                    ])
                ), html.Div(id="div_2")])
        
    return html.P("This shouldn't ever be displayed...")    




@app.callback(
    Output("card-content", "children"), [Input("card-tabs", "active_tab")]
)
def tab_content(active_tab):
    if active_tab == "tab-age":
        return html.Div([
            dbc.Card([dbc.CardHeader("Graphique Proportion de décès par age"),
                dbc.CardBody([
                    dcc.Graph(id='age_graphique', figure=fig_age_genre("Age")),
                    html.P("Selon le graphique, les personnes appartenant à la catégorie  '85 +' occupent la plus grande proportion, suivi de la catégorie '75-84'. "
                    "Autrement dit, plus âgés sont les individus il y a moins de posibilités de se remettre."),
                    
                    
                    
                    ])
                ]), html.Div(id="div_3")])
    elif active_tab == "tab-genre":
        return html.Div([
            dbc.Card([dbc.CardHeader("Grafique Proportion par genre "),
                dbc.CardBody([
                    # dcc.Dropdown(["friends","minutes"], id="drop-c", value="friends"),
                    dcc.Graph(id='graph_genre', figure=fig_age_genre("Genre")),
                    html.P("Le graphique révèle que le pourcentage de femmes et d'hommes est quasiment égal. Ces informations nous incitent à savoir si la proportion de femmes et d'hommes diffère selon la nature des causes de décès. Pour y répondre, nous proposons des tests d'hypothèse présentés ci-après.")
                    
                    
                    ])
                ]), html.Div(id="div_2")])
        
    return html.P("This shouldn't ever be displayed...")  


if __name__ == "__main__":
    app.run_server(debug=True)
