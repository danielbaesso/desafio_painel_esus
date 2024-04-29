from flask import Blueprint, request, jsonify
from ..services import AtendimentosService
from ..models.dto.atendimento_dto import AtendimentoDto
from ..models.dto.atendimento_response_dto import AtendimentoResponseDto
from ..models.dto.atendimento_filter_dto import AtendimentoFilterDto
from ..models.exception.business_logic_exception import BusinessLogicException

consultas_bp = Blueprint('atendimentos', __name__)

@consultas_bp.route('/api/v1/atendimentos', methods=['GET'])
def get_atendimentos():
    response = AtendimentoResponseDto()
    try:
        atendimentos_service = AtendimentosService()
        atendimento_filter = atendimentos_service.extract_request_args(request.args)
        result = atendimentos_service.find_with_filter(atendimento_filter)
        serialized_atendimentos = [atendimento.serialize() for atendimento in result]
        response.status = "Ok"
        response.atendimentos = serialized_atendimentos
    except BusinessLogicException as e:
        response.status = "Error"
        response.message = e.message
    return jsonify(response.serialize())