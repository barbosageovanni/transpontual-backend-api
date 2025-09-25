<<<<<<< HEAD
  import os
=======
 import os
>>>>>>> 61311663062c3d52a9306f76bc65e24208df8e8c
  import uvicorn

  if __name__ == "__main__":
      port = int(os.getenv("PORT", 8000))
      uvicorn.run(
          "backend_fastapi.app.main:app",
          host="0.0.0.0",
          port=port,
          log_level="info"
<<<<<<< HEAD
      )
=======
      )
>>>>>>> 61311663062c3d52a9306f76bc65e24208df8e8c
