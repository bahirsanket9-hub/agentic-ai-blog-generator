import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from src.graphs.graph_builder import GraphBuilder
from src.llms.openaillm import OpenaiLlm
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

class BlogRequest(BaseModel):
    topic: str
    
@app.post("/blogs")
async def create_blog(req: BlogRequest):
    topic = req.topic
    #LLM
    openllm = OpenaiLlm()
    llm = openllm.get_llm()
    
    #Graph
    
    graph_builder = GraphBuilder(llm)
    graph = graph_builder.setup_graph(usecase="topic")
    
    initial_state = {
        "topic": topic,
        "blog": {"title": "", "content": ""},
        "current_language": "en"
    }
    state = graph.invoke(initial_state)

    return {"data": state}
    
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port = 8000, reload=True)