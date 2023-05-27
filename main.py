import uvicorn

from health_time import application

app = application.create_app()


def main():
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8000,
        reload=True,
    )


if __name__ == '__main__':
    main()
