
import  pandas as pd
import numpy as np
import plotly.express as px
import prince
import gspread

import pandas as pd
from gspread_dataframe import get_as_dataframe

credentials={
  "type": "service_account",
  "project_id": "dashboardcv",
  "private_key_id": "e2d3136b06c56edce23d297f06a0cdd59af5735d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCmmnuwnR18+7wY\nU1XxN/ty8BViY3y1gx7+GIsis1ynd2ek8QPyVW8biDVgLOBzUZE3sZduZIJpmmLA\nYDJa1+Hr2ppXuzIy8kDpesokm7wr7htxJzlNkM2Q/puvUA6NToLtr9LldcuVISlR\nY1J0UMMfoXNH20ulew7e0tvQhxFeZuBTj8Ws+NKwZX/yquzAc3OzzPly32wC8bfx\nN1YTeDy/HxMG3JfgrB0o44NVVQv4ALaJBhk1aacjwbaoNMCnP4m9FpKJbt5S3Plu\ncF6YLDhcRtQ5TgK4Fj0QuCp+Rw67nPGHUm4baneDMqt/fc74Ic8qv+coAolFowsY\nLtyUZwtxAgMBAAECggEABmcqCU3kh/zpy/qJ80keRBrXi448yQIW0xew4z7G+RW0\n+UkdCHeBm2qG+KEI6E2yedQ8uGyq+XGKSY/453ZkE6s1YtlKMtyOI5sJQVJt7zdJ\nvTXPdTxzNhce9yQpxwMFM6rd/V0jW6IoYx0g2mEPOrw7AMA8HkpGNkie05sZTwov\ntS8g39mRGUCcCkLN9xg7bhbHU3ypyUDH6sqiAXjzlvxGTo/3qUMgVAM56aZ+7Ec3\n8uG6Ze4YkNyExf3NuKMvrMCLGGq3o84rxUgaHsJiX5Xub47si5yfxdZz2ijwGrFK\nHnI5HIUwJuw1WL/5l+woHFShnsvNJ1rwAUHEeKFu9QKBgQDh7XVHh2c3Jofe/M5v\nUugJHquMc2jOVqM2xDNkDwcLERVt50CSxsjiVM92wzEKMQQ9lhZi7+FIek+3MesW\n9UldrMrH9f6QHsaZE2MiCR7uIQ8FMyMIN2UGMAjw07Noq+qQBGS73vXfg10F9lmg\n/xfj1kpcSIJ3UUi0nP15TcNALQKBgQC8x4o2SoUjA7vN8sBwu8KaZVbyWFI6LaJD\nHl/fNCPXaBLqR3LvgVNaOGok0vGp1TN8eH7qn9ahmDwKPBEhdK739Ibbuzk2SneI\nyXF2GY7qVtUdxNrAG7Ksp32H0HVIcJF+rtOezHIWC1V0PuM/vpJW0CcvTgoMZjqK\nF+p/ah7+1QKBgBPiWlgZSrRH591wUprpqRJkaKTL44WFioffbMZ5rB0FO+WYXM6O\nQE/rNvc05rQG7GCfPQkoI6PFYA63jgFPRU3BT3eZ5vW4P7JpSmhMdTRwJGpIveST\nO4j34VGQ0FF+D/7s5BDE5s7tONq1e933lZqv2YuVtiXaOZPr3UM33N9hAoGABfrc\nKfQaW42WuWNjLS8FbxaetnaNxEIFzdJ8fvmL2Rr23mz8+xFBrq3yzs/Pz+1tABhh\nDNWbWusTm89jS4gCsuAQFY3MtieNucuHyJHusQWnIpZFx6gY9NcpZs/3px/JvBWV\npoYbZw9c2Z3UXQSQZieZ1inGr7XdTNqNFxQpfzECgYEAhCqYspDxrSZhJy6xndGa\nuDPpP8T5BoOqKzTs4nRNNFFNbzbUHRdB9mu0ZaC5Osb6R/Hg7Td4Yqk2JLQF4MLZ\nZYjtJEq3HDJzfmvXmQSQCVdbbJiiLpg0Vx8YM8+MRnHdXllhr4oxGCklwGbRWS1n\nUQ/yWJ+cMirIBUtdARf0I6o=\n-----END PRIVATE KEY-----\n",
  "client_email": "drive-577@dashboardcv.iam.gserviceaccount.com",
  "client_id": "107779434677742178563",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/drive-577%40dashboardcv.iam.gserviceaccount.com"
}

gc = gspread.service_account_from_dict(credentials)
wks = gc.open("cause").sheet1
datasss=wks.get_all_values()
headers=datasss.pop(0)
dfsss=pd.DataFrame(datasss, columns=headers)
data2=dfsss.iloc[:,[0,2,3,4,5,6,7,8]]





# data2=pd.read_excel("opendata_COD_cause (1).xlsx")

# data2=data2.iloc[:,[0,2,3,4,5,6,7,8]]
data2.columns=["CD_maladie","Cause","CD_Region","Month","Year","Age","Genre","Total"]
data2["Total"]=data2["Total"].astype('int')
data2= data2[data2['Cause'].notna()]
data2.drop(data2[data2["Cause"]=='#N/A'].index, inplace=True)
data_2=pd.DataFrame(data2.values.repeat(data2["Total"], axis=0), columns=data2.columns)
data2['Year']=data2['Year'].astype('category')
data2["CD_Region"]=data2["CD_Region"].astype('category')
data2["Age"]=data2["Age"].astype('category')
data2["CD_Region"]= data2["CD_Region"] .cat.rename_categories(["Region_Flamande",
"Region Wallonne","Region_Brux_Capit"])

data_2['Year']=data_2['Year'].astype('category')
data_2["CD_Region"]=data_2["CD_Region"].astype('category')
data_2["Age"]=data_2["Age"].astype('category')

data_2["CD_Region"]= data_2["CD_Region"] .cat.rename_categories(["Region_Flamande",
"Region Wallonne","Region_Brux_Capit"])

def data_brut():
    return data2

maladies=data2.groupby("Cause").sum()
maladies["Cause"]=maladies.index
maladies=maladies.sort_values(by=["Total"])
#fig=px.bar(maladies,x='Total',y="Cause", title="Cause de Décès",text_auto='.8s', height=600)

def fig_cause_dece():
    fig=px.bar(maladies,x='Total',y="Cause", title="Cause de Décès", height=600)
    return fig



maladies2=data2.groupby(["Cause","Year"]).sum()
maladies2.reset_index(inplace=True)

#fig2=px.line(maladies2,x="Year", y="Total", color="Cause", title="")


def fig_cause_year():
    fig=px.line(maladies2,x="Year", y="Total", color="Cause", title="Evolution des causes par ans")
    return fig


maladies3=data2.groupby(["Age","Genre"]).sum()
maladies3.reset_index(inplace=True)
def fig_age_genre(nom="Age"):
    fig=px.pie(maladies3,values="Total", names=nom, hole=.7)
    return fig

maladies4=data2.groupby(["Age","Genre"]).sum()
maladies4.reset_index(inplace=True)
#fig3=px.bar(maladies4, x="Age", y="Total", color="Genre",barmode="group", width=500)

def fig_ag():
    fig=px.bar(maladies4, x="Age", y="Total", color="Genre",barmode="group", width=500, title="Graphique Age vs Genre")
    return fig


data3=data2
region_2=data3.groupby(["Cause","CD_Region"]).sum()
region_2.reset_index(inplace=True)
# fig7=px.bar(region_2, x="Cause", y="Total", color="CD_Region",barmode="group", height=800,color_discrete_map={
#                 "Region_Flamande": "red",
#                 "Region Wallonne": "green",
#                 "Region_Brux_Capit": "goldenrod",})
data4=data2
region_3=data4.groupby(["CD_Region","Year"]).sum()
region_3.reset_index(inplace=True)
#fig8=px.line(region_3, x='Year',y='Total', color="CD_Region")


def fig_ultimo_dopddown(optiones="Cause-CD_Region"):
    if optiones=="Cause-CD_Region":
        fig7=px.bar(region_2, x="Cause", y="Total", color="CD_Region",barmode="group", title="Cuases vs Region",height=800,color_discrete_map={
                "Region_Flamande": "red",
                "Region Wallonne": "green",
                "Region_Brux_Capit": "goldenrod",})
        return fig7
    elif optiones=="CD_Region-Year":
        fig9=px.line(region_3, x='Year',y='Total', color="CD_Region")
        return fig9







a=data_2[["Genre","Age","Cause","CD_Region"]]
ca= prince.MCA(n_components=2,
n_iter=3,copy=True,check_input=True,engine='auto',random_state=42)



ca = ca.fit(a)
cordonnees=ca.column_coordinates(a)

cordonnees["masa"]=ca.col_masses_

cordonnees["categories"]=cordonnees.index


type_cordonnees=[]
for i in cordonnees["categories"]:
    if  "Genre" in i:
        type_cordonnees.append("Genre")
    elif "Age"  in i:
        type_cordonnees.append("Age")
    elif "Cause" in i:
        type_cordonnees.append("Cause")
    elif "CD_Region" in i:
        type_cordonnees.append("Region")


cordonnees["Type"]=type_cordonnees

cordonnees.columns=["cord_x","cord_y","masa","categories","type_cat"]        
cordonnees=cordonnees.drop("Cause_Codes d'utilisation particulière")
cordonnees=cordonnees.round(2)

def ACM_graph():
    fig4= px.scatter(cordonnees, x="cord_x", y="cord_y", color="type_cat",
                 hover_name="categories", size_max=60, title='Analyse de Correspondance Multiple' )
    fig4.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    fig4.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    return fig4


b=data_2[["Age","Cause"]]
cb= prince.MCA(n_components=2,
n_iter=3,copy=True,check_input=True,engine='auto',random_state=42)



cb = cb.fit(b)
cordonneesb=cb.column_coordinates(b)

cordonneesb["masa"]=cb.col_masses_

cordonneesb["categories"]=cordonneesb.index


type_cordonneesb=[]
for i in cordonneesb["categories"]:
    if  "Genre" in i:
        type_cordonneesb.append("Genre")
    elif "Age"  in i:
        type_cordonneesb.append("Age")
    elif "Cause" in i:
        type_cordonneesb.append("Cause")
    elif "CD_Region" in i:
        type_cordonneesb.append("Region")


cordonneesb["Type"]=type_cordonneesb

cordonneesb.columns=["cord_x","cord_y","masa","categories","type_cat"]        
cordonneesb=cordonneesb.drop("Cause_Codes d'utilisation particulière")
cordonneesb=cordonneesb.round(2)

def ACS_age_cause():
    fig5 = px.scatter(cordonneesb, x="cord_x", y="cord_y", color="type_cat",
                 hover_name="categories", size_max=60,title='Analyse de Correspondance Simple Age-Cause' ,width=500)
    fig5.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    fig5.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    return fig5


c=data_2[["Genre","Cause"]]
cb= prince.MCA(n_components=2,
n_iter=3,copy=True,check_input=True,engine='auto',random_state=42)



cc = cb.fit(c)
cordonneesc=cb.column_coordinates(c)

cordonneesc["masa"]=cc.col_masses_

cordonneesc["categories"]=cordonneesc.index


type_cordonneesc=[]
for i in cordonneesc["categories"]:
    if  "Genre" in i:
        type_cordonneesc.append("Genre")
    elif "Age"  in i:
        type_cordonneesc.append("Age")
    elif "Cause" in i:
        type_cordonneesc.append("Cause")
    elif "CD_Region" in i:
        type_cordonneesc.append("Region")


cordonneesc["Type"]=type_cordonneesc

cordonneesc.columns=["cord_x","cord_y","masa","categories","type_cat"]        
cordonneesc=cordonneesc.drop("Cause_Codes d'utilisation particulière")
cordonneesc=cordonneesc.round(2)


def ACS_genre_cause():
    fig6 = px.scatter(cordonneesc, x="cord_x", y="cord_y", color="type_cat",
                 hover_name="categories", size_max=60,title='Analyse de Correspondance Simple Genre-Cause',width=500 )
    fig6.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    fig6.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
    return fig6
#




