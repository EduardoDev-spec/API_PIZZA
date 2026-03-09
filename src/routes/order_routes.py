from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.dependencies.dependencies import get_session
from src.schemas.schemas import OrderSchema
from src.models.models import Order

order_router = APIRouter(prefix='/orders', tags=['orders'])

@order_router.get("/")
async def orders():
    """
    Essa é a rota padrão de pedidos do sistema
    """
    return {'message': 'Vc acessou a rota order'}

@order_router.post('/order')
async def create_order(order_schema: OrderSchema, session: Session = Depends(get_session)):
    new_order = Order(user=order_schema.user)
    session.add(new_order)
    session.commit()
    return {'message': f'Pedido criado com sucesso. ID do pedido: {new_order.id}'}
