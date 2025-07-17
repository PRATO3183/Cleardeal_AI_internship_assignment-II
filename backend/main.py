from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import joblib
# import re

import sys, os
sys.path.append(os.path.dirname(__file__))
from reranker import rerank_score

app = FastAPI()
@app.get("/") # so that the bat file knows where to look.
def read_root():
    return {"message": "It works!"}

model = joblib.load("model.pkl")

class LeadInput(BaseModel):
    email: EmailStr
    credit_score: int
    income: int
    family_background: str
    age_group: str
    comments: str
    consent: bool

def preprocess(data: LeadInput):
    family_map = {"Single": 0, "Married": 1, "Married with Kids": 2}
    age_map = {"18–25": 0, "26–35": 1, "36–50": 2, "51+": 3}
    return [[
        data.credit_score,
        data.income,
        family_map.get(data.family_background, 0),
        age_map.get(data.age_group, 0)
    ]]

@app.post("/score")
def score_lead(lead: LeadInput):
    if not lead.consent:
        raise HTTPException(status_code=400, detail="Consent is required.")
    
    features = preprocess(lead)
    pred_score = int(model.predict_proba(features)[0][1] * 100)
    final_score = rerank_score(pred_score, lead.comments)
    
    return {
        "email": lead.email,
        "initial_score": pred_score,
        "reranked_score": final_score,
        "comments": lead.comments
    }