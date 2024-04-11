from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Article(BaseModel):
    id: int
    title: str
    url: str
    year: int

# Route to add a new article
@app.post("/articles")
def create_article(article: Article):
    articles.append(article)
    return article

# Route to get all articles
@app.get("/articles")
def get_articles():
    return articles

# Route to get a specific article by ID
@app.get("/articles/{article_id}")
def get_article(article_id: int):
    for article in articles:
        if article.id == article_id:
            return article
    raise HTTPException(status_code=404, detail="Article not found")

articles = [
    Article(id=1,
            title="Distributed Cloud Architecture for Resilient Systems: Rethink Your Approach To Resilient Cloud Services",
            url="https://dzone.com/articles/distributed-cloud-architecture-for-resilient-syste", year=2023),
    Article(id=2, title="Using Unblocked to Fix a Service That Nobody Owns",
            url="https://dzone.com/articles/using-unblocked-to-fix-a-service-that-nobody-owns", year=2023),
    Article(id=3, title="Exploring the Horizon of Microservices With KubeMQ's New Control Center",
            url="https://dzone.com/articles/exploring-the-horizon-of-microservices-with-kubemq", year=2024),
    Article(id=4, title="Build a Digital Collectibles Portal Using Flow and Cadence (Part 1)",
            url="https://dzone.com/articles/build-a-digital-collectibles-portal-using-flow-and-1", year=2024),
    Article(id=5, title="Build a Flow Collectibles Portal Using Cadence (Part 2)",
            url="https://dzone.com/articles/build-a-flow-collectibles-portal-using-cadence-par-1", year=2024),
    Article(id=6,
            title="Eliminate Human-Based Actions With Automated Deployments: Improving Commit-to-Deploy Ratios Along the Way",
            url="https://dzone.com/articles/eliminate-human-based-actions-with-automated-deplo", year=2024),
    Article(id=7, title="Vector Tutorial: Conducting Similarity Search in Enterprise Data",
            url="https://dzone.com/articles/using-pgvector-to-locate-similarities-in-enterpris", year=2024),
    Article(id=8, title="DevSecOps: It's Time To Pay for Your Demand, Not Ingestion",
            url="https://dzone.com/articles/devsecops-its-time-to-pay-for-your-demand", year=2024),
]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
