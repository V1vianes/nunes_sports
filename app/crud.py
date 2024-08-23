from sqlalchemy.orm import Session
from . import models, schemas

def get_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(models.Produto.id == produto_id).first()

def get_produto_by_codigo(db: Session, codigo: str):
    return db.query(models.Produto).filter(models.Produto.codigo == codigo).first()

def get_produtos(db: Session):
    return db.query(models.Produto).all()

def _commit_and_refresh(db: Session, obj):
    try:
        db.commit()
        db.refresh(obj)
    except Exception as e:
        db.rollback()
        raise e

def create_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto = models.Produto(**produto.dict())
    db.add(db_produto)
    _commit_and_refresh(db, db_produto)
    return db_produto

def update_produto(db: Session, produto_id: int, produto: schemas.ProdutoUpdate):
    db_produto = get_produto(db, produto_id)
    if db_produto:
        for key, value in produto.dict().items():
            setattr(db_produto, key, value)
        _commit_and_refresh(db, db_produto)
    return db_produto

def delete_produto(db: Session, produto_id: int):
    db_produto = get_produto(db, produto_id)
    if db_produto:
        db.delete(db_produto)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
