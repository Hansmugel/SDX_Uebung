import unittest
import requests

class TestRecipeAPI(unittest.TestCase):
    # Base URL for the Recipe API.
    API_URL = "http://localhost:8080/recipes"
    
    # Sample recipe data for testing.
    RECIPE_SAMPLE = {
        "name": "Test Recipe",
        "ingredients": ["Ingredient 1", "Ingredient 2"],
        "instructions": "Test instructions"
    }

    def test_get_all_recipes(self):
        """
        Test to verify that the API returns a list of recipes.
        """
        # Make a GET request to fetch all recipes.
        response = requests.get(self.API_URL)
        self.assertEqual(response.status_code, 200)
        # Check if the response is a list, indicating multiple recipes.
        self.assertIsInstance(response.json(), list)
    
    def test_add_and_get_recipe(self):
        """
        Test to verify that a recipe can be added and then retrieved correctly.
        """
        # Add a new recipe via POST request and verify successful addition.
        add_response = requests.post(self.API_URL, json=self.RECIPE_SAMPLE)
        self.assertEqual(add_response.status_code, 200)
        added_recipe = add_response.json()
        self.assertIsNotNone(added_recipe.get('ID'), "Expected 'ID' in response but got None.")

        # Fetch the added recipe by its ID to verify it exists and is correct.
        recipe_id = added_recipe.get('ID')
        get_response = requests.get(f"{self.API_URL}/{recipe_id}")
        self.assertEqual(get_response.status_code, 200)
        retrieved_recipe = get_response.json()

        # Verify the fetched recipe matches the added recipe data.
        # Instructions are not compared here as the focus is on name and ingredients.
        self.assertEqual(retrieved_recipe.get('name'), self.RECIPE_SAMPLE['name'])
        self.assertListEqual(retrieved_recipe.get('ingredients'), self.RECIPE_SAMPLE['ingredients'])

# Enables running the tests from the command line.
if __name__ == '__main__':
    unittest.main()
