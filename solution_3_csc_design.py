from abc import ABC, abstractmethod

class ServiceRequest:
    def __init__(self, user_id, request_type, metadata):
        self.user_id = user_id
        self.request_type = request_type
        self.metadata = metadata

class IServiceHandler(ABC):
    @abstractmethod
    def validate(self, req: ServiceRequest):
        pass

    @abstractmethod
    def process(self, req: ServiceRequest):
        pass

class VacationHandler(IServiceHandler):
    def validate(self, req: ServiceRequest):
        print(f"[Férias] Verificando saldo de dias do usuário {req.user_id}...")
        if req.metadata.get('days') > 30:
            raise ValueError("Máximo de 30 dias permitido.")
            
    def process(self, req: ServiceRequest):
        print(f"[Férias] Notificando RH e Financeiro para período de {req.metadata.get('days')} dias.")

class CarLoanHandler(IServiceHandler):
    def validate(self, req: ServiceRequest):
        print(f"[Carro] Verificando CNH e disponibilidade de frota...")
        
    def process(self, req: ServiceRequest):
        print(f"[Carro] Veículo reservado. Chave na portaria.")

class TravelHandler(IServiceHandler):
    def validate(self, req: ServiceRequest):
        print(f"[Viagem] Verificando políticas de orçamento...")
        
    def process(self, req: ServiceRequest):
        print(f"[Viagem] Passagens compradas via API da Agência.")

class ServiceFactory:
    @staticmethod
    def get_handler(request_type: str) -> IServiceHandler:
        mapping = {
            "VACATION": VacationHandler(),
            "CAR_LOAN": CarLoanHandler(),
            "TRAVEL": TravelHandler()
        }
        handler = mapping.get(request_type)
        if not handler:
            raise ValueError(f"Serviço '{request_type}' não suportado.")
        return handler

def main():
    requests = [
        ServiceRequest(101, "VACATION", {"days": 15}),
        ServiceRequest(102, "CAR_LOAN", {"model": "Sedan"}),
        ServiceRequest(103, "TRAVEL",   {"dest": "SP"}),
    ]

    factory = ServiceFactory()

    for req in requests:
        try:
            print(f"--- Processando {req.request_type} ---")
            handler = factory.get_handler(req.request_type)
            handler.validate(req)
            handler.process(req)
            print(">> Sucesso.")
        except Exception as e:
            print(f">> Erro: {e}")
        print()

if __name__ == "__main__":
    main()