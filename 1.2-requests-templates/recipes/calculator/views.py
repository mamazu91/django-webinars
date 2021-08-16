from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def dish_view(request, input_dish):
    template = 'calculator/index.html'

    try:
        servings = int(request.GET.get('servings', 1))
    except ValueError:
        return HttpResponse(f'Parameter "servings" must be an int!')
    else:
        if servings == 0:
            return HttpResponse(f'Parameter "servings" must be bigger than 0!')

        recipe_dish = DATA.get(input_dish, None)
        recipe = {ingredient: amount * servings for ingredient, amount in recipe_dish.items()} if recipe_dish else None
        context = {
            'recipe': recipe
        }

        return render(request, template, context)
