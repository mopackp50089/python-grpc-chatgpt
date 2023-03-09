proto:
	python -m grpc_tools.protoc --proto_path=grpc/chatgpt/proto --python_out=grpc/chatgpt/pb --pyi_out=grpc/chatgpt/pb --grpc_python_out=grpc/chatgpt/pb grpc/chatgpt/proto/*.proto
server:
	python openai_server.py
client:
	python openai_client.py
.PHONY: proto server client