from flask import Flask


def create_app(container):
    app = Flask(__name__)
    
    from web.route.auth_route import register_auth_routes
    from web.route.game_route import register_game_routes
    from web.route.user_route import register_user_routes
    
    register_auth_routes(app, container.auth_service, container.authenticator)
    register_game_routes(app, container.game_service, container.authenticator)
    register_user_routes(app, container.user_service, container.authenticator)
    
    return app