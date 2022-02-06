# Instagram Bot v2

This is version 2 of a bot that was built to automate tedious and boring Instagram tasks.

# Main Flow

## Farm hashtags (Not implemented for production)

1. Start the application
-- app starts and opens up the browsers
-- app prompts you several accounts with usernames and passwords to use to login
2. Login to Instagram
3. Confirm on app. Begin 5 second countdown before hashtag farming begins
-- app begins farming hashtags around a certain niche
-- interMETHODS with the terminal can occur to change the queue? << FUTURE UPGRADE >>

## Farm users & niches

N/A

## Farm popular posts from users in my niche / market

N/A

# Commands

```pytest```  
```python main.py```  

# Dev Notes

Motivation for this project was to see If it was posssible to automate tedious tasks with Instagram. Yes. Python makes it very easy to do so... far easier than anticipated.

## File Structure

```
- x
  - .pytest_cache
  - .venv
  - .vscode
  - src
    - agents
      - controls
        - keyboard.py
        - mouse.py
        - screen.py
      - instagram.py
      - browser.py
      - agent.py
    - builders
      - content_builder
      - bot_builder.py
      - username_builder.py
    - console
    - controls
    - data
    - http_listener
    - interaction_logger
    - utils
      - wrappers
      - dtos
    - virtualization
    - app.py
    - programs.py
    - state.py
  - .gitignore
  - main.py
  - README.md
  - requirements.txt
```
