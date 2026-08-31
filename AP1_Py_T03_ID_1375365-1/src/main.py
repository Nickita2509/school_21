from di.container import Container
from web.module.game_module import create_app


def main():

    container = Container()

    app = create_app(container.service, container.repository)
    
    print("Сервер запущен на http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)


if __name__ == '__main__':
    main()