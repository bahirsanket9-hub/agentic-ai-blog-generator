from typing import TypedDict

class BlogState(TypedDict):
    topic: str
    blog: dict  # Contains title and content
    current_language: str
    
    
    