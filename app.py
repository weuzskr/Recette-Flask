from flask import Flask, render_template,request,redirect
import random

app = Flask(__name__)

ingredients_list = [
    {"name": "pommes de terre", "image": "static/images/poivre.jpg"},
    {"name": "oignons", "image": "static/images/oignons.jpg"},
    {"name": "ail", "image": "static/images/ail.jpg"},
    {"name": "huile d'olive", "image": "static/images/huile_dolive.jpg"},
    {"name": "sel", "image": "static/images/sel.jpg"},
    {"name": "riz", "image": "static/images/riz.jpg"},
    {"name": "poivre", "image": "static/images/poivre.jpg"},
    {"name": "poulet", "image": "static/images/poulet.jpg"},
    {"name": "beurre", "image": "static/images/beurre.jpg"},
    {"name": "lait", "image": "static/images/lait.jpg"},
    {"name": "oeufs", "image": "static/images/oeufs.jpg"},
    {"name": "sauce soja", "image": "static/images/sauce soja.jpg"},
    {"name": "sucre", "image": "static/images/sucre.jpg"},
    {"name": "cannelle", "image": "static/images/cannelle.jpg"},
    {"name": "légumes variés", "image": "static/images/légumes variés.jpg"},
    {"name": "basilic", "image": "static/images/basilic.jpg"},
    {"name": "tomates", "image": "static/images/tomates.jpg"},
    {"name": "pommes", "image": "static/images/pommes.jpg"},
    {"name": "vinaigre balsamique", "image": "static/images/vinaigre balsamique.jpg"},
    {"name": "Pâte d'arachide", "image": "static/images/patte d'arachide.jpg"},
    {"name": "Bouillon","image": "static/images/bouillon.jpg"},
    {"name": "Concentré de tomate","image":"static/images/concentre de tomate.jpg"},
    {"name": "Piment frais","image":"static/images/piment frais.jpg"},
    {"name": "Huile d'arachide","image":"static/images/huille d'arachide.jpg"},
    {"name": "Viande","image":"static/images/viande.jpg"},
    {"name": "Yet","image":"static/images/yet.jpg"},
    {"name": "Guedj","image":"static/images/guedj.jpg"},
    {"name": "Netetou","image":"static/images/netetou.jpg"},
    {"name": "Arachide en poudre","image":"static/images/arachide en poudre.jpg"},
    {"name": "Citron","image":"static/images/citron.jpg"}
    
]

recipes = [

{
        "name": "Mafé de poulet",
        "ingredients": ["Pâte d'arachide", "Bouillon", "Concentré de tomate", "Piment frais", "Huile d'arachide","légumes variés","oignons","sel","poulet"],
        "steps": [
            "faites sauter la viande et les oignons dans une sauteuse ou une grande poêle, avec l'huile d'arachide.",
            "Lorsque les oignons sont bien dorés mais pas caramélisés, réduisez le feu et couvrez pendant quelques minutes.",
            "Ajoutez tous les autres ingrédients sauf la pâte d'arachides, le beurre de cacahuètes et le bouillon.",
            "Couvrez et laissez mijoter pendant encore 30 min, jusqu'à ce que les légumes soient bien tendres. N'hésitez pas à mélanger de temps en temps. On peut ajouter du bouillon si nécessaire.",
            "Réduisez le feu et ajoutez le beurre de cacahuètes et la pâte d'arachides.",
            "Remuez bien pour répartir la sauce dans l'ensemble de la préparation. Ajoutez du bouillon jusqu'à l'obtention d'une sauce onctueuse. Laissez mijoter quelques minutes.",
            "Servez votre mafé de poulet de Maimouna bien chaud, de préférence avec du riz."
        ]
    },

    {
        "name": "Mbakhalou Saloum",
        "ingredients": ["Viande", "Bouillon", "Oignon","6Cl Huile d'arachide", "Piment frais", "350g d'Arachide en poudre","Yet","Guedj","sel","netetou","350g de riz","citron beure de vache"],
        "steps": [
            "Mettre à chauffer les 6 cl d’huile. Ajouter la viande. Laisser cuire environ 15 min. Ajouter ensuite le yët puis 1 oignon émincé. Mélanger et laisser bien colorer le tout environ 5 bonnes minutes",
            "Découper le poivron vert, le piment vert et les tomates fraîches en morceaux. Mixer le tout. Ajouter cette mixture dans la marmite. Ajouter du sel. Mélanger et laisser cuire 5 min. Vous obtenez ainsi une bonne coloration.",
            "Ajouter ensuite 0,6 l d’eau. Mélanger et ajouter les haricots secs, les pagnes, le guedj et le piment frais. Laisser cuire 30 min à feu moyen",
            "Retirer si besoin le piment pour qu’il n’éclate pas. Poser un couscoussier au-dessus de la marmite et ajouter le riz préalablement lavé. Laisser cuire 15 min. Puis retirer le couscoussier.",
            "Ajouter ensuite du poivre et le nététou en poudre. Goûter l’assaisonnement et rajouter du sel si besoin.",
            "Ajouter le riz précédemment cuit à la vapeur. Mélanger. Laisser mijoter 12 min. Lorsque vous remarquez que le riz a absorbé tout le bouillon (toute l’eau), alors ajouter l’arachide en poudre en la saupoudrant au-dessus du riz. Laisser cuire 10 min à feu doux.",
            "Mélanger puis cuire de nouveau 10 min pour poursuivre la cuisson de l’arachide."
        ]
    },


    {
        "name": "Purée de pommes de terre",
        "ingredients": ["pommes de terre", "beurre", "lait", "sel", "poivre"],
        "steps": [
            "Épluchez les pommes de terre et coupez-les en morceaux.",
            "Faites cuire les pommes de terre dans une casserole d'eau bouillante salée jusqu'à ce qu'elles soient tendres.",
            "Égouttez les pommes de terre et écrasez-les avec un presse-purée.",
            "Ajoutez le beurre et le lait, puis mélangez jusqu'à obtenir une consistance lisse.",
            "Assaisonnez avec du sel et du poivre selon votre goût.",
            "Servez chaud."
        ]
    },
    {
        "name": "Omelette aux oignons",
        "ingredients": ["oeufs", "oignons", "huile d'olive", "sel", "poivre"],
        "steps": [
            "Émincez les oignons.",
            "Faites chauffer l'huile d'olive dans une poêle.",
            "Ajoutez les oignons et faites-les revenir jusqu'à ce qu'ils soient dorés.",
            "Dans un bol, battez les œufs avec du sel et du poivre.",
            "Versez les œufs battus dans la poêle avec les oignons.",
            "Laissez cuire l'omelette jusqu'à ce qu'elle soit prise.",
            "Retournez l'omelette et laissez cuire l'autre côté pendant quelques minutes.",
            "Servez chaud."
        ]
    },
    {
        "name": "Poulet rôti",
        "ingredients": ["poulet", "ail", "huile d'olive", "sel", "poivre"],
        "steps": [
            "Préchauffez le four à 200°C.",
            "Assaisonnez le poulet avec du sel, du poivre et de l'ail.",
            "Badigeonnez le poulet d'huile d'olive.",
            "Placez le poulet dans un plat allant au four et enfournez pendant environ 1 heure.",
            "Vérifiez la cuisson en insérant un thermomètre à viande dans la partie la plus épaisse du poulet. La température interne doit atteindre 75°C.",
            "Laissez reposer le poulet pendant quelques minutes avant de le découper.",
            "Servez chaud."
        ]
    },
    {
        "name": "Riz sauté aux légumes",
        "ingredients": ["riz", "légumes variés", "huile d'olive", "sauce soja"],
        "steps": [
            "Faites cuire le riz selon les instructions sur l'emballage.",
            "Dans une poêle, faites chauffer l'huile d'olive.",
            "Ajoutez les légumes coupés en dés et faites-les sauter jusqu'à ce qu'ils soient tendres.",
            "Ajoutez le riz cuit dans la poêle avec les légumes.",
            "Versez la sauce soja sur le riz et mélangez bien.",
            "Laissez cuire pendant quelques minutes jusqu'à ce que le riz soit chaud.",
            "Servez chaud."
        ]
    },
    {
        "name": "Salade de tomates et mozzarella",
        "ingredients": ["tomates", "mozzarella", "basilic", "huile d'olive", "vinaigre balsamique"],
        "steps": [
            "Coupez les tomates et la mozzarella en tranches.",
            "Disposez les tranches de tomates et de mozzarella sur une assiette.",
            "Parsemez de feuilles de basilic frais.",
            "Arrosez d'huile d'olive et de vinaigre balsamique.",
            "Salez et poivrez selon votre goût.",
            "Servez frais."
        ]
    },
    {
        "name": "Tarte aux pommes",
        "ingredients": ["pâte brisée", "pommes", "sucre", "cannelle"],
        "steps": [
            "Préchauffez le four à 180°C.",
            "Étalez la pâte brisée dans un moule à tarte.",
            "Épluchez et coupez les pommes en tranches.",
            "Disposez les tranches de pommes sur la pâte brisée.",
            "Saupoudrez de sucre et de cannelle.",
            "Enfournez la tarte pendant environ 30 minutes, jusqu'à ce qu'elle soit dorée.",
            "Laissez refroidir avant de servir."
        ]
    },
]
@app.route('/')
def index():
    return render_template('index.html', ingredients=ingredients_list, recipes=recipes)

@app.route('/generate_recipe')
def generate_recipe():
    random_recipe = random.choice(recipes)
    random_ingredients = random.sample(ingredients_list, 4)
    return render_template('recipe.html', recipe=random_recipe, ingredients=random_ingredients)

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    recipe_name = request.form['recipe_name']
    recipe_ingredients = request.form.getlist('recipe_ingredients')
    recipe_steps = request.form.getlist('recipe_steps')
    new_recipe = {
        "name": recipe_name,
        "ingredients": recipe_ingredients,
        "steps": recipe_steps
    }
    recipes.append(new_recipe)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)