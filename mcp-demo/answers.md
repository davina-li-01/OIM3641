In-class Activity 22 – MCP and the Python SDK
Davina Li

Q6. Compare classify_iris in mcp_server.py with predict in api.py. Which one does the actual prediction? What does the MCP version add?

predict in api.py does the actual prediction. It loads the trained model and calls model.predict on the four measurements. classify_iris never touches the model. It just forwards the four numbers to the API over HTTP and hands the answer back as a sentence. What MCP adds is not more machine learning, it is a layer that makes the model discoverable and callable by an AI app. It gives the function a name, a plain language description, and a typed input schema that any MCP host (Claude Desktop, Cursor, etc.) can read at runtime and call through a standard protocol, without anyone writing custom integration code.

Q8a. The client printed a tool name, a description and its inputs without reading your code. Where in mcp_server.py did each one come from?

Tool name: the Python function name, classify_iris, registered by the @mcp.tool() decorator.
Description: the function's docstring.
Inputs: the function's parameters and their type hints. Each float became a "number" in the JSON schema, and the titles (e.g. "Sepal Length") were generated from the parameter names.

Q8b. Both /docs and this output describe the same model. Who is each one written for?

/docs is written for human developers. It is a page you read, click "Try it out" on, and use to write code against the endpoint. The client output is written for an AI model. It is what an LLM reads at runtime to decide whether a tool is relevant to the user's request and what arguments to pass to it.

Q9. With the docstring changed to "Does a calculation.", if you were an LLM and a user asked "What kind of iris is this?", would you know to call this tool? What does that tell you about who the docstring is really for?

Probably not. The tool name still hints at it, but "Does a calculation" tells me nothing about irises, species, or what inputs mean, so I would have no confidence it answers the question and might skip it or guess. That shows the docstring is really written for the LLM. In a normal codebase a docstring is a note for other programmers, but in an MCP server it is effectively the prompt that decides whether the model ever uses the tool. A vague description makes a working tool invisible.

Q12. Try 6.0, 2.7, 5.1, 1.6: how sure is the model?

Not very sure. It returns setosa 0%, versicolor 68%, virginica 32%. This flower sits on the border between versicolor and virginica. classify_iris would just say "versicolor" and hide that uncertainty, which is exactly why iris_probabilities is useful and why its docstring tells the model to use it when the user asks how confident the prediction is or when a flower might be borderline.

Q13. Does your team's prototype need an MCP server? Why or why not?

No. Our prototype is an interview prep tool: a user enters a company and a job listing and gets prep materials back. It is a single Streamlit app where we control both the UI and the LLM call, and our code calls Gemini directly in a fixed order. No outside AI app needs to discover our functions, and our own model is not choosing between tools at runtime, so an MCP server would add a layer without adding value. It would become a yes if we wanted people to use the prep tool from inside an AI app they already use (like Claude or Cursor) instead of our Streamlit page, or if we broke the product into reusable capabilities (for example research a company, parse a job listing, generate practice questions, pull a user's saved resume) that different agents or apps should be able to discover and call on their own. At that point the docstrings and schemas become the product's interface, and MCP is the standard way to expose them.
