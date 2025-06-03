import subprocess

def talk_to_agent(prompt):
    command = f"A user wants fashion advice blending tradition and modern trend: {prompt}"
    result = subprocess.run(["ollama", "run", "tinyllama", command], capture_output=True, text=True)
    return result.stdout.strip()
