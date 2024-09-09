import language_tool_python

def check_grammar(file):
    tool = language_tool_python.LanguageTool('en-US')
    text = file.read().decode('utf-8')
    matches = tool.check(text)
    return {"grammar_errors": len(matches), "suggestions": matches}
