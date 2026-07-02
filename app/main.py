from fastapi import FastAPI

app = FastAPI(
    title="FortNog Product Hub",
    version="0.2.0"
)


@app.get("/")
def home():

    return {

        "application":"FortNog Product Hub",

        "version":"0.2.0"

    }
