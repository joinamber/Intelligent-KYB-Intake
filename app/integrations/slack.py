import json, os, urllib.request
def render_slack_work_item(assessment):
    missing=[r.label for r in assessment.requirements if r.status.value=="MISSING"]
    complete=[r.label for r in assessment.requirements if r.status.value=="SATISFIED"]
    return {"case_id":assessment.submission_id,"title":f"KYB Intake — {assessment.merchant_id}","status":assessment.status.value,"complete":complete,"missing":missing,"recommended_action":assessment.next_action,"human_review_required":assessment.human_review_required,"actions":["ACCEPT","EDIT","ESCALATE","WRONG_MERCHANT","PROCESSING_ERROR"]}
class LoggingSlackNotifier:
    def send(self, work_item): return {"delivered":False,"mode":"log","work_item":work_item}
class WebhookSlackNotifier:
    def __init__(self,url=None): self.url=url or os.getenv("SLACK_WEBHOOK_URL")
    def send(self,work_item):
        if not self.url: raise ValueError("SLACK_WEBHOOK_URL required")
        text=f"*{work_item['title']}*\nStatus: {work_item['status']}\nMissing: {', '.join(work_item['missing']) or 'None'}\nNext: {work_item['recommended_action']}"
        req=urllib.request.Request(self.url,data=json.dumps({"text":text}).encode(),headers={"Content-Type":"application/json"})
        with urllib.request.urlopen(req,timeout=10) as r:r.read()
        return {"delivered":True,"mode":"webhook"}
