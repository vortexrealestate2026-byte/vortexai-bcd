from src.tasks.property_task import run_property_agent


async def launch_property_agent():
    print("🏠 Launching Property Agent")
    await run_property_agent()
