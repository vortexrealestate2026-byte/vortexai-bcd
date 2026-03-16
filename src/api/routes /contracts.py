from ..services.contracts.contract_generator import generate_contract
from ..services.contracts.esign_client import send_for_signature
from ..schemas.contract import ContractGenerateRequest, ContractGenerateResponse

def generate_and_send_contract(req: ContractGenerateRequest):
    html = generate_contract(req.contract_type, req.context)

    esign_status = None
    if req.signer_email:
        result = send_for_signature(
            signer_email=req.signer_email,
            signer_name=req.signer_name or "",
            html_document=html
        )
        esign_status = result.get("status") or result.get("esign_status")

    return ContractGenerateResponse(
        contract_type=req.contract_type,
        html=html,
        signer_email=req.signer_email,
        signer_name=req.signer_name,
        esign_status=esign_status
    )
