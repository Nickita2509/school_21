from flask import Flask


def create_app(game_service, game_repository):

    app = Flask(__name__)
    
    from web.route.game_route import register_routes
    register_routes(app, game_service, game_repository)
    
    return app