# NOTES:

When developing: follow 80/20. If it takes 80% of your time to develop and automate something that provides only 20% values, drop it and implement `terminal`.

# Main Flow

## Farm hashtags

1. Start the application
-- app starts and opens up the browsers
-- app prompts you several accounts with usernames and passwords to use to login
2. Login to Instagram
3. Confirm on app. Begin 5 second countdown before hashtag farming begins
-- app begins farming hashtags around a certain niche
-- interactions with the terminal can occur to change the queue? << FUTURE UPGRADE >>

## Farm users & niches

TBD

## Farm popular posts from users in my niche / market

1. 

# Commands

```pytest```  
```python main.py```  


# Dev Notes

## Terminology

| `TERM`    | `DEFINITION`
| -         | -
| app       | The application as a whole
| program   | Sections of the program that encapsulate different functions of the program


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