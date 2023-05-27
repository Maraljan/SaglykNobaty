import uvicorn

from health_time import application

app = application.create_app()


def main():
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8000,
        reload=True,
    )


if __name__ == '__main__':
    main()
