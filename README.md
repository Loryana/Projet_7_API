# Projet 7 OC

Projet : Implémentez un modèle de scoring

C'est une partie du projet 7 de la formation OpenClassrooms du parcours data scientist
Objectifs du projet

Vous êtes Data Scientist au sein d'une société financière, nommée "Prêt à dépenser", qui propose des crédits à la consommation pour des personnes ayant peu ou pas du tout d'historique de prêt.

L’entreprise souhaite mettre en œuvre un outil de “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé. Elle souhaite donc développer un algorithme de classification en s’appuyant sur des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.)

Ce projet a donc pour but de déployer le modèle via une API (FAST API) à l' idez de AWS en utilisant un dashboard interactif (Streamlit) pour présenter le travail de modélisation.

l'API a été déployé sur AWS
Découpage des dossiers

    github/worflows : dossier nécessaire pour l'utilisation de Github Action
        ci.yml : fichier permettant de réaliser les tests unitaires
    fastapi_p7 : dossier contenant le code de l'API
        mlflow_model_smote : dossier contenant le modèle que l'on souhaite déployé dans l'API, enregistré sous Mlflow, les sous-dossier ne sont pas décrits ici, pour plus d'explication, se référer à la documentation de Mlflow directement
        app.py : fichier python contenant le code de l'API
        requirements.txt : fichier texte contenant les librairies nécessaires à l'utilisation de l'API
        test_api.csv : fichier contenant les données nécessaires au tests unitaires
    tests : dossier contenant les tests unitaires
        test_app.py : fichier python contenant les tests unitaires
        test_api.csv : fichier contenant les données nécessaires au tests unitaires
