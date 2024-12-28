import backend

if __name__ == '__main__':
    app = backend.create_app()
    app.run(debug=True)