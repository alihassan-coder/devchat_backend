from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserLogin
from utils.security import hash_password, verify_password, create_access_token
from configuration.databaseconfig import db
from pymongo.errors import PyMongoError

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    try:
        # Check if user already exists
        existing_user = await db.users.find_one({"email": user.email})
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")

        # Prepare user data
        user_data = {
            "name": user.name,
            "second_name": user.second_name,
            "email": user.email,
            "hashed_password": hash_password(user.password)
        }

        # Save user to DB
        await db.users.insert_one(user_data)
        return {
            "message": "Registered successfully",
            "status": "Success",
            "code": 201,
            }

    except PyMongoError as e:
        raise HTTPException(status_code=500, detail="Database error: " + str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected error: " + str(e))

@router.post("/login")
async def login(user: UserLogin):
    try:
        # Find user by email
        existing_user = await db.users.find_one({"email": user.email})
        if not existing_user:
            raise HTTPException(status_code=400, detail="Invalid email or password")

        # Check password
        if not verify_password(user.password, existing_user["hashed_password"]):
            raise HTTPException(status_code=400, detail="Invalid email or password")

        # Generate JWT token
        token = create_access_token({"sub": user.email})
        return {
            "message": "Login successful",
            "status": "Success",
            "code": 200,
            "access_token": token, 
            "token_type": "bearer"
            }

    except PyMongoError as e:
        raise HTTPException(status_code=500, detail="Database error: " + str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected error: " + str(e))