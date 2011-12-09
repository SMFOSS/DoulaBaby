from pyramid.config import Configurator
from doulababy.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_view('doulababy.views.my_view',
                    context='doulababy:resources.Root',
                    renderer='doulababy:templates/mytemplate.pt')
    config.add_static_view('static', 'doulababy:static', cache_max_age=3600)
    return config.make_wsgi_app()
