import logging
import os
import grpc
import sys
sys.path.append('grpc/chatgpt/pb')
import rpc_chat_gpt_pb2
import service_open_ai_pb2_grpc
from dotenv import load_dotenv
load_dotenv()

def run():
    print("Will try to chatgpt world ...")
    openai_grpc_server_port = os.getenv("OPENAI_GRPC_SERVER_PORT")
    with grpc.insecure_channel(f"localhost:{openai_grpc_server_port}") as channel:
        stub = service_open_ai_pb2_grpc.OpenAiStub(channel)
        reply = stub.ChatGpt(rpc_chat_gpt_pb2.ChatGptRequest(role='user',content='yoyoyo'))
    print("chatgpt client received: " + reply.response)
    
if __name__ == '__main__':
    logging.basicConfig()
    run()