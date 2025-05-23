from http import HTTPMethod
from typing import List

from fastapi import Depends
from modules.authentication.adapters.presentation.dependencies import decode_auth_token
from modules.order.application.dtos.request_order import RequestOrder
from modules.shared.adapters.presentation.decorators import (
    FastAPIManager,
    ControllerOptions,
    APIController,
)
from modules.shared.infra.dependency_injector.containers.core_container import (
    CoreContainer,
)
from modules.user.domain.entities import User


@FastAPIManager.controller("order", ControllerOptions(tags="Order"))
class OrderController(APIController):
    def __init__(self):
        self.__create_new_order_use_case = CoreContainer.create_new_order_use_case()
        self.__complete_order_use_case = CoreContainer.complete_order_use_case()
        super().__init__()

    @FastAPIManager.route(
        "{id}/complete",
        method=HTTPMethod.POST,
        dependencies=[Depends(decode_auth_token)],
    )
    async def complete(self, id: str, current_user: User = Depends(decode_auth_token)):
        return await self.__complete_order_use_case.process(
            current_user.id, current_user.session_id, id
        )

    @FastAPIManager.route("/submit", method=HTTPMethod.POST)
    async def submit(
        self,
        order_request: List[RequestOrder],
        current_user: User = Depends(decode_auth_token),
    ):
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
        return await self.__create_new_order_use_case.process(
            current_user.id, current_user.session_id, order_request
        )
