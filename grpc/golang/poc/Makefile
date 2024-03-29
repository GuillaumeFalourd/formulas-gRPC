# The Makefile file will be deprecated in March 2021. It will be replaced by the current build.sh file
# Go parameters

BIN_FOLDER=bin
SH=$(BIN_FOLDER)/run.sh
BAT=$(BIN_FOLDER)/run.bat
BIN_NAME=main
PROTO_GO_DIR=src/pkg/formula
GOCMD=go
GOBUILD=$(GOCMD) build
GOTEST=$(GOCMD) test
CMD_PATH=main.go
BIN_FOLDER_DARWIN=../$(BIN_FOLDER)/darwin
BIN_DARWIN=$(BIN_FOLDER_DARWIN)/$(BIN_NAME)
BIN_FOLDER_LINUX=../$(BIN_FOLDER)/linux
BIN_LINUX=$(BIN_FOLDER_LINUX)/$(BIN_NAME)
BIN_FOLDER_WINDOWS=../$(BIN_FOLDER)/windows
BIN_WINDOWS=$(BIN_FOLDER_WINDOWS)/$(BIN_NAME).exe


build: go-build sh-unix bat-windows docker

gen-go-proto:
	mkdir -p src/pkg/formula
	protoc --go_out=src/pkg/formula \
		--go_opt=paths=source_relative \
		--go-grpc_out=src/pkg/formula \
		--go-grpc_opt=paths=source_relative \
		protos/user/user.proto

go-build:
	cd src; mkdir -p $(BIN_FOLDER_DARWIN) $(BIN_FOLDER_LINUX) $(BIN_FOLDER_WINDOWS)
	#LINUX
	cd src; CGO_ENABLED=0 GOOS=linux GOARCH=amd64 $(GOBUILD) -o '$(BIN_LINUX)' $(CMD_PATH)
	#MAC
	cd src; GOOS=darwin GOARCH=amd64 $(GOBUILD) -o '$(BIN_DARWIN)' $(CMD_PATH)
	#WINDOWS 64
	cd src; GOOS=windows GOARCH=amd64 $(GOBUILD) -o '$(BIN_WINDOWS)' $(CMD_PATH)

sh-unix:
	echo '#!/bin/sh' > $(SH)
	echo 'if [ $$(uname) = "Darwin" ]; then' >> $(SH)
	echo '  "$$(dirname "$$0")"/darwin/$(BIN_NAME)' >> $(SH)
	echo 'else' >> $(SH)
	echo '  "$$(dirname "$$0")"/linux/$(BIN_NAME)' >> $(SH)
	echo 'fi' >> $(SH)
	chmod +x $(SH)

bat-windows:
	echo '@ECHO OFF' > $(BAT)
	echo 'SET mypath=%~dp0' >> $(BAT)
	echo 'start /B /D "%mypath%" /WAIT windows\main.exe' >> $(BAT)

docker:
	cp Dockerfile set_umask.sh $(BIN_FOLDER)

test:
	$(GOTEST) -short `go list ./... | grep -v vendor/`
