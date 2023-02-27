from httpx import AsyncClient
# import pytest
#
# @pytest.mark.asyncio
async def test_health_check(ac: AsyncClient):
    data = {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }
    async for client in ac:
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == data

    # response = await ac.get("/")
    #
    # assert response.status_code == 200
    # assert response.json() == data
