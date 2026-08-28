from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(
    title = "tech_solution_API",
    description ="CRM para techlog solutions",
    version ="1.0.0",
)


@app.get("/")
async def health_check():
    return {"status":"OK"}

@app.get("/front",response_class =HTMLResponse)
async def front_page():
    html_content = """
        <html>
            <head>
            <title>TechLog Solutions</title>
            </head>
            <body>
                <h1>TechLog Solutions</h1>
            </body>
        </html>
    """
    return html_content
