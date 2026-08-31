import os
from di.container import Container
from web.module.game_module import create_app
from datasource.database import init_db


def main():
    container = Container()
    init_db(container.engine)
    app = create_app(container)

    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', '5000'))
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'

    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        print(f"Сервер запущен на http://{host}:{port}")

    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()