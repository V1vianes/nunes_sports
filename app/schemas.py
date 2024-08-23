from pydantic import BaseModel, Field

class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=1)
    codigo: str = Field(..., min_length=1)
    descricao: str = Field(..., min_length=1)
    preco: float = Field(..., gt=0)

class ProdutoUpdate(BaseModel):
    nome: str = Field(..., min_length=1)
    descricao: str = Field(..., min_length=1)
    preco: float = Field(..., gt=0)

class ProdutoOut(BaseModel):
    id: int
    nome: str
    codigo: str
    descricao: str
    preco: float

    class Config:
        orm_mode = True
