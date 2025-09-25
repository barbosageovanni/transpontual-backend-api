  #!/usr/bin/env python3
  """
  Server entry point for Railway deployment
  Routes to FastAPI backend in backend_fastapi/app/main.py
  """
  import os
  import sys
  from pathlib import Path

  # Add backend_fastapi to Python path
  current_dir = Path(__file__).parent
  backend_path = current_dir / "backend_fastapi"
  sys.path.insert(0, str(backend_path))

  def start_server():
      """Start the FastAPI server"""
      try:
          # Import the FastAPI app from backend
          from app.main import app
          print("✅ FastAPI app imported successfully")

          # Start with uvicorn
          import uvicorn

          # Get port from Railway environment
          port = int(os.getenv("PORT", 8000))
          host = "0.0.0.0"

          print(f"🚀 Starting Transpontual API on {host}:{port}")
          print(f"🩺 Health check: http://{host}:{port}/health" )
          print(f"📚 Docs: http://{host}:{port}/docs")

          # Start server with Railway-compatible settings
          uvicorn.run(
              app,
              host=host,
              port=port,
              log_level="info",
              access_log=True,
              proxy_headers=True,
              forwarded_allow_ips="*"
          )

      except ImportError as e:
          print(f"❌ Failed to import FastAPI app: {e}")
          print(f"Current directory: {os.getcwd()}")
          print(f"Python path: {sys.path}")
          print("Files in current directory:")
          for item in Path.cwd().iterdir():
              print(f"  {item}")
          sys.exit(1)

      except Exception as e:
          print(f"❌ Server startup failed: {e}")
          sys.exit(1)

  if __name__ == "__main__":
      start_server()
