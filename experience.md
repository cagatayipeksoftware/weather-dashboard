# Experience Documentation

## 1. Tool Selection Justification

For this project, I chose **Cursor**. I selected it because it is currently the most discussed "Vibe Coding" tool in the developer community and I wanted to see if the hype was real.
What made it appealing was its "Composer" feature (Ctrl+I), which allows you to edit multiple files at once using natural language. Unlike standard Copilot, Cursor feels like a complete fork of VS Code designed specifically for AI-native development.

## 2. Development Process

I used Cursor as a "pair programmer" rather than just an autocomplete tool.

- **Workflow:** I started by creating an empty folder and opening the Cursor Chat (Cmd+L).
- **Prompts:** My most effective prompt was: _"Create a Python GUI using Tkinter for a weather dashboard. It should fetch data from a free API without requiring an API key (like Open-Meteo). Structure it with a class."_
- **Iterations:** It took about 3 iterations to get fully working code. The first version didn't handle errors well (e.g., if the city wasn't found), so I used the "Edit" feature to highlight the code and asked it to _"Add error handling for invalid city names."_

## 3. Challenges and Solutions

- **Difficulty:** The main difficulty was handling the asynchronous nature of API calls within a GUI (Tkinter) without freezing the app.
- **AI Solution:** The AI tool recognized this potential issue and kept the API logic simple for this specific homework scope. When I asked it to make the UI look better, it suggested specific padding and font sizes that I wouldn't have known manually.
- **Manual Fixes:** I had to manually adjust the geometry of the window because the initial AI suggestion was too small for the text it generated. I also tweaked the "City not found" message to be more user-friendly.

## 4. Reflection

- **Surprise:** I was surprised by how much context Cursor holds. I didn't have to copy-paste the error message; I just clicked "Add to Chat" in the terminal, and it fixed the bug immediately.
- **Workflow Change:** My workflow changed from "write-run-debug" to "prompt-review-refine." I spent more time reading code than writing syntax.
- **Future Use:** I would definitely use this for future projects, especially for boilerplate setup. It removes the "blank page" paralysis.
- **Impact:** I believe this technology will lower the barrier to entry for coding but will raise the bar for "system design" skills. Developers will need to be better at explaining _what_ they want rather than knowing exactly _how_ to write the syntax.
