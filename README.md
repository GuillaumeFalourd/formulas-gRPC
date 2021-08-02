[![Security Pipeline](https://github.com/GuillaumeFalourd/formulas-gRPC/actions/workflows/security_pipeline.yml/badge.svg)](https://github.com/GuillaumeFalourd/formulas-gRPC/actions/workflows/security_pipeline.yml)

# Formulas gRPC

## 📚 Documentation

This repository contains Ritchie formulas which can be executed by [ritchie-cli](https://github.com/ZupIT/ritchie-cli).

- [Ritchie CLI documentation](https://docs.ritchiecli.io)
- [Step by step to create a Github profile with Ritchie CLI](https://bit.ly/devtoritgithubcreateprofile)

## 📊 Use Formulas

To import this repository, you need [Ritchie CLI installed](https://docs.ritchiecli.io/getting-started/installation)

Then, you can use the `rit add repo` command manually, or execute the command line below directly on your terminal (since CLI version 2.8.0):

```bash
rit add repo --provider="Github" --name="formulas-gRPC" --repoUrl="https://github.com/GuillaumeFalourd/formulas-gRPC" --priority=1
```

Finally, you can check if the repository has been imported correctly by executing the `rit list repo` command.
