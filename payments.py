from fastapi import APIRouter

router=APIRouter(tags=["Payments"]) 

@round.post("/pay") 
def make_payment():
    return {"status": "success","message":"Payment processed"} 
 
