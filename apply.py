from os import access
import mysql.connector
import streamlit as st  # web development
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import time  # to simulate a real time data, time loop
import plotly.express as px  # interactive charts
import datetime
# st.set_page_config(page_title="My App", layout='wide')
st.set_page_config(
    page_title='Monitoring des PDA',
    page_icon='✅',
    layout='wide'
)

# ============================== BD CONNEXION=================================
config = {
    'user': 'STL',
    'password': 'stl@elisath',
    'host': '10.60.0.1',
    'port': '5454',
    'database': 'elisath_gestion_abo',
    'use_pure': True,
    'charset': 'utf8'
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor(buffered=True)
# ============================== BD CONNEXION=================================


# ============================= UTILS =======================================
def genere_alert(statut):
    if statut == 1:
        return "perdu"
    else:
        return "connecte"


def generator(tourniquet):
    query = f"SELECT * FROM elisath_gestion_abo.Supervision sv WHERE sv.Nom IN ('{tourniquet}') ORDER BY sv.DateHeure DESC"
    data = pd.read_sql(query, cnx)
    data_droped = data.drop_duplicates(
        subset=["Nom"], keep='first').reset_index(drop=True)
    statut = data_droped.loc[data_droped.Nom == tourniquet, "Code"].values[0]
    last_time = data_droped.loc[data_droped.Nom ==
                                tourniquet, "DateHeure"].values[0]
    alerte = genere_alert(statut)
    print(f"{tourniquet} --- {alerte} ---- {last_time}")
    return alerte, statut, last_time


def get_stats(pda):
    badge_ok = 0
    badge_interdit = 0
    badge_perime = 0
    solde_epuise = 0
    article_inconnu = 0
    total = 0

    query = f" SELECT tb.Message, COUNT(tb.Message)'Compte' FROM elisath_gestion_abo.TestBadge tb  WHERE tb.Acces = '{pda}'  AND DAY(tb.DateHeure) = DAY(CURDATE()) AND MONTH(tb.DateHeure) = MONTH(CURDATE()) AND YEAR(tb.DateHeure) = YEAR(CURDATE()) GROUP BY 1 "
    donnee = pd.read_sql(query, cnx)
    try:
        badge_ok = donnee.loc[donnee.Message == 'BADGE OK', 'Compte'].values[0]
    except Exception as e:
        badge_ok = 0
    try:
        badge_interdit = donnee.loc[donnee.Message ==
                                    'BADGE INTERDIT', 'Compte'].values[0]
    except Exception as e:
        badge_interdit = 0
    try:
        badge_perime = donnee.loc[donnee.Message ==
                                  'BADGE PERIME', 'Compte'].values[0]
    except Exception as e:
        badge_perime = 0
    try:
        solde_epuise = donnee.loc[donnee.Message ==
                                  'SOLDE EPUISE', 'Compte'].values[0]
    except Exception as e:
        solde_epuise = 0
    try:
        article_inconnu = donnee.loc[donnee.Message ==
                                     'ARTICLE INCONNU', 'Compte'].values[0]
    except Exception as e:
        article_inconnu = 0

    print(pda, badge_ok, badge_interdit,
          badge_perime, solde_epuise, article_inconnu)
    total = badge_ok + badge_interdit + badge_perime + solde_epuise + article_inconnu
    return badge_ok, badge_interdit, badge_perime, solde_epuise, article_inconnu, total
# ============================= UTILS ========================================


# ============================= ALERTE =======================================
# ============================= ALERTE =======================================
satut_TRE_PDA_FAM_215 = 1
time_TRE_PDA_FAM_215 = 0
alert_TRE_PDA_FAM_215 = "perdu"

satut_TRE_PDA_COP_743 = 1
time_TRE_PDA_COP_743 = 0
alert_TRE_PDA_COP_743 = "perdu"

satut_AZI_PDA_COP_057 = 1
time_AZI_PDA_COP_057 = 0
alert_AZI_PDA_COP_057 = "perdu"

satut_AZI_PDA_FAM_850 = 1
time_AZI_PDA_FAM_850 = 0
alert_AZI_PDA_FAM_850 = "perdu"

satut_MPO_PDA_COP_006 = 1
time_MPO_PDA_COP_006 = 0
alert_MPO_PDA_COP_006 = "perdu"

satut_MPO_PDA_COP_735 = 1
time_MPO_PDA_COP_735 = 0
alert_MPO_PDA_COP_735 = "perdu"

satut_MPO_PDA_FAM_617 = 1
time_MPO_PDA_FAM_617 = 0
alert_MPO_PDA_FAM_617 = "perdu"

satut_KOU_PDA_FAM_153 = 1
time_KOU_PDA_FAM_153 = 0
alert_KOU_PDA_FAM_153 = "perdu"

satut_KOU_PDA_FAM_575 = 1
time_KOU_PDA_FAM_575 = 0
alert_KOU_PDA_FAM_575 = "perdu"

satut_ABO_PDA_FAM_975 = 1
time_ABO_PDA_FAM_975 = 0
alert_ABO_PDA_FAM_975 = "perdu"

satut_ABO_PDA_FAM_932 = 1
time_ABO_PDA_FAM_932 = 0
alert_ABO_PDA_FAM_932 = "perdu"

satut_PLA_PDA_FAM_211 = 1
time_PLA_PDA_FAM_211 = 0
alert_PLA_PDA_FAM_211 = "perdu"

satut_PLA_PDA_FAM_354 = 1
time_PLA_PDA_FAM_354 = 0
alert_PLA_PDA_FAM_354 = "perdu"

satut_PLA_PDA_COP_701 = 1
time_PLA_PDA_COP_701 = 0
alert_PLA_PDA_COP_701 = "perdu"

# TQT
satut_TRE_TOUR_STID_60_57 = 1
time_TRE_TOUR_STID_60_57 = 0
alert_TRE_TOUR_STID_60_57 = "perdu"

satut_TRE_TOUR_STID_60_58 = 1
time_TRE_TOUR_STID_60_58 = 0
alert_TRE_TOUR_STID_60_58 = "perdu"

satut_PLA_TOUR_LAN_42_7 = 1
time_PLA_TOUR_LAN_42_7 = 0
alert_PLA_TOUR_LAN_42_7 = "perdu"

satut_PLA_TOUR_STID_42_6 = 1
time_PLA_TOUR_STID_42_6 = 0
alert_PLA_TOUR_STID_42_6 = "perdu"

satut_PLA_KOU_TOUR_LAND_100_7 = 1
time_PLA_KOU_TOUR_LAND_100_7 = 0
alert_PLA_KOU_TOUR_LAND_100_7 = "perdu"

satut_PLA_KOU_TOUR_STID_100_6 = 1
time_PLA_KOU_TOUR_STID_100_6 = 0
alert_PLA_KOU_TOUR_STID_100_6 = "perdu"

satut_PLA_MPO_TOUR_LAND_99_6 = 1
time_PLA_MPO_TOUR_LAND_99_6 = 0
alert_PLA_MPO_TOUR_LAND_99_6 = "perdu"

satut_MPO_TOUR_STID_99_7 = 1
time_MPO_TOUR_STID_99_7 = 0
alert_MPO_TOUR_STID_99_7 = "perdu"


badge_ok_TRE_PDA_FAM_215, badge_interdit_TRE_PDA_FAM_215, badge_perime_TRE_PDA_FAM_215, solde_epuise_TRE_PDA_FAM_215, article_inconnu_TRE_PDA_FAM_215, total_TRE_PDA_FAM_215 = 0, 0, 0, 0, 0, 0
badge_ok_TRE_PDA_COP_743, badge_interdit_TRE_PDA_COP_743, badge_perime_TRE_PDA_COP_743, solde_epuise_TRE_PDA_COP_743, article_inconnu_TRE_PDA_COP_743, total_TRE_PDA_COP_743 = 0, 0, 0, 0, 0, 0
badge_ok_AZI_PDA_COP_057, badge_interdit_AZI_PDA_COP_057, badge_perime_AZI_PDA_COP_057, solde_epuise_AZI_PDA_COP_057, article_inconnu_AZI_PDA_COP_057, total_AZI_PDA_COP_057 = 0, 0, 0, 0, 0, 0
badge_ok_AZI_PDA_FAM_850, badge_interdit_AZI_PDA_FAM_850, badge_perime_AZI_PDA_FAM_850, solde_epuise_AZI_PDA_FAM_850, article_inconnu_AZI_PDA_FAM_850, total_AZI_PDA_FAM_850 = 0, 0, 0, 0, 0, 0
badge_ok_KOU_PDA_FAM_153, badge_interdit_KOU_PDA_FAM_153, badge_perime_KOU_PDA_FAM_153, solde_epuise_KOU_PDA_FAM_153, article_inconnu_KOU_PDA_FAM_153, total_KOU_PDA_FAM_153 = 0, 0, 0, 0, 0, 0
badge_ok_KOU_PDA_FAM_575, badge_interdit_KOU_PDA_FAM_575, badge_perime_KOU_PDA_FAM_575, solde_epuise_KOU_PDA_FAM_575, article_inconnu_KOU_PDA_FAM_575, total_KOU_PDA_FAM_575 = 0, 0, 0, 0, 0, 0
badge_ok_MPO_PDA_COP_006, badge_interdit_MPO_PDA_COP_006, badge_perime_MPO_PDA_COP_006, solde_epuise_MPO_PDA_COP_006, article_inconnu_MPO_PDA_COP_006, total_MPO_PDA_COP_006 = 0, 0, 0, 0, 0, 0
badge_ok_MPO_PDA_COP_735, badge_interdit_MPO_PDA_COP_735, badge_perime_MPO_PDA_COP_735, solde_epuise_MPO_PDA_COP_735, article_inconnu_MPO_PDA_COP_735, total_MPO_PDA_COP_735 = 0, 0, 0, 0, 0, 0
badge_ok_MPO_PDA_FAM_617, badge_interdit_MPO_PDA_FAM_617, badge_perime_MPO_PDA_FAM_617, solde_epuise_MPO_PDA_FAM_617, article_inconnu_MPO_PDA_FAM_617, total_MPO_PDA_FAM_617 = 0, 0, 0, 0, 0, 0
badge_ok_KOU_PDA_FAM_575, badge_interdit_KOU_PDA_FAM_575, badge_perime_KOU_PDA_FAM_575, solde_epuise_KOU_PDA_FAM_575, article_inconnu_KOU_PDA_FAM_575, total_KOU_PDA_FAM_575 = 0, 0, 0, 0, 0, 0
badge_ok_ABO_PDA_FAM_975, badge_interdit_ABO_PDA_FAM_975, badge_perime_ABO_PDA_FAM_975, solde_epuise_ABO_PDA_FAM_975, article_inconnu_ABO_PDA_FAM_975, total_ABO_PDA_FAM_975 = 0, 0, 0, 0, 0, 0
badge_ok_ABO_PDA_FAM_932, badge_interdit_ABO_PDA_FAM_932, badge_perime_ABO_PDA_FAM_932, solde_epuise_ABO_PDA_FAM_932, article_inconnu_ABO_PDA_FAM_932, total_ABO_PDA_FAM_932 = 0, 0, 0, 0, 0, 0
badge_ok_PLA_PDA_FAM_211, badge_interdit_PLA_PDA_FAM_211, badge_perime_PLA_PDA_FAM_211, solde_epuise_PLA_PDA_FAM_211, article_inconnu_PLA_PDA_FAM_211, total_PLA_PDA_FAM_211 = 0, 0, 0, 0, 0, 0
badge_ok_PLA_PDA_FAM_354, badge_interdit_PLA_PDA_FAM_354, badge_perime_PLA_PDA_FAM_354, solde_epuise_PLA_PDA_FAM_354, article_inconnu_PLA_PDA_FAM_354, total_PLA_PDA_FAM_354 = 0, 0, 0, 0, 0, 0
badge_ok_PLA_PDA_COP_701, badge_interdit_PLA_PDA_COP_701, badge_perime_PLA_PDA_COP_701, solde_epuise_PLA_PDA_COP_701, article_inconnu_PLA_PDA_COP_701, total_PLA_PDA_COP_701 = 0, 0, 0, 0, 0, 0
# TQT
badge_ok_TRE_TOUR_STID_60_57, badge_interdit_TRE_TOUR_STID_60_57, badge_perime_TRE_TOUR_STID_60_57, solde_epuise_TRE_TOUR_STID_60_57, article_inconnu_TRE_TOUR_STID_60_57, total_TRE_TOUR_STID_60_57 = 0, 0, 0, 0, 0, 0
badge_ok_TRE_TOUR_STID_60_58, badge_interdit_TRE_TOUR_STID_60_58, badge_perime_TRE_TOUR_STID_60_58, solde_epuise_TRE_TOUR_STID_60_58, article_inconnu_TRE_TOUR_STID_60_58, total_TRE_TOUR_STID_60_58 = 0, 0, 0, 0, 0, 0

badge_ok_PLA_TOUR_LAN_42_7, badge_interdit_PLA_TOUR_LAN_42_7, badge_perime_PLA_TOUR_LAN_42_7, solde_epuise_PLA_TOUR_LAN_42_7, article_inconnu_PLA_TOUR_LAN_42_7, total_PLA_TOUR_LAN_42_7 = 0, 0, 0, 0, 0, 0
badge_ok_PLA_TOUR_STID_42_6, badge_interdit_PLA_TOUR_STID_42_6, badge_perime_PLA_TOUR_STID_42_6, solde_epuise_PLA_TOUR_STID_42_6, article_inconnu_PLA_TOUR_STID_42_6, total_PLA_TOUR_STID_42_6 = 0, 0, 0, 0, 0, 0

badge_ok_KOU_TOUR_LAND_100_7, badge_interdit_KOU_TOUR_LAND_100_7, badge_perime_KOU_TOUR_LAND_100_7, solde_epuise_KOU_TOUR_LAND_100_7, article_inconnu_KOU_TOUR_LAND_100_7, total_KOU_TOUR_LAND_100_7 = 0, 0, 0, 0, 0, 0
badge_ok_KOU_TOUR_STID_100_6, badge_interdit_KOU_TOUR_STID_100_6, badge_perime_KOU_TOUR_STID_100_6, solde_epuise_KOU_TOUR_STID_100_6, article_inconnu_KOU_TOUR_STID_100_6, total_KOU_TOUR_STID_100_6 = 0, 0, 0, 0, 0, 0

badge_ok_MPO_TOUR_LAND_99_6, badge_interdit_MPO_TOUR_LAND_99_6, badge_perime_MPO_TOUR_LAND_99_6, solde_epuise_MPO_TOUR_LAND_99_6, article_inconnu_MPO_TOUR_LAND_99_6, total_MPO_TOUR_LAND_99_6 = 0, 0, 0, 0, 0, 0
badge_ok_MPO_TOUR_STID_99_7, badge_interdit_MPO_TOUR_STID_99_7, badge_perime_MPO_TOUR_STID_99_7, solde_epuise_MPO_TOUR_STID_99_7, article_inconnu_MPO_TOUR_STID_99_7, total_MPO_TOUR_STID_99_7 = 0, 0, 0, 0, 0, 0

# BIBLIOTHEQUES CSS
st.markdown("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
""", unsafe_allow_html=True)
st.markdown("""
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.0/css/all.min.css">
""", unsafe_allow_html=True)
# BIBLIOTHEQUES CSS


def plot_detail(tourniquet, statut, total, ok, interdit, perime, inconnu, epuise):
    details_disconnected = f"""<ul class="list-group" style="border:none">
                    <li class="list-group-item" style="border:none; padding-bottom:0px; margin-bottom:0px">
                        <span style="font-size:15px; font-weight:800; padding-top:0px; margin-top:0px">{tourniquet}<span>
                    </li>
                    <li class="list-group-item" style="border:none; padding-bottom:0px; margin-bottom:0px">
                        <span style="font-size:45px">📠<span> <span style="font-size:15px">🔴<span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#2ecc71">
                            Total : {total}
                        <span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#2980b9">
                            Badge OK : {ok}
                        <span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#c0392b">
                            Badge interdit : {interdit}
                        <span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#c0392b">
                            Badge périmé : {perime}
                        <span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#f1c40f">
                            Article inconnu : {inconnu}
                        <span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#f1c40f">
                            Solde épuisé : {epuise}
                        <span>
                    </li>
                </ul>"""
    details_connected = f"""<ul class="list-group" style="border:none">
                    <li class="list-group-item" style="border:none; padding-bottom:0px; margin-bottom:0px">
                        <span style="font-size:15px; font-weight:800; padding-top:0px; margin-top:0px">{tourniquet}<span>
                    </li>
                    <li class="list-group-item" style="border:none; padding-bottom:0px; margin-bottom:0px">
                        <span style="font-size:45px">📠<span> <span style="font-size:15px">🟢<span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#2ecc71">
                            Total : {total}
                        <span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#2980b9">
                            Badge OK : {ok}
                        <span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#c0392b">
                            Badge interdit : {interdit}
                        <span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#c0392b">
                            Badge périmé : {perime}
                        <span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#f1c40f">
                            Article inconnu : {inconnu}
                        <span>
                    </li>
                    <li class="list-group-item" style="border:none">
                        <span style="font-size:12px; font-weight:800; padding-top:0px; margin-top:0px; color:#f1c40f">
                            Solde épuisé : {epuise}
                        <span>
                    </li>
                </ul>"""
    if statut == 0:
        return details_connected
    else:
        return details_disconnected


# VISUEL CREATION
placeholder = st.empty()

while True:
    cnx = mysql.connector.connect(**config)
    print("****************************************** ALERTE **********************************")
    print("****************************************** ALERTE **********************************")
    alert_TRE_PDA_FAM_215, satut_TRE_PDA_FAM_215, time_TRE_PDA_FAM_215 = generator(
        "TRE_PDA_FAM_215")

    alert_TRE_PDA_COP_743, satut_TRE_PDA_COP_743, time_TRE_PDA_COP_743 = generator(
        "TRE_PDA_COP_743")
    alert_AZI_PDA_COP_057, satut_AZI_PDA_COP_057, time_AZI_PDA_COP_057 = generator(
        "AZI_PDA_COP_057")
    alert_AZI_PDA_FAM_850, satut_AZI_PDA_FAM_850, time_AZI_PDA_FAM_850 = generator(
        "AZI_PDA_FAM_850")
    alert_MPO_PDA_COP_006, satut_MPO_PDA_COP_006, time_MPO_PDA_COP_006 = generator(
        "MPO_PDA_COP_006")
    alert_MPO_PDA_COP_735, satut_MPO_PDA_COP_735, time_MPO_PDA_COP_735 = generator(
        "MPO_PDA_COP_735")
    alert_MPO_PDA_FAM_617, satut_MPO_PDA_FAM_617, time_MPO_PDA_FAM_617 = generator(
        "MPO_PDA_FAM_617")
    alert_KOU_PDA_FAM_153, satut_KOU_PDA_FAM_153, time_KOU_PDA_FAM_153 = generator(
        "KOU_PDA_FAM_153")
    alert_KOU_PDA_FAM_575, satut_KOU_PDA_FAM_575, time_KOU_PDA_FAM_575 = generator(
        "KOU_PDA_FAM_575")
    alert_ABO_PDA_FAM_975, satut_ABO_PDA_FAM_975, time_ABO_PDA_FAM_975 = generator(
        "ABO_PDA_FAM_975")
    alert_ABO_PDA_FAM_932, satut_ABO_PDA_FAM_932, time_ABO_PDA_FAM_932 = generator(
        "ABO_PDA_FAM_932")
    alert_PLA_PDA_FAM_211, satut_PLA_PDA_FAM_211, time_PLA_PDA_FAM_211 = generator(
        "PLA_PDA_FAM_211")
    alert_PLA_PDA_FAM_354, satut_PLA_PDA_FAM_354, time_PLA_PDA_FAM_354 = generator(
        "PLA_PDA_FAM_354")
    alert_PLA_PDA_COP_701, satut_PLA_PDA_COP_701, time_PLA_PDA_COP_701 = generator(
        "PLA_PDA_COP_701")
    # TQT
    alert_TRE_TOUR_STID_60_57, satut_TRE_TOUR_STID_60_57, time_TRE_TOUR_STID_60_57 = generator(
        "TRE_TOUR_STID_60_57")
    alert_TRE_TOUR_STID_60_58, satut_TRE_TOUR_STID_60_58, time_TRE_TOUR_STID_60_58 = generator(
        "TRE_TOUR_STID_60_58")
    alert_PLA_TOUR_LAN_42_7, satut_PLA_TOUR_LAN_42_7, time_PLA_TOUR_LAN_42_7 = generator(
        "PLA_TOUR_LAN_42_7")
    alert_PLA_TOUR_STID_42_6, satut_PLA_TOUR_STID_42_6, time_PLA_TOUR_STID_42_6 = generator(
        "PLA_TOUR_STID_42_6")
    alert_KOU_TOUR_LAND_100_7, satut_KOU_TOUR_LAND_100_7, time_KOU_TOUR_LAND_100_7 = generator(
        "KOU_TOUR_LAND_100_7")
    alert_KOU_TOUR_STID_100_6, satut_KOU_TOUR_STID_100_6, time_KOU_TOUR_STID_100_6 = generator(
        "KOU_TOUR_STID_100_6")
    alert_MPO_TOUR_LAND_99_6, satut_MPO_TOUR_LAND_99_6, time_MPO_TOUR_LAND_99_6 = generator(
        "MPO_TOUR_LAND_99_6")
    alert_MPO_TOUR_STID_99_7, satut_MPO_TOUR_STID_99_7, time_MPO_TOUR_STID_99_7 = generator(
        "MPO_TOUR_STID_99_7")

    print("****************************************** ALERTE **********************************")

    print("****************************************** STATS **********************************")
    badge_ok_TRE_PDA_FAM_215, badge_interdit_TRE_PDA_FAM_215, badge_perime_TRE_PDA_FAM_215, solde_epuise_TRE_PDA_FAM_215, article_inconnu_TRE_PDA_FAM_215, total_TRE_PDA_FAM_215, = get_stats(
        'TRE_PDA_FAM_215')
    badge_ok_TRE_PDA_COP_743, badge_interdit_TRE_PDA_COP_743, badge_perime_TRE_PDA_COP_743, solde_epuise_TRE_PDA_COP_743, article_inconnu_TRE_PDA_COP_743, total_TRE_PDA_COP_743 = get_stats(
        'TRE_PDA_COP_743')
    badge_ok_AZI_PDA_COP_057, badge_interdit_AZI_PDA_COP_057, badge_perime_AZI_PDA_COP_057, solde_epuise_AZI_PDA_COP_057, article_inconnu_AZI_PDA_COP_057, total_AZI_PDA_COP_057 = get_stats(
        'AZI_PDA_COP_057')
    badge_ok_AZI_PDA_FAM_850, badge_interdit_AZI_PDA_FAM_850, badge_perime_AZI_PDA_FAM_850, solde_epuise_AZI_PDA_FAM_850, article_inconnu_AZI_PDA_FAM_850, total_AZI_PDA_FAM_850 = get_stats(
        'AZI_PDA_FAM_850')
    badge_ok_MPO_PDA_COP_006, badge_interdit_MPO_PDA_COP_006, badge_perime_MPO_PDA_COP_006, solde_epuise_MPO_PDA_COP_006, article_inconnu_MPO_PDA_COP_006, total_MPO_PDA_COP_006 = get_stats(
        'MPO_PDA_COP_006')
    badge_ok_MPO_PDA_COP_735, badge_interdit_MPO_PDA_COP_735, badge_perime_MPO_PDA_COP_735, solde_epuise_MPO_PDA_COP_735, article_inconnu_MPO_PDA_COP_735, total_MPO_PDA_COP_735 = get_stats(
        'MPO_PDA_COP_735')
    badge_ok_MPO_PDA_FAM_617, badge_interdit_MPO_PDA_FAM_617, badge_perime_MPO_PDA_FAM_617, solde_epuise_MPO_PDA_FAM_617, article_inconnu_MPO_PDA_FAM_617, total_MPO_PDA_FAM_617 = get_stats(
        'MPO_PDA_FAM_617')
    badge_ok_KOU_PDA_FAM_153, badge_interdit_KOU_PDA_FAM_153, badge_perime_KOU_PDA_FAM_153, solde_epuise_KOU_PDA_FAM_153, article_inconnu_KOU_PDA_FAM_153, total_KOU_PDA_FAM_153 = get_stats(
        'KOU_PDA_FAM_153')
    badge_ok_KOU_PDA_FAM_575, badge_interdit_KOU_PDA_FAM_575, badge_perime_KOU_PDA_FAM_575, solde_epuise_KOU_PDA_FAM_575, article_inconnu_KOU_PDA_FAM_575, total_KOU_PDA_FAM_575 = get_stats(
        'KOU_PDA_FAM_575')
    badge_ok_ABO_PDA_FAM_975, badge_interdit_ABO_PDA_FAM_975, badge_perime_ABO_PDA_FAM_975, solde_epuise_ABO_PDA_FAM_975, article_inconnu_ABO_PDA_FAM_975, total_ABO_PDA_FAM_975 = get_stats(
        'ABO_PDA_FAM_975')
    badge_ok_ABO_PDA_FAM_932, badge_interdit_ABO_PDA_FAM_932, badge_perime_ABO_PDA_FAM_932, solde_epuise_ABO_PDA_FAM_932, article_inconnu_ABO_PDA_FAM_932, total_ABO_PDA_FAM_932 = get_stats(
        'ABO_PDA_FAM_932')
    badge_ok_PLA_PDA_FAM_211, badge_interdit_PLA_PDA_FAM_211, badge_perime_PLA_PDA_FAM_211, solde_epuise_PLA_PDA_FAM_211, article_inconnu_PLA_PDA_FAM_211, total_PLA_PDA_FAM_211 = get_stats(
        'PLA_PDA_FAM_211')
    badge_ok_PLA_PDA_FAM_354, badge_interdit_PLA_PDA_FAM_354, badge_perime_PLA_PDA_FAM_354, solde_epuise_PLA_PDA_FAM_354, article_inconnu_PLA_PDA_FAM_354, total_PLA_PDA_FAM_354 = get_stats(
        'PLA_PDA_FAM_354')
    badge_ok_PLA_PDA_COP_701, badge_interdit_PLA_PDA_COP_701, badge_perime_PLA_PDA_COP_701, solde_epuise_PLA_PDA_COP_701, article_inconnu_PLA_PDA_COP_701, total_PLA_PDA_COP_701 = get_stats(
        'PLA_PDA_COP_701')
    # TQT
    badge_ok_TRE_TOUR_STID_60_57, badge_interdit_TRE_TOUR_STID_60_57, badge_perime_TRE_TOUR_STID_60_57, solde_epuise_TRE_TOUR_STID_60_57, article_inconnu_TRE_TOUR_STID_60_57, total_TRE_TOUR_STID_60_57 = get_stats(
        'TRE_TOUR_STID_60_57')
    badge_ok_TRE_TOUR_STID_60_58, badge_interdit_TRE_TOUR_STID_60_58, badge_perime_TRE_TOUR_STID_60_58, solde_epuise_TRE_TOUR_STID_60_58, article_inconnu_TRE_TOUR_STID_60_58, total_TRE_TOUR_STID_60_58 = get_stats(
        'TRE_TOUR_STID_60_58')
    badge_ok_PLA_TOUR_LAN_42_7, badge_interdit_PLA_TOUR_LAN_42_7, badge_perime_PLA_TOUR_LAN_42_7, solde_epuise_PLA_TOUR_LAN_42_7, article_inconnu_PLA_TOUR_LAN_42_7, total_PLA_TOUR_LAN_42_7 = get_stats(
        'PLA_TOUR_LAN_42_7')
    badge_ok_PLA_TOUR_STID_42_6, badge_interdit_PLA_TOUR_STID_42_6, badge_perime_PLA_TOUR_STID_42_6, solde_epuise_PLA_TOUR_STID_42_6, article_inconnu_PLA_TOUR_STID_42_6, total_PLA_TOUR_STID_42_6 = get_stats(
        'PLA_TOUR_STID_42_6')
    badge_ok_KOU_TOUR_LAND_100_7, badge_interdit_KOU_TOUR_LAND_100_7, badge_perime_KOU_TOUR_LAND_100_7, solde_epuise_KOU_TOUR_LAND_100_7, article_inconnu_KOU_TOUR_LAND_100_7, total_KOU_TOUR_LAND_100_7 = get_stats(
        'KOU_TOUR_LAND_100_7')
    badge_ok_KOU_TOUR_STID_100_6, badge_interdit_KOU_TOUR_STID_100_6, badge_perime_KOU_TOUR_STID_100_6, solde_epuise_KOU_TOUR_STID_100_6, article_inconnu_KOU_TOUR_STID_100_6, total_KOU_TOUR_STID_100_6 = get_stats(
        'KOU_TOUR_STID_100_6')
    badge_ok_MPO_TOUR_LAND_99_6, badge_interdit_MPO_TOUR_LAND_99_6, badge_perime_MPO_TOUR_LAND_99_6, solde_epuise_MPO_TOUR_LAND_99_6, article_inconnu_MPO_TOUR_LAND_99_6, total_MPO_TOUR_LAND_99_6 = get_stats(
        'MPO_TOUR_LAND_99_6')
    badge_ok_MPO_TOUR_STID_99_7, badge_interdit_MPO_TOUR_STID_99_7, badge_perime_MPO_TOUR_STID_99_7, solde_epuise_MPO_TOUR_STID_99_7, article_inconnu_MPO_TOUR_STID_99_7, total_MPO_TOUR_STID_99_7 = get_stats(
        'MPO_TOUR_STID_99_7')

    query = ' SELECT * FROM elisath_gestion_abo.Supervision sv \
    WHERE sv.Nom IN ("TRE_PDA_FAM_215", "TRE_PDA_COP_743", \
    "AZI_PDA_COP_057", "AZI_PDA_FAM_850", "MPO_PDA_COP_006", "MPO_PDA_COP_735", "PLA_PDA_COP_701" \
    "MPO_PDA_FAM_617", "KOU_PDA_FAM_153", "KOU_PDA_FAM_575", "ABO_PDA_FAM_975", \
    "ABO_PDA_FAM_932", "PLA_PDA_FAM_211", "PLA_PDA_FAM_354") ORDER BY sv.DateHeure DESC'
    donnee = pd.read_sql(query, cnx)
    donnee.drop_duplicates(subset="Nom", keep="first", inplace=True)

    query2 = ' SELECT * FROM elisath_gestion_abo.Supervision sv \
    WHERE sv.Nom IN ("TRE_TOUR_STID_60_57", "TRE_TOUR_STID_60_58", \
    "PLA_TOUR_LAN_42_7", "PLA_TOUR_STID_42_6", "KOU_TOUR_LAND_100_7", "KOU_TOUR_STID_100_6", "MPO_TOUR_LAND_99_6" \
    "MPO_TOUR_STID_99_7") ORDER BY sv.DateHeure DESC'
    donnee2 = pd.read_sql(query2, cnx)
    donnee2.drop_duplicates(subset="Nom", keep="first", inplace=True)

    s_11, s12, s_13, s14, s_15, s_16, s1t = 0, 0, 0, 0, 0, 0, 0
    query_s1 = 'SELECT tb.Message, COUNT(tb.Message)"Compte" FROM elisath_gestion_abo.TestBadge tb  WHERE tb.Acces IN ("TRE_PDA_FAM_215", "TRE_PDA_COP_743", \
    "AZI_PDA_COP_057", "AZI_PDA_FAM_850", "MPO_PDA_COP_006", "MPO_PDA_COP_735", "PLA_PDA_COP_701" \
    "MPO_PDA_FAM_617", "KOU_PDA_FAM_153", "KOU_PDA_FAM_575", "ABO_PDA_FAM_975", \
    "ABO_PDA_FAM_932", "PLA_PDA_FAM_211", "PLA_PDA_FAM_354")  \
        AND DAY(tb.DateHeure) = DAY(CURDATE()) AND MONTH(tb.DateHeure) = MONTH(CURDATE()) \
        AND YEAR(tb.DateHeure) = YEAR(CURDATE()) GROUP BY 1'
    cnx = mysql.connector.connect(**config)
    stat_1 = pd.read_sql(query_s1, cnx)
    s1t = stat_1.Compte.sum()
    try:
        s_11 = stat_1.loc[stat_1.Message == "BADGE OK", "Compte"].values[0]
    except:
        s_11 = 0

    try:
        s_13 = stat_1.loc[stat_1.Message == "BADGE PERIME", "Compte"].values[0]
    except:
        s_13 = 0
    try:
        s_14 = stat_1.loc[stat_1.Message ==
                          "BADGE INTERDIT", "Compte"].values[0]
    except:
        s_14 = 0
    try:
        s_15 = stat_1.loc[stat_1.Message ==
                          "ARTICLE INCONNU", "Compte"].values[0]
    except:
        s_15 = 0
    try:
        s_16 = stat_1.loc[stat_1.Message == "SOLDE EPUISE", "Compte"].values[0]
    except:
        s_16 = 0

    s_21, s22, s_23, s24, s_25, s_26, s2t = 0, 0, 0, 0, 0, 0, 0
    query_s2 = 'SELECT tb.Message, COUNT(tb.Message)"Compte" FROM elisath_gestion_abo.TestBadge tb  WHERE tb.Acces IN ("TRE_TOUR_STID_60_57", "TRE_TOUR_STID_60_58", \
    "PLA_TOUR_LAN_42_7", "PLA_TOUR_STID_42_6", "KOU_TOUR_LAND_100_7", "KOU_TOUR_STID_100_6", "MPO_TOUR_LAND_99_6" \
    "MPO_TOUR_STID_99_7")  \
        AND DAY(tb.DateHeure) = DAY(CURDATE()) AND MONTH(tb.DateHeure) = MONTH(CURDATE()) \
        AND YEAR(tb.DateHeure) = YEAR(CURDATE()) GROUP BY 1'
    cnx = mysql.connector.connect(**config)
    stat_2 = pd.read_sql(query_s2, cnx)
    s2t = stat_2.Compte.sum()
    try:
        s_21 = stat_2.loc[stat_2.Message == "BADGE OK", "Compte"].values[0]
    except:
        s_21 = 0

    try:
        s_23 = stat_2.loc[stat_2.Message == "BADGE PERIME", "Compte"].values[0]
    except:
        s_23 = 0
    try:
        s_24 = stat_2.loc[stat_2.Message ==
                          "BADGE INTERDIT", "Compte"].values[0]
    except:
        s_24 = 0
    try:
        s_25 = stat_2.loc[stat_2.Message ==
                          "ARTICLE INCONNU", "Compte"].values[0]
    except:
        s_25 = 0
    try:
        s_26 = stat_2.loc[stat_2.Message == "SOLDE EPUISE", "Compte"].values[0]
    except:
        s_26 = 0
    print("****************************************** STATS **********************************")
    with placeholder.container():
        st.markdown(
            f"""
            <div class="d-flex justify-content-center;">
                <h1 class="display-1" style="border: 5px solid black">MONITORING PDA & TOURNIQUET</h1>
            </div>
            <div class="d-flex justify-content-center;">
                <span style="color:white; font-weight:bold; font-size:25px;">SYNTHESE GLOBALE <span style="color:white; font-weight:bold; font-size:20px; font-style:italic"> | <span class="badge bg-success">TOTAL : {s2t + s1t}</span> | <span class="badge bg-info ">BAGDE OK : {s_21 + s_11}</span> | <span class="badge bg-danger">BADGE PERIME : {s_23 + s_13}</span> | <span class="badge bg-danger">BADGE INTERDIT : {s_24 + s_14} </span> | <span class="badge bg-warning">ARTICLE INCONNU : {s_25 +s_15} </span> | <span class="badge bg-warning">SOLDE EPUISE : {s_26 + s_16}</span> </span> </span>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown(f"""
                <div class="card">
                    <div class="card-header" style="background: #0c2461">
                        <span style="color:white; font-weight:bold; font-size:25px">Monitoring des PDA <span style="color:white; font-weight:bold; font-size:20px; font-style:italic"> | <span class="badge bg-success">TOTAL : {s1t}</span> | <span class="badge bg-info ">BAGDE OK : {s_11}</span> | <span class="badge bg-danger">BADGE PERIME : {s_13}</span> | <span class="badge bg-danger">BADGE INTERDIT : {s_14} </span> | <span class="badge bg-warning">ARTICLE INCONNU : {s_15} </span> | <span class="badge bg-warning">SOLDE EPUISE : {s_16}</span> </span> </span>
                    </div>
                    <div class="card-body" style="color:black">
                        <div class="row align-items-start">
                            <div class="col" style="border : 3px solid black; margin-right: 3px">
                                <span style="color:black; justify-conten:center; text-align:center; font-weight:bold; border-bottom: 2px solid black">PDA Treichville</span>
                                <div class="row align-items-start m-0 p-0">
                                    <div class="col m-0 p-0">
                                        {plot_detail("TRE_PDA_FAM_215",satut_TRE_PDA_FAM_215, total_TRE_PDA_FAM_215, badge_ok_TRE_PDA_FAM_215,
                                                     badge_interdit_TRE_PDA_FAM_215, badge_perime_TRE_PDA_FAM_215, article_inconnu_TRE_PDA_FAM_215, solde_epuise_TRE_PDA_FAM_215)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("TRE_PDA_COP_743",satut_TRE_PDA_COP_743, total_TRE_PDA_COP_743, badge_ok_TRE_PDA_COP_743,
                                                     badge_interdit_TRE_PDA_COP_743, badge_perime_TRE_PDA_COP_743, article_inconnu_TRE_PDA_COP_743, solde_epuise_TRE_PDA_COP_743)}
                                    </div>
                                </div>
                            </div>
                            <div class="col" style="border : 3px solid black; margin-right: 3px">
                                <span style="color:black; justify-conten:center; text-align:center; font-weight:bold; border-bottom: 2px solid black">PDA Azito</span>
                                <div class="row align-items-start m-0 p-0">
                                    <div class="col m-0 p-0">
                                        {plot_detail("AZI_PDA_COP_057",satut_AZI_PDA_COP_057, total_AZI_PDA_COP_057, badge_ok_AZI_PDA_COP_057,
                                                     badge_interdit_AZI_PDA_COP_057, badge_perime_AZI_PDA_COP_057, article_inconnu_AZI_PDA_COP_057, solde_epuise_AZI_PDA_COP_057)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("AZI_PDA_FAM_850",satut_AZI_PDA_FAM_850, total_AZI_PDA_FAM_850, badge_ok_AZI_PDA_FAM_850,
                                                     badge_interdit_AZI_PDA_FAM_850, badge_perime_AZI_PDA_FAM_850, article_inconnu_AZI_PDA_FAM_850, solde_epuise_AZI_PDA_FAM_850)}
                                    </div>
                                </div>
                            </div>
                            <div class="col" style="border : 3px solid black; margin-right: 3px">
                                <span style="color:black; justify-conten:center; text-align:center; font-weight:bold; border-bottom: 2px solid black">PDA Koumassi</span>
                                <div class="row align-items-start m-0 p-0">
                                    <div class="col m-0 p-0">
                                        {plot_detail("KOU_PDA_FAM_153",satut_KOU_PDA_FAM_153, total_KOU_PDA_FAM_153, badge_ok_KOU_PDA_FAM_153,
                                                     badge_interdit_KOU_PDA_FAM_153, badge_perime_KOU_PDA_FAM_153, article_inconnu_KOU_PDA_FAM_153, solde_epuise_KOU_PDA_FAM_153)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("KOU_PDA_FAM_575",satut_KOU_PDA_FAM_575, total_KOU_PDA_FAM_575, badge_ok_KOU_PDA_FAM_575,
                                                     badge_interdit_KOU_PDA_FAM_575, badge_perime_KOU_PDA_FAM_575, article_inconnu_KOU_PDA_FAM_575, solde_epuise_KOU_PDA_FAM_575)}
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row align-items-start mt-2">
                            <div class="col" style="border : 3px solid black; margin-right: 3px">
                                <span style="color:black; justify-conten:center; text-align:center; font-weight:bold; border-bottom: 2px solid black">PDA M'Pouto </span>
                                <div class="row align-items-start m-0 p-0">
                                    <div class="col m-0 p-0">
                                        {plot_detail("MPO_PDA_COP_006",satut_MPO_PDA_COP_006, total_MPO_PDA_COP_006, badge_ok_MPO_PDA_COP_006,
                                                     badge_interdit_MPO_PDA_COP_006, badge_perime_MPO_PDA_COP_006, article_inconnu_MPO_PDA_COP_006, solde_epuise_MPO_PDA_COP_006)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("MPO_PDA_COP_735",satut_MPO_PDA_COP_735, total_MPO_PDA_COP_735, badge_ok_MPO_PDA_COP_735,
                                                     badge_interdit_MPO_PDA_COP_735, badge_perime_MPO_PDA_COP_735, article_inconnu_MPO_PDA_COP_735, solde_epuise_MPO_PDA_COP_735)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("MPO_PDA_FAM_617",satut_MPO_PDA_FAM_617, total_MPO_PDA_FAM_617, badge_ok_MPO_PDA_FAM_617,
                                                     badge_interdit_MPO_PDA_FAM_617, badge_perime_MPO_PDA_FAM_617, article_inconnu_MPO_PDA_FAM_617, solde_epuise_MPO_PDA_FAM_617)}
                                    </div>
                                </div>
                            </div>
                            <div class="col" style="border : 3px solid black; margin-right: 3px">
                                <span style="color:black; justify-conten:center; text-align:center; font-weight:bold; border-bottom: 2px solid black">PDA Abobodoumé </span>
                                <div class="row align-items-start m-0 p-0">
                                    <div class="col m-0 p-0">
                                        {plot_detail("ABO_PDA_FAM_975",satut_ABO_PDA_FAM_975, total_ABO_PDA_FAM_975, badge_ok_ABO_PDA_FAM_975,
                                                     badge_interdit_ABO_PDA_FAM_975, badge_perime_ABO_PDA_FAM_975, article_inconnu_ABO_PDA_FAM_975, solde_epuise_ABO_PDA_FAM_975)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("ABO_PDA_FAM_932",satut_ABO_PDA_FAM_932, total_ABO_PDA_FAM_932, badge_ok_ABO_PDA_FAM_932,
                                                     badge_interdit_ABO_PDA_FAM_932, badge_perime_ABO_PDA_FAM_932, article_inconnu_ABO_PDA_FAM_932, solde_epuise_ABO_PDA_FAM_932)}
                                    </div>
                                </div>
                            </div>
                            <div class="col" style="border : 3px solid black; margin-right: 3px">
                                <span style="color:black; justify-conten:center; text-align:center; font-weight:bold; border-bottom: 2px solid black">PDA Plateau </span>
                                <div class="row align-items-start m-0 p-0">
                                    <div class="col m-0 p-0">
                                        {plot_detail("PLA_PDA_FAM_211",satut_PLA_PDA_FAM_211, total_PLA_PDA_FAM_211, badge_ok_PLA_PDA_FAM_211,
                                                     badge_interdit_PLA_PDA_FAM_211, badge_perime_PLA_PDA_FAM_211, article_inconnu_PLA_PDA_FAM_211, solde_epuise_PLA_PDA_FAM_211)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("PLA_PDA_FAM_354",satut_PLA_PDA_FAM_354, total_PLA_PDA_FAM_354, badge_ok_PLA_PDA_FAM_354,
                                                     badge_interdit_PLA_PDA_FAM_354, badge_perime_PLA_PDA_FAM_354, article_inconnu_PLA_PDA_FAM_354, solde_epuise_PLA_PDA_FAM_354)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("PLA_PDA_COP_701",satut_PLA_PDA_COP_701, total_PLA_PDA_COP_701, badge_ok_PLA_PDA_COP_701,
                                                     badge_interdit_PLA_PDA_COP_701, badge_perime_PLA_PDA_COP_701, article_inconnu_PLA_PDA_COP_701, solde_epuise_PLA_PDA_COP_701)}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        # TOURNIQETS
        st.markdown(f"""
                <div class="card">
                    <div class="card-header" style="background: #0c2461">
                        <span style="color:white; font-weight:bold; font-size:25px">Monitoring des Tourniquets <span style="color:white; font-weight:bold; font-size:20px; font-style:italic"> | <span class="badge bg-success">TOTAL : {s2t}</span> | <span class="badge bg-info ">BAGDE OK : {s_21}</span> | <span class="badge bg-danger">BADGE PERIME : {s_23}</span> | <span class="badge bg-danger">BADGE INTERDIT : {s_24} </span> | <span class="badge bg-warning">ARTICLE INCONNU : {s_25} </span> | <span class="badge bg-warning">SOLDE EPUISE : {s_26}</span> </span> </span>
                    </div>
                    <div class="card-body" style="color:black">
                        <div class="row align-items-start">
                            <div class="col" style="border : 3px solid black; margin-right: 3px">
                                <span style="color:black; justify-conten:center; text-align:center; font-weight:bold; border-bottom: 2px solid black">Tourniquet Treichville </span>
                                <div class="row align-items-start m-0 p-0">
                                    <div class="col m-0 p-0">
                                        {plot_detail("TRE_TOUR_STID_60_57",satut_TRE_TOUR_STID_60_57, total_TRE_TOUR_STID_60_57, badge_ok_TRE_TOUR_STID_60_57,
                                                     badge_interdit_TRE_TOUR_STID_60_57, badge_perime_TRE_TOUR_STID_60_57, article_inconnu_TRE_TOUR_STID_60_57, solde_epuise_TRE_TOUR_STID_60_57)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("TRE_TOUR_STID_60_58",satut_TRE_TOUR_STID_60_58, total_TRE_TOUR_STID_60_58, badge_ok_TRE_TOUR_STID_60_58,
                                                     badge_interdit_TRE_TOUR_STID_60_58, badge_perime_TRE_TOUR_STID_60_58, article_inconnu_TRE_TOUR_STID_60_58, solde_epuise_TRE_TOUR_STID_60_58)}
                                    </div>
                                </div>
                            </div>
                            <div class="col" style="border : 3px solid black; margin-right: 3px">
                                <span style="color:black; justify-conten:center; text-align:center; font-weight:bold; border-bottom: 2px solid black">Tourniquets Plateau</span>
                                <div class="row align-items-start m-0 p-0">
                                    <div class="col m-0 p-0">
                                        {plot_detail("PLA_TOUR_LAN_42_7",satut_PLA_TOUR_LAN_42_7, total_PLA_TOUR_LAN_42_7, badge_ok_PLA_TOUR_LAN_42_7,
                                                     badge_interdit_PLA_TOUR_LAN_42_7, badge_perime_PLA_TOUR_LAN_42_7, article_inconnu_PLA_TOUR_LAN_42_7, solde_epuise_PLA_TOUR_LAN_42_7)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("PLA_TOUR_STID_42_6",satut_PLA_TOUR_STID_42_6, total_PLA_TOUR_STID_42_6, badge_ok_PLA_TOUR_STID_42_6,
                                                     badge_interdit_PLA_TOUR_STID_42_6, badge_perime_PLA_TOUR_STID_42_6, article_inconnu_PLA_TOUR_STID_42_6, solde_epuise_PLA_TOUR_STID_42_6)}
                                    </div>
                                </div>
                            </div>
                            <div class="col" style="border : 3px solid black; margin-right: 3px">
                                <span style="color:black; justify-conten:center; text-align:center; font-weight:bold; border-bottom: 2px solid black">Tourniquets Koumassi</span>
                                <div class="row align-items-start m-0 p-0">
                                    <div class="col m-0 p-0">
                                        {plot_detail("KOU_TOUR_LAND_100_7",satut_KOU_TOUR_LAND_100_7, total_KOU_TOUR_LAND_100_7, badge_ok_KOU_TOUR_LAND_100_7,
                                                     badge_interdit_KOU_TOUR_LAND_100_7, badge_perime_KOU_TOUR_LAND_100_7, article_inconnu_KOU_TOUR_LAND_100_7, solde_epuise_KOU_TOUR_LAND_100_7)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("KOU_TOUR_STID_100_6",satut_KOU_TOUR_STID_100_6, total_KOU_TOUR_STID_100_6, badge_ok_KOU_TOUR_STID_100_6,
                                                     badge_interdit_KOU_TOUR_STID_100_6, badge_perime_KOU_TOUR_STID_100_6, article_inconnu_KOU_TOUR_STID_100_6, solde_epuise_KOU_TOUR_STID_100_6)}
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row align-items-start mt-2 justify-content-start">
                            <div class="col justify-content-start" style="border : 3px solid black; margin-right: 3px">
                                <span style="color:black; justify-conten:center; text-align:center; font-weight:bold; border-bottom: 2px solid black">Tourniquets M'Pouto </span>
                                <div class="row align-items-start m-0 p-0">
                                    <div class="col m-0 p-0">
                                        {plot_detail("MPO_TOUR_LAND_99_6",satut_MPO_TOUR_LAND_99_6, total_MPO_TOUR_LAND_99_6, badge_ok_MPO_TOUR_LAND_99_6,
                                                     badge_interdit_MPO_TOUR_LAND_99_6, badge_perime_MPO_TOUR_LAND_99_6, article_inconnu_MPO_TOUR_LAND_99_6, solde_epuise_MPO_TOUR_LAND_99_6)}
                                    </div>
                                    <div class="col m-0 p-0">
                                        {plot_detail("MPO_TOUR_STID_99_7",satut_MPO_TOUR_STID_99_7, total_MPO_TOUR_STID_99_7, badge_ok_MPO_TOUR_STID_99_7,
                                                     badge_interdit_MPO_TOUR_STID_99_7, badge_perime_MPO_TOUR_STID_99_7, article_inconnu_MPO_TOUR_STID_99_7, solde_epuise_MPO_TOUR_STID_99_7)}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("### Details PDA")
        col1, col2 = st.columns(2)
        with st.container():
            with col1:
                st.markdown("##### PDA fonctiontionnels")
                st.dataframe(donnee.loc[donnee.Code == 0, :])
            with col2:
                st.markdown("##### PDA non fonctiontionnels")
                st.dataframe(donnee.loc[donnee.Code == 1, :])

        st.markdown("### Details Tourniques")
        col1, col2 = st.columns(2)
        with st.container():
            with col1:
                st.markdown("##### Tourniquets fonctiontionnels")
                st.dataframe(donnee2.loc[donnee2.Code == 0, :])
            with col2:
                st.markdown("##### Tourniquets non fonctiontionnels")
                st.dataframe(donnee2.loc[donnee2.Code == 1, :])
