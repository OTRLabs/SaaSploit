from __future__ import annotations
from rich.console import Console
from datetime import datetime
import asyncio

async def main() -> None:
    console: Console = Console()
    console.print(f"Launching SaaSploit - {datetime.now()}")


if __name__ == "__main__":

    asyncio.run(main())
