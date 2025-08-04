from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import boto3

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


## VAR
REGION_NAME = ""
AWS_ACCOUNT_ID = ""


## Dashboard

INITIAL_DASHBOARD_ID = "" 

## Q&A Generative
INITIAL_TOPIC_ID = ""



@app.get("/embed-dashboard-url")
async def get_embed_dashboard_url():
    """
    Generates an embed URL for a specific QuickSight Dashboard.
    """
    try:
        client = boto3.client("quicksight", region_name=REGION_NAME)
        response = client.generate_embed_url_for_registered_user(
            AwsAccountId=AWS_ACCOUNT_ID,
            UserArn="arn:aws:quicksight:<region>:<aws-account>:user/default/<username>",
            ExperienceConfiguration={
                'Dashboard': {'InitialDashboardId': INITIAL_DASHBOARD_ID}
            },
            AllowedDomains=["http://localhost:8080"],
            SessionLifetimeInMinutes=60
        )
        return {"embed_url": response["EmbedUrl"]}
    except client.exceptions.InvalidParameterValueException as e:
        raise HTTPException(status_code=400, detail=f"Invalid parameter: {str(e)}")
    except client.exceptions.ResourceNotFoundException as e:
        raise HTTPException(status_code=404, detail=f"Dashboard or User not found: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@app.get("/embed-generative-qna-url")
async def get_embed_generative_qna_url():
    """
    Generates an embed URL for the QuickSight Generative Q&A experience.
    """
    try:
        client = boto3.client("quicksight", region_name=REGION_NAME)
        response = client.generate_embed_url_for_registered_user(
            AwsAccountId=AWS_ACCOUNT_ID,
            UserArn="arn:aws:quicksight:<region>:<aws-account>:user/default/<username>",
            ExperienceConfiguration={
                'GenerativeQnA': {'InitialTopicId': INITIAL_TOPIC_ID }
            },
            AllowedDomains=["http://localhost:8080"],
            SessionLifetimeInMinutes=60
        )
        return {"embed_url": response["EmbedUrl"]}
    except client.exceptions.InvalidParameterValueException as e:
        raise HTTPException(status_code=400, detail=f"Invalid parameter: {str(e)}")
    except client.exceptions.ResourceNotFoundException as e:
        raise HTTPException(status_code=404, detail=f"Q Topic or User not found: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
