
# Calorie Counter Django App

This is a Django web application that allows users to:
1. Add ingredients with their respective calorie values.
2. Select ingredients to create a dish and calculate the total calories of the dish.

The application uses **Bootstrap** for a simple, responsive UI design.

## Features
- Add new ingredients with a name and calorie value.
- Create a dish by selecting multiple ingredients.
- Automatically calculate and display the total calories for the selected ingredients.
  
## Prerequisites

- Python 3.8+
- Django 4.x+
- Bootstrap (included via CDN)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/LiamSeridan/calorie-counter.git
    cd calorie-counter
    ```

2. Set up a virtual environment and install dependencies:

    ```bash
    python3 -m venv env
    source env/bin/activate
    pip3 install django
    ```

3. Run migrations to set up the database:

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

4. Start the Django development server:

    ```bash
    python3 manage.py runserver
    ```

5. Open the app in your web browser:

    - Add ingredients: `http://127.0.0.1:8000/ingredients/add/`
    - Create a dish and calculate calories: `http://127.0.0.1:8000/ingredients/create_dish/`

## Directory Structure

```
calorie_counter/
├── calorie_counter/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── ingredients/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── ingredients/
│           ├── add_ingredient.html
│           ├── create_dish.html
│           ├── dish_result.html
│           └── ingredient_list.html (optional)
└── manage.py
```

## Usage

### 1. Add Ingredients

Visit the `/ingredients/add/` page to add new ingredients. You can enter the name of the ingredient and its calorie count (e.g., "Banana" - 89 kcal).

### 2. Create a Dish and Calculate Calories

Visit the `/ingredients/create_dish/` page to select ingredients and calculate the total calories. The app will display the selected ingredients along with their calorie values and the total calories of the dish.

## Technologies Used

- **Django**: Python web framework.
- **Bootstrap**: Front-end component library for responsive UI.
  
## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

- GitHub: [LiamSeridan](https://github.com/LiamSeridan)
