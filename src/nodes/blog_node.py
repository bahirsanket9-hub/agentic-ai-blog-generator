from src.states.blogstate import BlogState
from langchain_core.messages import HumanMessage, SystemMessage

class BlogNode:
    def __init__(self, llm):
        self.llm = llm
        
    def title_creation(self, state: BlogState):
        if "topic" in state and state["topic"]:
            prompt = """
            You are an expert blog content writer.
            Generate a creative blog title for: {topic}
            """
            system_message = SystemMessage(content=prompt.format(topic=state["topic"]))
            response = self.llm.invoke([system_message])
            return {"blog": {"title": response.content}}

    def content_creation(self, state: BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """
            you are an expert blog writer. use markdown formatting
            Generate a comprehensive blog content for the topic: {topic}
            The blog title is: {title}
            """
            title = state.get("blog", {}).get("title", "") if state.get("blog") else ""
            system_message = SystemMessage(content=system_prompt.format(topic=state["topic"], title=title))
            response = self.llm.invoke([system_message])
            return {"blog": {
              "title": state.get("blog", {}).get("title", "") if state.get("blog") else "",
              "content": response.content
            }}
            
          
            