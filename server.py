  import os
  import sys
  sys.path.insert(0, 'backend_fastapi')
  from app.main import app
  import uvicorn

  if __name__ == "__main__":
      port = int(os.getenv("PORT", 8000))
      uvicorn.run(app, host="0.0.0.0", port=port)
