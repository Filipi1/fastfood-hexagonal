from http import HTTPMethod
import uuid

from fastapi import Depends
from modules.authentication.adapters.presentation.dependencies import decode_auth_token
from modules.order.adapters.dtos.request_completion import RequestOrderCompletion
from modules.shared.adapters.presentation.decorators import (
    FastAPIManager,
    ControllerOptions,
    APIController,
)
from modules.user.domain.entities import User


@FastAPIManager.controller("order", ControllerOptions(tags="Order"))
class OrderController(APIController):
    def __init__(self):
        super().__init__()

    @FastAPIManager.route(
        "{id}/complete",
        method=HTTPMethod.POST,
        dependencies=[Depends(decode_auth_token)],
    )
    async def complete(self, id: str, request_payment: RequestOrderCompletion):
        return {
            "message": "Pagamento confirmado com sucesso",
            "data": {
                "order_id": id,
                "ticket": "S101",
            },
        }

    @FastAPIManager.route("/submit", method=HTTPMethod.POST)
    async def submit(self, current_user: User = Depends(decode_auth_token)):
        # raise HTTPException(
        #     status_code=400,
        #     detail={
        #         "message": "Já existe um pedido em andamento",
        #         "data": {"status": "order_in_progress", "id": str(uuid.uuid4())},
        #     },
        # )

        # raise HTTPException(
        #     status_code=400,
        #     detail={
        #         "message": "Alguns produtos não estão disponíveis",
        #         "data": {
        #             "status": "unavailable_products",
        #             "products": [
        #                 {"id": "C1012", "name": "Produto 1"},
        #                 {"id": "C1013", "name": "Produto 2"},
        #             ],
        #         },
        #     },
        # )

        return {
            "message": "Carrinho confirmado com sucesso",
            "data": {
                "id": uuid.uuid4(),
                "status": "waiting_payment",
                "resume": {
                    "total_items": 2,
                    "total_price": 100.00,
                    "total_discount": 10.00,
                    "total_price_with_discount": 90.00,
                    "items": [
                        {
                            "id": "C1012",
                            "name": "Produto 1",
                            "price": 50.00,
                            "quantity": 1,
                            "total_price": 50.00,
                            "total_discount": 5.00,
                            "total_price_with_discount": 45.00,
                        },
                        {
                            "id": "C1013",
                            "name": "Produto 2",
                            "price": 50.00,
                            "quantity": 1,
                            "total_price": 50.00,
                            "total_discount": 5.00,
                            "total_price_with_discount": 45.00,
                        },
                    ],
                },
            },
        }
