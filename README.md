[![Security Pipeline](https://github.com/GuillaumeFalourd/formulas-gRPC/actions/workflows/security_pipeline.yml/badge.svg)](https://github.com/GuillaumeFalourd/formulas-gRPC/actions/workflows/security_pipeline.yml)

# Formulas Google Remote Procedure Call (gRPC)

## 📚 Documentation

This repository contains Ritchie `poc formulas` consuming gRPC services which can be executed by [ritchie-cli](https://github.com/ZupIT/ritchie-cli).

- [Ritchie CLI documentation](https://docs.ritchiecli.io)

## 📊 Use Formulas

To import this repository, you need [Ritchie CLI installed](https://docs.ritchiecli.io/getting-started/installation)

Then, you can use the `rit add repo` command manually, or execute the command line below directly on your terminal (since CLI version 2.8.0):

```bash
rit add repo --provider="Github" --name="formulas-gRPC" --repoUrl="https://github.com/GuillaumeFalourd/formulas-gRPC" --priority=1 --tag="1.3.0"
```

Finally, you can check if the repository has been imported correctly by executing the `rit list repo` command.

## 🔎 Formulas available on this repository

- `rit grpc golang hello-world`
  - *Formula to consume a local gRPC API on a **hello-world server** running through [this repository](https://github.com/GuillaumeFalourd/poc-grpc-golang)*.
  - [Formula README file](https://github.com/GuillaumeFalourd/formulas-gRPC/tree/main/grpc/golang/hello-world)

- `rit grpc golang poc`
  - *Formula to consume a local gRPC API on a **login server** running through [this repository](https://github.com/GuillaumeFalourd/poc-grpc-golang)*.
  - [Formula README file](https://github.com/GuillaumeFalourd/formulas-gRPC/tree/main/grpc/golang/poc)
  - This example use the `*.proto` file as submodule to then generate `*.go` files with the `protoc` command.

- `rit grpc java login`
  - *Formula to consume a local gRPC API on a **login server** running through [this repository](https://github.com/GuillaumeFalourd/poc-grpc-java-maven)*.
  - [Formula README file](https://github.com/GuillaumeFalourd/formulas-gRPC/tree/main/grpc/java/login)

- `rit grpc python message`
  - *Formula to consume a local gRPC API on a **message server** running through [this repository](https://github.com/GuillaumeFalourd/poc-grpc-python)*.
  - [Formula README file](https://github.com/GuillaumeFalourd/formulas-gRPC/tree/main/grpc/python/message)

## ♻️ Contribute to the repository with your formulas

### 🆕 Creating formulas

1. Fork and clone the repository
2. Create a branch: `git checkout -b <branch_name>`
3. Check the step by step of [how to create formulas on Ritchie](https://docs.ritchiecli.io/tutorials/formulas/how-to-create-formulas)
4. Add your formulas to the repository
and commit your implementation: `git commit -m '<commit_message>`
5. Push your branch: `git push origin <project_name>/<location>`
6. Open a pull request on the repository for analysis.

### 🆒 Updating Formulas

1. Fork and clone the repository
2. Create a branch: `git checkout -b <branch_name>`
3. Add the cloned repository to your workspaces (`rit add workspace`) with a highest priority (for example: 1).
4. Check the step by step of [how to implement formulas on Ritchie](https://docs.ritchiecli.io/tutorials/formulas/how-to-implement-a-formula)
and commit your implementation: `git commit -m '<commit_message>`
5. Push your branch: `git push origin <project_name>/<location>`
6. Open a pull request on the repository for analysis.

- [Contribute to Ritchie community](https://github.com/ZupIT/ritchie-formulas/blob/master/CONTRIBUTING.md)
