# Django Model Behaviors Example

Sample code to explore the model behaviors pattern for Django.

There are two apps, `traditional` and `updated` that show the same generic `BlogPost` model in a traditional Django model definition, and separated into reusable behaviors.  Each app has a unit test example that shows how to architect the test code to match.  Finally, theres view code in the `updated` app that shows common queryset interactions.

## Installation

1. Clone this repository

        git clone https://github.com/kevinastone/django-model-behaviors-example.git
        cd django-model-behaviors-example

2. Install the dependencies

        pip install -r requirements.txt

3. Run the Unit Tests

        ./manage.py test

