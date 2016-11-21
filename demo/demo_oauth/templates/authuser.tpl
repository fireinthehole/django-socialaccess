{% load staticfiles %}

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

        <link rel="stylesheet" type="text/css" href="{% static 'assets/bootstrap/3.3.5/css/bootstrap.css' %}">
        <link rel="stylesheet" type="text/css" href="{% static 'assets/font-awesome/4.3.0/css/font-awesome.min.css' %}" media="all" />

        <title>Merge account login page | {{ site.name }}</title>
    </head>

    <body>
        <div class="alert alert-warning" role="alert">User {{ form.login.value }} already exists. Please authenticate to proceed linking it with this social profile.</div>

        <div class="row">
            <div class="col-md-4 col-md-offset-4">

                <div class="panel panel-default">
                    <div class="panel-heading">
                        <h3 class="panel-title">Please Sign In</h3>
                    </div>
                    <div class="panel-body">

                        <form role="form" method="post" action="{% url 'authuser' %}">
                            {% csrf_token %}
                            <fieldset>
                                {% if form.errors %}
                                    <div class="alert alert-danger">
                                        {% if form.errors.password %}
                                            {% if form.errors.password %}
                                                Password: {{ form.errors.password|striptags }}<br>
                                            {% endif %}
                                        {% endif %}
                                    </div>
                                {% endif %}

                                <div class="form-group">
                                    <label for="id_email" class="sr-only">{{ form.login.label }}</label>
                                    {{ form.login }}
                                </div>

                                <div class="form-group">
                                    <label for="inputPassword" class="sr-only">{{ form.password.label }}</label>
                                    {{ form.password }}
                                </div>

                                {{ form.next }}

                                <button class="btn btn-lg btn-success btn-block" type=submit value=login>Login</button>
                            </fieldset>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </body>

</html>