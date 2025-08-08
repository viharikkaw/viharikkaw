from fastapi import APIRouter,Depends,HTTPException 
from sqlalchemy.orm import session
import database,models,schemas,utils 

router=APIRouter(tags="Courses") 

@router.post("/",response_model=schemas.CourseCreate) 
def create_course(course: schemas.CourseCreate,db: session=Depends(database.get_db)):
    new_course=models.Course(**course.dict(), instructor_id=1) 
    db.add(new_course) 
    db.commit() 
    db.refresh(new_course) 
    return new_course 
@router.get("/") 
def list_course(db:session=Depends(database.get_db)):
    return db.query(models.Course).all()  