cookbook = {
	'Sandwich': {
		'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
		'meal': 'lunch',
		'prep_time': 10
	},
	'Cake': {
		'ingredients': ['flour', 'sugar', 'eggs'],
		'meal': 'dessert',
		'prep_time': 60
	},
	'Salad': {
		'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
		'meal': 'lunch',
		'prep_time': 15
	}
}

def print_recipe_names():
	"""
	Fonction qui affiche les noms des recettes du cookbook
	"""
	print("Les recettes dispo sont :")
	for recipe_name in cookbook.keys():
		print(f"  - {recipe_name}")

def print_recipe_details(recipe_name):
	"""
	Affiche les details d'une recette specifique ou
	une erreur si elle n'existe pas
	"""
	if recipe_name in cookbook:
		recipe = cookbook[recipe_name]
		print(f"\nRecette pour {recipe_name} :")
		print(f"Ingrédients : {recipe['ingredients']}")
		print(f"Type de repas : {recipe['meal']}")
		print(f"Temps de préparation : {recipe['prep_time']} minutes")
	else:
		print(f"Désolé, la recette '{recipe_name}' n'existe pas dans le cookbook.")

def delete_recipe(recipe_name):
	"""
	Fonction qui supprime une recette du cookbook.
	Retourne True si la suppression a réussi, False sinon.
	"""
	if recipe_name in cookbook:
		del cookbook[recipe_name]
		print(f"La recette '{recipe_name}' a été supprimée.")
		return True
	else:
		print(f"Désolé, la recette '{recipe_name}' n'existe pas dans le cookbook.")
		return False

def add_recipe():
	"""
	Fonction pour ajouter de nouvelles recettes dans le cookbook
	"""
	name = input("Entrez le nom de la recette : ")
	print("Entrez les ingrédients (appuyez sur Entrée sans rien écrire pour terminer) : ")
	ingredients = []
	while True:
		ingredient = input()
		if ingredient == "":
			break
		ingredients.append(ingredient)
	meal = input("Entrez le type de repas : ")
	while True:
		try:
			prep_time = int(input("Entrez le temps de préparation (en minutes) : "))
			if prep_time >= 0:
				break
			print("Le temps doit etre positif.")
		except ValueError:
			print("Veuillez entrer un nombre entier valide.")

	cookbook[name] = {
		'ingredients': ingredients,
		'meal': meal,
		'prep_time': prep_time
	}
	print(f"\nLa recette '{name}' a été avec succès!")

def print_menu():
	"""
	Affiche le menu principal des options disponibles.
	"""
	print("\nListe des options disponibles :")
	print("  1: Ajouter une recette")
	print("  2: Supprimer une recette")
	print("  3: Afficher une recette")
	print("  4: Afficher le cookbook")
	print("  5: Quitter")

def main():
	"""
	Programme qui gère l'interaction avec l'utilisateur
	"""
	print("Bienvenue dans le Python CookBook !")

	while True:
		print_menu()
		print("\nChoisissez une option :")
		choice = input(">> ")
		if choice == "1":
			add_recipe()
		elif choice == "2":
			name = input("Entrez le nom de la recette à supprimer : ")
			delete_recipe(name)
		elif choice == "3":
			name = input("Entrez le nom de la recette à afficher : ")
			print_recipe_details(name)
		elif choice == "4":
			print_recipe_names()
		elif choice == "5":
			print("Cookbook fermé. Au revoir !")
			break
		else:
			print("Désolé, cette option n'existe pas.")

if __name__ == '__main__':
	main()