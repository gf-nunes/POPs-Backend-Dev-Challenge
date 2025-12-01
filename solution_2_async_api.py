import time
import uuid
import threading
from enum import Enum

jobs_db = {}

class JobStatus(Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"

def background_worker(job_id, data):
    
    print(f"\n[Worker] Processando Job {job_id} ({data})...")
    jobs_db[job_id]['status'] = JobStatus.PROCESSING
    
    time.sleep(5) 
    
    jobs_db[job_id]['status'] = JobStatus.COMPLETED
    jobs_db[job_id]['result'] = "Relatório Gerado com Sucesso"
    print(f"[Worker] Job {job_id} finalizado.\n")

class ReportController:
    
    def post_generate_report(self, request_data):
        
        job_id = str(uuid.uuid4())
        
        jobs_db[job_id] = {'status': JobStatus.PENDING, 'result': None}
        
        thread = threading.Thread(target=background_worker, args=(job_id, request_data))
        thread.start()
        
        return {
            "status": 202,
            "body": {
                "message": "Processamento iniciado.",
                "poll_url": f"/api/jobs/{job_id}"
            }
        }

    def get_job_status(self, job_id):

        job = jobs_db.get(job_id)
        if not job:
            return {"status": 404, "body": "Job não encontrado"}
            
        return {
            "status": 200, 
            "body": {
                "state": job['status'].value,
                "data": job['result'] if job['status'] == JobStatus.COMPLETED else None
            }
        }

if __name__ == "__main__":
    api = ReportController()
    
    print("1. Cliente solicita relatório pesado...")
    response = api.post_generate_report("Dados Financeiros 2023")
    print(f"   API Respondeu: HTTP {response['status']} - {response['body']}")
    
    job_id = response['body']['poll_url'].split('/')[-1]
    
    print("\n2. Cliente faz Polling (esperando conclusão)...")
    while True:
        status = api.get_job_status(job_id)
        state = status['body']['state']
        print(f"   Status atual: {state}")
        
        if state == "COMPLETED":
            print(f"   >> Resultado recebido: {status['body']['data']}")
            break
        
        time.sleep(2)