from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db
from fastapi.staticfiles import StaticFiles

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

# Inicializar a aplicação FastAPI
app = FastAPI()

# Configurar Jinja2
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(get_db)):
    produtos = crud.get_produtos(db)
    return templates.TemplateResponse("index.html", {"request": request, "produtos": produtos})

@app.get("/create", response_class=HTMLResponse)
async def create_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/create")
async def create_produto(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    try:
        produto = schemas.ProdutoCreate(
            nome=form.get("nome"),
            codigo=form.get("codigo"),
            descricao=form.get("descricao"),
            preco=float(form.get("preco"))
        )
        crud.create_produto(db, produto)
        return RedirectResponse(url='/', status_code=303)
    except ValueError:
        return templates.TemplateResponse(
            "create.html", 
            {"request": request, "error_message": "Preço inválido"}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "create.html", 
            {"request": request, "error_message": f"Erro ao criar produto: {str(e)}"}
        )

@app.get("/edit/{produto_id}", response_class=HTMLResponse)
async def edit_form(request: Request, produto_id: int, db: Session = Depends(get_db)):
    produto = crud.get_produto(db, produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return templates.TemplateResponse("edit.html", {"request": request, "produto": produto})

@app.post("/edit/{produto_id}")
async def update_produto(produto_id: int, request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    try:
        produto = schemas.ProdutoUpdate(
            nome=form.get("nome"),
            descricao=form.get("descricao"),
            preco=float(form.get("preco"))
        )
        db_produto = crud.update_produto(db, produto_id, produto)
        if db_produto is None:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return RedirectResponse(url='/', status_code=303)
    except ValueError:
        return templates.TemplateResponse(
            "edit.html", 
            {"request": request, "produto": produto, "error_message": "Preço inválido"}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "edit.html", 
            {"request": request, "produto": produto, "error_message": f"Erro ao atualizar produto: {str(e)}"}
        )

@app.post("/delete/{produto_id}")
async def delete_produto(produto_id: int, db: Session = Depends(get_db)):
    try:
        db_produto = crud.get_produto(db, produto_id)
        if db_produto is None:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        crud.delete_produto(db, produto_id)
        return RedirectResponse(url='/', status_code=303)
    except HTTPException:
        raise
    except Exception as e:
        return RedirectResponse(url='/', status_code=303)
