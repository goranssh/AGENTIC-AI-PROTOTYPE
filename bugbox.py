from datetime import datetime

def ask_user(prompt):
    return input(prompt + "\n> ")

def agent_conversation():
    print(" Welcome to BugBox - your smart bug reporting assistant!")

    bug_desc = ask_user("Please describe the bug you encountered.")
    system = ask_user("Which system or platform did this happen on?")
    frequency = ask_user("How often does it happen? (e.g., always, sometimes)")
    impact = ask_user("How severe is it? (low/medium/high)")
    steps = ask_user("Can you describe the steps to reproduce it?")
    
    summary = f"""
📋 Bug Report Summary:
- Description: {bug_desc}
- System: {system}
- Frequency: {frequency}
- Impact: {impact}
- Reproduction Steps: {steps}
- Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

    print("\n✅ Thank you! Here's a summary of your bug report:")
    print(summary)

    # Save to file
    with open("bug_log.txt", "a") as log:
        log.write(summary + "\n" + "-"*40 + "\n")

if __name__ == "__main__":
    agent_conversation()
