# Description

Formula (poc) to consume an gRPC API.

This formula is locally consuming a method `Login` from the server generated by [this repository](https://github.com/GuillaumeFalourd/poc-grpc-java-maven).

## Command

```bash
rit grpc java login
```

## Requirements

- Java 8
- [This repository](https://github.com/GuillaumeFalourd/poc-grpc-java-maven) message server running locally (`localhost:9090`).

## Demonstration

**After running the server:**

![Server](https://user-images.githubusercontent.com/22433243/128190844-82729fa1-0fd0-43e6-97f3-7fbe80d7daa2.png)

**Run the formula command:**

![Formula](https://user-images.githubusercontent.com/22433243/128190899-9a5c7c05-5eb2-426e-a5f4-da41273595d8.png)
