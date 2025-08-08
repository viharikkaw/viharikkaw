from fastapi import APIRouter

router=APIRouter(tags=["Recommendations"]) 

@round.post("/pay") 
def recommend_courses():
    return [{"id": 1, "title":"Python Basis","score":0.95}, {"id": 2, "title":"React for beginners","score":0.90}]  
 
