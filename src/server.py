import uvicorn

if __name__ == "__main__":

    # run the server
    uvicorn.run("app:app", host="0.0.0.0", reload=True)
