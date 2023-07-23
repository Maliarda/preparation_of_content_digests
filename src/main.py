import sys
from pathlib import Path


# This path was added to solve some problems with absolute
# imports in order to run this script as an executable file.
sys.path.append(str(Path(__file__).parent.parent))

import uvicorn
from fastapi import FastAPI

from src.api.endpoints import router
from src.core import get_settings
from src.migrations.main import main as run_migration


settings = get_settings()


def get_application() -> "FastAPI":
    """Get FastAPI app"""

    app = FastAPI(
        title=settings.project_name,
        root_path=settings.root_path,
        version=settings.app_version,
        debug=settings.debug,
    )

    app.include_router(router, prefix=settings.api_prefix)
    return app


app = get_application()


def main():
    run_migration(settings.sqlalchemy.url)
    uvicorn.run(**settings.uvicorn.dict())


if __name__ == "__main__":
    main()
