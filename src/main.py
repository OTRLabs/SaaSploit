from __future__ import annotations
from rich.console import Console
from datetime import datetime
import asyncio
from saasploit.application import application_runner

async def main(project_directory: str) -> None:
    console: Console = Console()
    console.print(f"Launching SaaSploit - {datetime.now()}")
    asyncio.run(application_runner(console=console, project_directory))

if __name__ == "__main__":

    asyncio.run(main())
