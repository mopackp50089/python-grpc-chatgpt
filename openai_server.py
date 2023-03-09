from concurrent import futures
import logging

import grpc
# from chaptgpt import gptTurbo 
import openai
import os
from dotenv import load_dotenv
load_dotenv()

import sys
sys.path.append('grpc/chatgpt/pb')
import rpc_chat_gpt_pb2
import service_open_ai_pb2_grpc


class Openai(service_open_ai_pb2_grpc.OpenAiServicer):
    def __init__(self,openai,model):
        super().__init__()
        self.openai = openai
        self.model = model
    def ChatGpt(self, request, context):
        reply = self.openai.ChatCompletion.create(
            model=self.model, 
            messages=[
                {"role": request.role, "content": request.content},
                ]
        )
        return rpc_chat_gpt_pb2.ChatGptReply(response='%s' % reply['choices'][0]['message']['content'])
    

def serve():
    openai_grpc_server_port = os.getenv("OPENAI_GRPC_SERVER_PORT")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    openai.api_key = os.getenv("OPENAI_API_KEY")
    service_open_ai_pb2_grpc.add_OpenAiServicer_to_server(Openai(openai,"gpt-3.5-turbo"), server)
    server.add_insecure_port('[::]:' + openai_grpc_server_port)
    server.start()
    print("Server started, listening on " + openai_grpc_server_port)
    server.wait_for_termination()
    
if __name__ =='__main__':
    logging.basicConfig()
    serve()