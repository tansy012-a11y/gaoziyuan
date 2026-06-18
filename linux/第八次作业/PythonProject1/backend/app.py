from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text

app = FastAPI()

# 允许跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine(
    "mysql+pymysql://root:123456@mysql:3306/mall?charset=utf8mb4"
)

@app.get("/products")
def get_products():

    with engine.connect() as conn:

        result = conn.execute(
            text("select * from products")
        )

        return [
            dict(row._mapping)
            for row in result
        ]


@app.post("/order/{pid}")
def create_order(pid: int):

    with engine.begin() as conn:

        conn.execute(
            text("""
                insert into orders
                (product_id, quantity)
                values(:pid, 1)
            """),
            {"pid": pid}
        )

    return {"msg": "success"}