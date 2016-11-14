{% load staticfiles %}
{% load connect_buttons %}

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

        <link rel="stylesheet" type="text/css" href="{% static 'assets/bootstrap/3.3.5/css/bootstrap.css' %}">
        <link rel="stylesheet" type="text/css" href="{% static 'assets/font-awesome/4.3.0/css/font-awesome.min.css' %}" media="all" />

        <style>
            .btn-facebook {
                color: #fff;
                background-color: #4267b2;
            }
            .btn-facebook:hover, .btn-facebook:focus, .btn-facebook:active, .btn-facebook.active, .open>.dropdown-toggle.btn-facebook {
                color: #fff;
                background-color: #365899;
            }

            .btn-google {
                color: #fff;
                background-color: #f4511e;
            }
            .btn-google:hover, .btn-google:focus, .btn-google:active, .btn-google.active, .open>.dropdown-toggle.btn-google {
                color: #fff;
                background-color: #db4437;
            }

            .btn-linkedin {
                color: #fff;
                background-color: #287bbc;
            }
            .btn-linkedin:hover, .btn-linkedin:focus, .btn-linkedin:active, .btn-linkedin.active, .open>.dropdown-toggle.btn-linkedin {
                color: #fff;
                background-color: #1b5480;
            }

            .btn-twitter {
                color: #fff;
                background-color: #55ACEF;
            }
            .btn-twitter:hover, .btn-twitter:focus, .btn-twitter:active, .btn-twitter.active, .open>.dropdown-toggle.btn-twitter {
                color: #fff;
                background-color: #1B95E0;
            }

            .btn-github {
                color: #fff;
                background-color: #505050;
            }
            .btn-github:hover, .btn-github:focus, .btn-github:active, .btn-github.active, .open>.dropdown-toggle.btn-github {
                color: #fff;
                background-color: #444;
            }
        </style>
        <title>Welcome | {{ site.name }}</title>
    </head>

    <body>
        {% if request.user.is_authenticated %}
            <div class="container">
                <h1>
                    <span>Welcome! </span>
                    <a type="button" href="/logout" class="btn btn-default btn-sm pull-right">
                        <span class="glyphicon glyphicon-log-out"></span> Log out
                    </a>
                </h1>
                <hr/>
            </div>

            <div class="container">
                <h2>User information</h2>
                <table class="table table-striped table-bordered table-hover">
                    <thead>
                        <tr>
                            <th>Firstname</th>
                            <th>Lastname</th>
                            <th>Email</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{{user.first_name}}</td>
                            <td>{{user.last_name}}</td>
                            <td>{{user.email}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        {% else %}
            <div class="container">
                <h1>
                    <span>Welcome! Please Sign In</span>
                </h1>
                <hr/>
            </div>

            <div>
                <div class="row">
                    <div class="col-md-3 col-md-offset-1">
                        <!-- Facebook connect button -->
                        {% connect_button facebook %}
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-md-3 col-md-offset-1">
                        <!-- Google connect button -->
                        {% connect_button google %}
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-md-3 col-md-offset-1">
                        <!-- Linkedin connect button -->
                        {% connect_button linkedin %}
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-md-3 col-md-offset-1">
                        <!-- Linkedin connect button -->
                        {% connect_button github %}
                    </div>
                </div>
            </div>
        {% endif %}
    </body>

</html>