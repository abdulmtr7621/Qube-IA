from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def root():
    return {'message': 'Qube IA backend running!'}