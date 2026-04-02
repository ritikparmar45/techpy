import httpx
import asyncio
import json
import time

BASE_URL = "http://localhost:8000"

async def test_candidate_api():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        # Create a unique email using timestamp
        unique_email = f"john_{int(time.time())}@example.com"
        
        # 1. Health Check
        print("Checking health...")
        health = await client.get("/")
        print(f"Health response: {health.json()}")

        # 2. Create Candidate
        print("\nCreating candidate...")
        candidate_data = {
            "name": "John Doe",
            "email": unique_email,
            "skill": "Python",
            "status": "applied"
        }
        create_res = await client.post("/candidates/", json=candidate_data)
        if create_res.status_code == 201:
            candidate = create_res.json()
            candidate_id = candidate["_id"]
            print(f"Candidate created with ID: {candidate_id}")
        else:
            print(f"Failed to create candidate: {create_res.text}")
            return

        # 3. Get All Candidates
        print("\nGetting all candidates...")
        get_res = await client.get("/candidates/")
        print(f"Found {len(get_res.json())} candidates.")

        # 4. Get Candidates with filtering
        print("\nFiltering candidates by status 'interview'...")
        filter_res = await client.get("/candidates/?status=interview")
        print(f"Found {len(filter_res.json())} candidates with status 'interview'.")

        # 5. Update Candidate Status
        print(f"\nUpdating candidate status to 'interview' for ID: {candidate_id}")
        update_data = {"status": "interview"}
        update_res = await client.put(f"/candidates/{candidate_id}/status", json=update_data)
        if update_res.status_code == 200:
            print(f"Updated status: {update_res.json()['status']}")
        else:
            print(f"Failed to update status: {update_res.text}")

if __name__ == "__main__":
    print("Ensure your FastAPI server and MongoDB are running before executing this script.")
    try:
        asyncio.run(test_candidate_api())
    except Exception as e:
        print(f"Error during testing: {e}")
