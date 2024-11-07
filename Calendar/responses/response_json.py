from fastapi.responses import JSONResponse

#En esta sección devuelve la respuesta del servidor, si fue correcta muestra 200
def response_json(message: str, status: int = 200)-> JSONResponse:
    return JSONResponse(content={"message": message}, status_code=status)