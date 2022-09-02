import uvicorn
import os

if __name__ == "__main__":

    # even though uvicorn is running on 0.0.0.0 check 127.0.0.1 from the browser

    if "code" in os.getcwd():
        uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="debug",
                    proxy_headers=True, reload=True)
    else:
        # for running locally from IDE without docker
        uvicorn.run("app.app:app", host="0.0.0.0", port=8000, log_level="debug",
                    proxy_headers=True, reload=True)