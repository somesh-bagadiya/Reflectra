import subprocess
import os

def run_reverse_workflow():
    # Activate virtual environment
    venv_path = "./venv/bin/activate"
    if os.name == 'nt':
        venv_path = "./venv/Scripts/activate"
    activate_command = f"source {venv_path} && " if os.name != 'nt' else f"{venv_path} && "

    # Workflow defined in reverse order
    workflow = [
        "redis_agent.py",
        "summary_agent.py",
        "display_agent.py",
        "transcribing_agent.py",
        "recording_agent.py",
        "sender_agent.py"
    ]

    # Run each Python file in reverse order within the virtual environment
    for agent in workflow:
        print(f"Running {agent}...")
        subprocess.run(f"{activate_command} python {agent}", shell=True, executable='/bin/bash')

# Execute the function
run_reverse_workflow()
