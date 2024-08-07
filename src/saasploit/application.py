from __future__ import annotations



from rich.console import Console


from rich.panel import Panel
from rich.progress import Progress
from datetime import datetime



async def application_runner(console: Console, scope: str) -> None:

    
    console.print(f"Launching Textual TUI dashboard for analysis of scope: {scope} - {datetime.now()}\n\n")
    
    console.print(f"Extracting scope from directory provided\n\n")
    console.clear()
    
    






