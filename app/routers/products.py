from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/produtos", response_model=schemas.ProdutoOut)
def create_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    db_produto = crud.create_produto(db, produto)
    return db_produto

@router.get("/produtos", response_model=List[schemas.ProdutoOut])
def list_produtos(db: Session = Depends(get_db)):
    return crud.get_produtos(db)

@router.put("/produtos/{produto_id}", response_model=schemas.ProdutoOut)
def update_produto(produto_id: int, produto: schemas.ProdutoUpdate, db: Session = Depends(get_db)):
    db_produto = crud.update_produto(db, produto_id, produto)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_produto

@router.delete("/produtos/{produto_id}", response_model=schemas.ProdutoOut)
def delete_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produto = crud.get_produto(db, produto_id)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    crud.delete_produto(db, produto_id)
    return db_produto

