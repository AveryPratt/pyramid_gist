from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import MyModel


@view_config(route_name='home', renderer='../templates/home.jinja2')
def my_view_home(request):
    try:
        query = request.dbsession.query(MyModel)
        name = query.filter(MyModel.name == 'avery').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'name': name}


@view_config(route_name='login', renderer='../templates/login.jinja2')
def my_view_edit(request):
    try:
        query = request.dbsession.query(MyModel)
        name = query.filter(MyModel.name == 'avery').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'name': name}


@view_config(route_name='edit', renderer='../templates/edit.jinja2')
def my_view_login(request):
    try:
        query = request.dbsession.query(MyModel)
        name = query.filter(MyModel.name == 'avery').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'name': name}


@view_config(route_name='create', renderer='../templates/create.jinja2')
def my_view_create(request):
    try:
        query = request.dbsession.query(MyModel)
        name = query.filter(MyModel.name == 'avery').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'name': name}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_gist_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
