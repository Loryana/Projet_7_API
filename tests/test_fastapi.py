import unittest
from fastapi.testclient import TestClient
from fastapi_p7.app import app  # Assurez-vous que le chemin correspond à votre projet
import pandas as pd

class TestFastAPI(unittest.TestCase):
    def setUp(self):
        # Initialisation du client de test
        self.client = TestClient(app)

    def load_data_test(self):
        #Charger les données nécessaires pour le test
        df = pd.read_csv('test_api.csv')
        return df

    def test_root_endpoint(self):
        # Tester la route GET /
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Bienvenue dans l'API de prédiction"})

    def test_predict_endpoint_success(self):
        # Tester la route POST /predict/ avec des données valides
        df = self.load_data_test()
        ligne = df
        input_data = ligne.to_dict()

        response = self.client.post("/predict/", json=input_data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("predictions", response.json())
        self.assertIsInstance(response.json()["predictions"], list)

    def test_predict_endpoint_invalid_data(self):
        # Tester la route POST /predict/ avec des données invalides
        df = self.load_data_test()
        ligne = df
        input_data = ligne.to_dict()

        first_feature = 'CODE_GENDER'
        input_data[first_feature] = "invalid"

        response = self.client.post("/predict/", json=input_data)
        self.assertEqual(response.status_code, 422)  # FastAPI retourne 422 pour des données invalides

    def test_predict_endpoint_missing_data(self):
        # Tester la route POST /predict/ avec des données manquantes
        df = self.load_data_test()
        ligne = df
        input_data = ligne.to_dict()
    
        first_feature = 'CODE_GENDER'
        input_data.pop(first_feature)

        response = self.client.post("/predict/", json=input_data)
        self.assertEqual(response.status_code, 422)  # Erreur car certaines données sont manquantes

if __name__ == "__main__":
    unittest.main()