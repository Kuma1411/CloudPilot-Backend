
from fastapi import FastAPI
from model import CloudPilot
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware

html = """[
    {
        "type": "a",
        "id": "",
        "className": "navbar-brand mx-3 mx-lg-0 mr-auto d-none d-lg-flex",
        "textContent": "",
        "href": "https://xathon.mettl.com/event/amazonmlsummerschool"
    },
    {
        "type": "button",
        "id": "",
        "className": "btn header-btn",
        "textContent": "Hackathons",
        "href": ""
    },
    {
        "type": "button",
        "id": "",
        "className": "btn header-btn",
        "textContent": "Blogs",
        "href": ""
    },
    {
        "type": "button",
        "id": "",
        "className": "btn btn-primary",
        "textContent": "Login",
        "href": ""
    },
    {
        "type": "button",
        "id": "",
        "className": "btn btn-outline-primary",
        "textContent": "Sign Up",
        "href": ""
    },
    {
        "type": "button",
        "id": "",
        "className": "dropdown-toggle btn btn-link btn-language p-0",
        "textContent": "",
        "href": ""
    },
    {
        "type": "a",
        "id": "",
        "className": "",
        "textContent": "",
        "href": "https://support.mettl.com/portal/en/home"
    },
    {
        "type": "button",
        "id": "",
        "className": "btn btn-outline-blue px-3 px-lg-3 px-xl-3 min-w-auto btn-height border-blue rounded mx-lg-0 ml-md-0 share-btn ng-star-inserted",
        "textContent": "",
        "href": ""
    },
    {
        "type": "button",
        "id": "",
        "className": "btn ft-14 rounded ml-2 btn-height px-4 font-mxs-size add-btn btn-blue disabled border-0 ng-star-inserted",
        "textContent": "Registration Closed",
        "href": ""
    },
    {
        "type": "button",
        "id": "",
        "className": "btn ft-14 px-1 rounded py-2 px-4 font-mxs-size add-btn btn-blue disabled border-0 ng-star-inserted",
        "textContent": "REGISTRATION CLOSED",
        "href": ""
    },
    {
        "type": "button",
        "id": "",
        "className": "btn btn-outline-blue px-3 min-w-auto rounded ml-2 py-2",
        "textContent": "",
        "href": ""
    },
    {
        "type": "button",
        "id": "truste-show-consent",
        "className": "trustarc-secondary-btn",
        "textContent": "Manage Cookies",
        "href": ""
    },
    {
        "type": "button",
        "id": "truste-consent-button",
        "className": "trustarc-primary-btn trustarc-acceptall-btn trustarc-agree-btn",
        "textContent": "Okay",
        "href": ""
    }
]

"""



app = FastAPI()


# Define allowed origins for CORS
origins = [
    "*",  
]

# Add CORSMiddleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


class UI(BaseModel):
    className: str
    textContent: str


class PredictionPayload(BaseModel):
    prompt: str
    context: List[UI]



@app.post("/predict")
def predict(predictionPayload:PredictionPayload):
    context_str = str(predictionPayload.context)
    cloudPilot = CloudPilot()
    prediction_result = cloudPilot.predict(predictionPayload.prompt, context_str)
    
    # Structure the response in JSON format with status 200
    return JSONResponse(
        status_code=200,
        content={
            "prediction": prediction_result
        }
    )

