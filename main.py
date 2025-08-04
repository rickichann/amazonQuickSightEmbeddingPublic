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

@app.get("/embed-dashboard-url")
async def get_embed_dashboard_url():
    """
    Generates an embed URL for a specific QuickSight Dashboard.
    """
    try:
        client = boto3.client("quicksight", region_name="ap-southeast-1")
        response = client.generate_embed_url_for_registered_user(
            AwsAccountId="484468819120",
            UserArn="arn:aws:quicksight:ap-southeast-1:484468819120:user/default/ics-de",
            ExperienceConfiguration={
                'Dashboard': {'InitialDashboardId': '310e4ae4-b240-4f85-b2a5-5625af3cea0f'}
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
        client = boto3.client("quicksight", region_name="ap-southeast-1")
        response = client.generate_embed_url_for_registered_user(
            AwsAccountId="484468819120",
            UserArn="arn:aws:quicksight:ap-southeast-1:484468819120:user/default/ics-de",
            ExperienceConfiguration={
                'GenerativeQnA': {'InitialTopicId': 'blGXZnP3aGJtAyqvlNwALuWPEZj3bfkn'}
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
